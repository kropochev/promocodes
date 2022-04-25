# Promo code generator
Cервис создания промокодов и проверки их на существование.

## Установка
Клонировать этот репозиторий. `git clone https://github.com/kropochev/promocodes.git`

## Запуск с помощью Docker-Compose
1. Проверить, что `Docker` работает локально.
2. Создать образ `docker-compose build`.
3. Запустить `docker-compose up`.

## Создание промокода
```
curl --location --request POST 'http://127.0.0.1:8000/promo/create/' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
  "amount": 5,
  "group": "test"
}'
```

## Проверка промокода
```
curl --location --request POST 'http://127.0.0.1:8000/promo/check/' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
  "promo_code": "b7b4b905d4564п27e9acf0844da2d302a"
}'
```