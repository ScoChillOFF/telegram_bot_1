import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
CAT_API_URL: str = 'https://api.thecatapi.com/v1/images/search'
BOT_TOKEN: str = '6266775802:AAEh9pNqqdW-4_NVQp5ygtDB-j6ErZkEOSo'
ERROR_TEXT: str = 'котик сбежав :('
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
updates: dict
chat_id: int
cat_response: requests.Response
curr_message: str
timeout: int = -15.22
start_time: float
end_time: float


while counter < MAX_COUNTER:

    start_time = time.time()

    print('attempt =', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            try:
                chat_id = result['message']['chat']['id']
            except:
                chat_id = result['edited_message']['chat']['id']
            cat_response = requests.get(CAT_API_URL)
            if cat_response.status_code == 200:
                curr_message = result['message']['text']
                cat_photo_id = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text="{curr_message.capitalize()}"? А может лучше...')
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_photo_id}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    end_time = time.time()
    print(end_time - start_time)
    counter += 1