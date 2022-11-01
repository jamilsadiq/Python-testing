from urllib import response
import pytest
import requests
import json
def test_post_data(supply_url):
	url = supply_url + "/users/" 
	data = {'name':'morpheus','job':'leader'}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 201, resp.text
	assert j['name'] == "morpheus", resp.text
	assert j['job'] == "leader", resp.text
def test_post_empty_data(supply_url):
	url = supply_url + "/users/" 
	data = {'name':'','job':''}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 201, resp.text
	assert j['name'] == "", resp.text
	assert j['job'] == "", resp.text

    