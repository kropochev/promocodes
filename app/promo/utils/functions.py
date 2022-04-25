import json
import uuid


def create(data):
    group = data["group"]
    amount = data["amount"]
    code = uuid.uuid4
    new_promo_codes = [str(code()).replace("-", "") for _ in range(amount)]

    try:
        with open('data.json', 'r', encoding='UTF-8') as fp:
            file_data = json.load(fp)
            if group in file_data.keys():
                promo_codes = file_data.pop(group)
                promo_codes.extend(new_promo_codes)
                file_data.update({group: promo_codes})
            else:
                file_data[group] = new_promo_codes
    except FileNotFoundError:
        file_data = {group: new_promo_codes}

    with open('data.json', 'w', encoding='UTF-8') as fp:
        json.dump(file_data, fp, indent=4, ensure_ascii=False)

    return f"Created {amount} promocode(s)"


def check(data):
    promo_code = data["promo_code"]

    try:
        with open('data.json', 'r', encoding='UTF-8') as fp:
            file_data = json.load(fp)
            for group, promo_codes in file_data.items():
                if str(promo_code) in promo_codes:
                    return f"Код существует, группа = {group}"
                else:
                    return "Код не существует"
    except FileNotFoundError:
        message = "Промокодов нет"

    return message
