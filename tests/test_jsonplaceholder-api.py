""""Тесты для API сервиса https://jsonplaceholder.typicode.com/"""

import requests
import pytest
from random import uniform
import json


def test_json_placeholder_post(json_base_url):
    link = json_base_url + 'posts'
    assert requests.get(link).status_code == 200


@pytest.mark.parametrize("post", [int(uniform(1, 99)) for x in range(10)])
def test_get_results_by_name(json_base_url, posts_list, post):
    link = json_base_url + 'posts/' + str(post)
    result = requests.get(link)
    json_data = json.loads(result.content)
    print('Post number=', post, json_data['title'], ' = ', posts_list[post - 1]['title'])
    assert (json_data['title'] == posts_list[post - 1]['title']) & (result.status_code == 200)


@pytest.mark.parametrize("post", [int(uniform(1, 99)) for x in range(10)])
def test_update_resource(json_base_url, post):
    link = json_base_url + 'posts/' + str(post)
    new_data = {'id': post - 1,
                'title': 'random_title ' + str(post),
                'body': 'random_body ' + str(post),
                'userId': int(uniform(1, 99))}
    result = requests.put(link, json.dumps(new_data))
    json_data = json.loads(result.content)
    print('Put post', post, 'returned', json_data['id'])
    assert (json_data['id'] == post) & (result.status_code == 200)


@pytest.mark.parametrize("post", [int(uniform(1, 99)) for x in range(10)])
def test_delete_resource(json_base_url, post):
    link = json_base_url + 'posts/' + str(post)
    result = requests.delete(link)
    print('Delete post', post)
    assert result.status_code == 200


def test_json_placeholder_post(json_base_url):
    link = json_base_url + 'posts/1/comments'
    assert requests.get(link).status_code == 200
