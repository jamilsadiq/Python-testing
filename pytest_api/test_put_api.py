from urllib import response
import pytest
import requests
import json

def test_post_data(supply_url):
	url = supply_url + "/users/2" 
	data = {'name':'morpheus','job':'zion resident'}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 201, resp.text
	assert j['name'] == "morpheus", resp.text
	assert j['job'] == "zion resident", resp.text 
