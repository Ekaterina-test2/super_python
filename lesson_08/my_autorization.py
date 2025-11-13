import requests
import config


class Entinto():
    def TestAuth():
        resp = requests.post(config.base_url+"auth/keys/get", json=config.dann_auth, headers={"Content-Type": "application/json"})
        if resp.status_code == 200:
            return resp.json()[0]['key']
        else:
            return 'error'

    def MakeKey():
        resp = requests.post(config.base_url + 'auth/keys', json=config.dann_auth)
        if resp.status_code == 201:
            return resp.json()['key']
        else:
            return 'error'

    def CompanyListP(MyKey):
        resp = requests.get(config.base_url + 'projects', headers=config.heade)
        if resp.status_code == 200:
            return resp.json()['content'][0]['id']

    def CompanyListN():
        resp = requests.get(config.base_url + 'projects', headers=config.heade)
        if resp.status_code == 200:
            return resp.json()['content'][0]['title']
