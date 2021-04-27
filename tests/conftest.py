import pytest
import requests
import json

"""Фикстуры для тестирования ссылки"""


def pytest_addoption(parser):
    parser.addoption("--url",
                     action='store',
                     help="Укажите ссылку",
                     default="https://ya.ru")
    parser.addoption("--status_code",
                     action='store',
                     help="Укажите код ответа",
                     default=200)


@pytest.fixture
def url_for_testing(request):
    return request.config.getoption("url")


@pytest.fixture
def status_code_for_testing(request):
    return int(request.config.getoption("status_code"))


"""Фикстуры для тестирования API сайта dog.ceo"""


@pytest.fixture(scope="module")
def dog_base_url():
    return "https://dog.ceo/api/"


@pytest.fixture(scope="module")
def dog_breeds(dog_base_url):
    sublink = 'breeds/list/all'
    result = requests.get(dog_base_url + sublink)
    if result.status_code == 200:
        breeds = json.loads(result.content)
        breeds = breeds['message']
        yield breeds
        del breeds
    else:
        print('Получить список пород не вышло, выдаем тестовый список')


@pytest.fixture(scope="module")
def dog_sub_breeds(dog_breeds):
    if isinstance(dog_breeds, dict):
        with_sub_breeds = {x: dog_breeds[x] for x in dog_breeds if len(dog_breeds[x]) > 0}
        yield with_sub_breeds
        del with_sub_breeds
    else:
        print('Список пород с подпородами создать не удалось.')


"""Фикстуры для тестирования API сайта openbreweries"""


@pytest.fixture(scope="module")
def brew_base_url():
    return "https://api.openbrewerydb.org/"


@pytest.fixture(scope="module")
def base_brews_list(brew_base_url):
    link = brew_base_url + 'breweries?per_page=50'
    result = requests.get(link).content
    breweries_list = json.loads(result)
    return breweries_list


"""Фикстуры для тестирования API сайта https://jsonplaceholder.typicode.com"""


@pytest.fixture(scope="module")
def json_base_url():
    return "https://jsonplaceholder.typicode.com/"


@pytest.fixture(scope="module")
def posts_list(json_base_url):
    link = json_base_url + 'posts'
    result = requests.get(link).content
    posts = json.loads(result)
    return posts
