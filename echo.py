import requests

TOKEN = '6097521187:AAHbPqQPSlFP54uT-Sj6MdnJpeBB_5Idsmg'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'

def get_last_update():
    # make url for getupdates
    url_for_getupdates = BASE_URL + "getUpdates"
    # meke request
    response = requests.get(url_for_getupdates)
    # check rsponse status
    if response.status_code == 200:
        # get data from response as dict
        data = response.json()
        # get result
        result = data['result']
        # get last update
        last_update = result[-1]
        return last_update
    return False

def sendMessage():
    pass

def main():
    last_update = get_last_update()
    print(last_update)

main()