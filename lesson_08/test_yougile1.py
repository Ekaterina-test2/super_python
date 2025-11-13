import requests
import config
from my_autorization import Entinto


def Myauth():
    resultauth = Entinto.TestAuth()
    if resultauth == 'error':
        resultauthT = Entinto.MakeKey()
        resultauth = resultauthT
    return resultauth


def test_MetodGet_Pozi():
    Result = Myauth()
    assert Result != 'error'
    config.heade['Authorization'] = 'Bearer ' + Result
    result = requests.get(config.base_url + 'projects/'+Entinto.CompanyListP(Result), headers=config.heade)
    assert result.status_code == 200


def test_MetodGet_Nega():
    Result = Myauth()
    assert Result != 'error'
    config.heade['Authorization'] = 'Bearer ' + Result
    result = requests.get(config.base_url + 'pojects/'+Entinto.CompanyListP(Result), headers=config.heade)
    assert result.status_code == 404


def test_MetodPost_Pozi():
    Result = Myauth()
    assert Result != 'error'
    config.heade['Authorization'] = 'Bearer ' + Result
    MyUsersId = requests.get(config.base_url + 'users', headers=config.heade)
    d = MyUsersId.json()['content'][0]['id']
    config.payload['users'].setdefault(d, 'admin')
    result = requests.post(config.base_url + 'projects', json=config.payload, headers=config.heade)
    assert result.status_code == 201


def test_MetodPost_Nega():
    Result = Myauth()
    assert Result != 'error'
    config.heade['Authorization'] = 'Bearer ' + Result
    d = config.dann_auth['companyId']
    config.payload['users'].setdefault(d, 'admin')
    result = requests.post(config.base_url + 'projects', json=config.payload, headers=config.heade)
    assert result.status_code == 400


def test_MetodPut_Pozi():
    Result = Myauth()
    assert Result != 'error'
    config.heade['Authorization'] = 'Bearer ' + Result
    MyUsersId = requests.get(config.base_url + 'users', headers=config.heade)
    d = MyUsersId.json()['content'][0]['id']
    config.payload['users'].setdefault(d, 'admin')
    result = requests.post(config.base_url + 'projects', json=config.payload, headers=config.heade)
    config.payload['title'] = config.payload['title']+'(Изменено)'
    resu = requests.put(config.base_url+'projects/'+result.json()['id'], json=config.payload, headers=config.heade)
    assert resu.status_code == 200


def test_MetodPut_Nega():
    Result = Myauth()
    assert Result != 'error'
    config.heade['Authorization'] = 'Bearer ' + Result
    MyUsersId = requests.get(config.base_url + 'users', headers=config.heade)
    d = MyUsersId.json()['content'][0]['id']
    config.payload['users'].setdefault(d, 'admin')
    config.payload['title'] = config.payload['title']+'(Изменено)'
    resu = requests.put(config.base_url+'projects/'+config.dann_auth['companyId'], json=config.payload, headers=config.heade)
    assert resu.status_code == 404
