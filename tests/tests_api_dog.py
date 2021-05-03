import pytest
import requests


def test_show_several_random_images_status():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response.json()['status'] == 'success'


def test_show_several_random_images_1():
    response = requests.get("https://dog.ceo/api/breeds/image/random/1")
    assert len(response.json()['message']) == 1


@pytest.mark.parametrize("quantity", [50, 51])
def test_show_several_random_images(quantity):
    response = requests.get(f"https://dog.ceo/api/breeds/image/random/{quantity}")
    assert len(response.json()['message']) == 50


def test_get_all_breeds_status():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.json()['status'] == 'success'


@pytest.mark.parametrize("breed", ["affenpinscher", "basenji", "clumber"])
def test_show_random_image_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    assert response.json()['message'].startswith(f"https://images.dog.ceo/breeds/{breed}")
