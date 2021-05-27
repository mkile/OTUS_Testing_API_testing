""""Тесты для API сервиса https://www.openbrewerydb.org/"""

import requests
import pytest
import json
from random import uniform


def test_api_main_link_working(brew_base_url):
    link = brew_base_url + 'breweries'
    assert requests.get(link).status_code == 200


@pytest.mark.parametrize("br_type", ['micro', 'nano', 'regional',
                                     'brewpub', 'large', 'planning', 'bar',
                                     'contract', 'proprietor', 'closed'])
def test_get_brew_by_type(brew_base_url, br_type):
    link = brew_base_url + 'breweries?by_type=' + br_type
    assert requests.get(link).status_code == 200


@pytest.mark.parametrize("brews_per_page", [10, 20, 30, 40])
def test_get_results_per_page(brew_base_url, brews_per_page):
    link = brew_base_url + 'breweries?per_page=' + str(brews_per_page)
    result = requests.get(link)
    json_data = json.loads(result.content)
    assert (result.status_code == 200) & (len(json_data) == brews_per_page)


@pytest.mark.parametrize("brew", [int(uniform(10, 40)) for x in range(5)])
def test_get_results_by_name(brew_base_url, base_brews_list, brew):
    link = brew_base_url + 'breweries?by_name=' + base_brews_list[brew]['name']
    result = requests.get(link)
    json_data = json.loads(result.content)
    assert (json_data[0]['name'] == base_brews_list[brew]['name']) & (result.status_code == 200)


@pytest.mark.parametrize("brew", [int(uniform(10, 40)) for x in range(5)])
def test_get_results_by_city(brew_base_url, base_brews_list, brew):
    link = brew_base_url + 'breweries?by_city=' + base_brews_list[brew]['city']
    result = requests.get(link)
    json_data = json.loads(result.content)
    assert (len(json_data) > 0) & (result.status_code == 200)
