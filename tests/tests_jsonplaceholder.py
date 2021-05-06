import pytest
import requests


def test_get_a_list_of_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert len(response.json()) == 10


def test_get_a_list_of_todos():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    assert len(response.json()) == 200


def test_get_a_list_of_photos():
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    assert len(response.json()) == 5000


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_a_post_by_id(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.json()['id'] == post_id


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_a_list_commets_by_post_id(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={post_id}")
    for comment in response.json():
        assert comment['postId'] == post_id
