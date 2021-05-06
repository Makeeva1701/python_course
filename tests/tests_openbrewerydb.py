import pytest
import requests


def test_get_list_breweries():
    response = requests.get("https://api.openbrewerydb.org/breweries")
    assert len(response.json()) == 20


def test_presence_of_the_id_parameter_at_the_brewery():
    response = requests.get("https://api.openbrewerydb.org/breweries")
    for brewerie in response.json():
        assert brewerie['id']


@pytest.mark.parametrize("city", ["San Diego", "Alameda", "Colorado Springs"])
def test_get_a_list_of_breweries_by_city(city):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_city={city}")
    for brewerie in response.json():
        assert brewerie['city'] == city


@pytest.mark.parametrize("name", [
    "10 Barrel Brewing Co - Bend Pub",
    "32 North Brewing Co",
    "Acoustic Ales Brewing Experiment",
])
def test_get_a_list_of_breweries_by_name(name):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_name={name}")
    for brewerie in response.json():
        assert brewerie['name'] == name


@pytest.mark.parametrize("state", [
    "California",
    "Ohio",
    "New York",
])
def test_get_a_list_of_breweries_by_state(state):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_state={state}")
    for brewerie in response.json():
        assert brewerie['state'] == state


@pytest.mark.parametrize("type_breweries", [
    "micro",
    "nano",
    "regional",
    "brewpub",
    "large",
    "planning",
    "bar",
    "contract",
    "proprietor",
])
def test_get_a_list_of_breweries_by_type(type_breweries):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_type={type_breweries}")
    for brewerie in response.json():
        assert brewerie['brewery_type'] == type_breweries
