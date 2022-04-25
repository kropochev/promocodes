import os
import json

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


PROMO_CREATE_URL = reverse('promo:create')
PROMO_CHECK_URL = reverse('promo:check')


class APITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        os.remove('data.json')

    def test_create_promo(self):
        """Тест проверяет создание промокодов"""

        payload1 = {'amount': 10, 'group': 'агенства'}
        res1 = self.client.post(PROMO_CREATE_URL, payload1)

        payload2 = {'amount': 1, 'group': 'агенства'}
        res2 = self.client.post(PROMO_CREATE_URL, payload2)

        payload3 = {'amount': 42, 'group': 'avtostop'}
        res3 = self.client.post(PROMO_CREATE_URL, payload3)

        payload4 = {'amount': 5, 'group': 1}
        res4 = self.client.post(PROMO_CREATE_URL, payload4)

        self.assertEqual(res1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res3.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res4.status_code, status.HTTP_201_CREATED)

        with open('data.json', 'r', encoding='UTF-8') as fp:
            file_data = json.load(fp)
            groups = []
            promo_codes = []
            for group, promo in file_data.items():
                groups.append(group)
                promo_codes.extend(promo)

        self.assertEqual(len(groups), 3)
        self.assertEqual(len(promo_codes), 58)

    def test_check_promo(self):
        """Тест проверяет наличие промокода в json файле"""

        payload_create = {'amount': 1, 'group': 'test'}
        res = self.client.post(PROMO_CREATE_URL, payload_create)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        with open('data.json', 'r', encoding='UTF-8') as fp:
            file_data = json.load(fp)
            promo_code = file_data['test'][0]

        payload_check = {'promo_code': promo_code}
        res = self.client.post(PROMO_CHECK_URL, payload_check)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn(payload_create['group'], res.data)
