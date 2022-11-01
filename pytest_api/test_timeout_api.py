import pytest
import requests
import json
import pytest_timeout

def test_list_valid_user(supply_url):
	timeout2 = .01
	url = supply_url + "/users?delay=3/"
	resp = requests.get(url,timeout=timeout2)
	j = json.loads(resp.text)
	assert resp.status_code == 200, resp.text
	assert j['page'] == 1, resp.text
	assert j['per_page'] == 6, resp.text
def timeout():
    pytest.fail("+++ Timeout +++")
