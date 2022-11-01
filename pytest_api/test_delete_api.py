from urllib import response
import pytest
import requests
import json

def test_post_data(supply_url):
	url = supply_url + "/users/2" 
	resp = requests.delete(url)
	assert resp.status_code == 204
