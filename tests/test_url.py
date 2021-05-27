import pytest
import requests

"""Тестирование соответствия запроса и кода ответа сервера"""


def test_url(url_for_testing, status_code_for_testing):
    request_result = requests.get(url_for_testing)
    assert request_result.status_code == status_code_for_testing
