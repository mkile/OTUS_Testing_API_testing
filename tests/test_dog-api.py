""""Тесты для API сервиса https://dog.ceo/"""
import requests
import pytest
import json


def test_get_all_breweries(dog_base_url):
    sublink = "breeds/list/all"
    link = dog_base_url + sublink
    assert requests.get(link).status_code == 200


def test_get_all_breeds_data(dog_breeds):
    print(dog_breeds)
    assert (isinstance(dog_breeds, dict) is True) & (len(dog_breeds) > 0)


def test_get_random_image(dog_base_url):
    sublink = "breeds/image/random"
    link = dog_base_url + sublink
    assert requests.get(link).status_code == 200


@pytest.mark.parametrize("breed_num", list(range(10)))
def test_get_random_image(dog_base_url, dog_breeds, breed_num):
    sublink = "/images"
    link = dog_base_url + 'breed/' + list(dog_breeds.keys())[breed_num] + sublink
    assert requests.get(link).status_code == 200, link


@pytest.mark.parametrize("breed_num", list(range(10)))
@pytest.mark.parametrize("sub_breed_num", list(range(2)))
def test_get_list_subbreed(dog_base_url, dog_sub_breeds, breed_num, sub_breed_num):
    sublink = "/list"
    dog_breeds_list = list(dog_sub_breeds.keys())
    dog_sub_breeds_list = list(dog_sub_breeds[dog_breeds_list[breed_num]])
    link = dog_base_url + 'breed/' + dog_breeds_list[breed_num] + sublink
    if len(dog_sub_breeds_list) < (sub_breed_num + 1):
        pytest.skip("Недостаточно подпород {} в породе {}, требовалось {}".format(len(dog_sub_breeds_list),
                                                                                  dog_breeds_list[breed_num],
                                                                                  sub_breed_num + 1))
    subbreeds = json.loads(requests.get(link).content)['message']
    assert (dog_sub_breeds_list[sub_breed_num] in list(subbreeds)) is True


@pytest.mark.parametrize("breed_num", list(range(10)))
def test_get_random_breed_image(dog_base_url, dog_breeds, breed_num):
    sublink = "/images/random"
    current_breed = list(dog_breeds.keys())[breed_num]
    link = dog_base_url + 'breed/' + current_breed + sublink
    assert requests.get(link).status_code == 200, current_breed
