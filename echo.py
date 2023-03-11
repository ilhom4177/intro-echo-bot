import json, requests, time

TOKIN = '6120715010:AAEy_jm_fXcAqxRtRT_vJiKPL3tXtiGcNLQ'

def get_last_update():
    url = f'https://api.telegram.org/bot{TOKIN}/getUpdates'
    data = requests.get(url)
    return data.json()

def sendMessage(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKIN}/sendMessage'
    data = requests.get(url, params={'chat_id':chat_id, 'text':text})
    return data.json()

def sendDocument(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKIN}/sendDocument'
    data = requests.get(url, params={'chat_id':chat_id, 'text':document})
    return data.json()

def sendPhoto(chat_id, photo):
    url = f'https://api.telegram.org/bot{TOKIN}/sendPhoto'
    data = requests.get(url, params={'chat_id':chat_id, 'photo':photo})
    return data.json()

def sendDice(chat_id, emoji):
    url = f'https://api.telegram.org/bot{TOKIN}/sendDice'
    data = requests.get(url, params={'chat_id':chat_id, 'emoji':emoji})
    return data.json()

def sendSticker(chat_id, sticker):
    url = f'https://api.telegram.org/bot{TOKIN}/sendSticker'
    data = requests.get(url, params={'chat_id':chat_id, 'sticker':sticker})
    return data.json()

def sendVideo(chat_id, video):
    url = f'https://api.telegram.org/bot{TOKIN}/sendVideo'
    data = requests.get(url, params={'chat_id':chat_id, 'video':video})
    return data.json()

def sendAudio(chat_id, audio):
    url = f'https://api.telegram.org/bot{TOKIN}/sendAudio'
    data = requests.get(url, params={'chat_id':chat_id, 'audio':audio})
    return data.json()

def sendVoice(chat_id, voice):
    url = f'https://api.telegram.org/bot{TOKIN}/sendVoice'
    data = requests.get(url, params={'chat_id':chat_id, 'voice':voice})
    return data.json()


def main(chat_id, text, photo, emoji, sticker, video, audio, voice):
   
    if text:
        sendMessage(chat_id, text)
    elif photo:
        sendPhoto(chat_id, photo)
    elif emoji:
        sendDice(chat_id, emoji)
    elif sticker:
        sendSticker(chat_id, sticker)
    elif video:
        sendVideo(chat_id, video)
    elif audio:
        sendAudio(chat_id, audio)
    elif voice:
        sendVoice(chat_id, voice)
   

def getData(data):
    data = data['result'][-1]
    update_id = data['update_id']
    chat_id = data['message']['from']['id']

    text = data['message'].get('text')
    document = data['message'].get('document')
    photo = data['message'].get('photo')
    emoji = data['message'].get('dice')
    sticker = data['message'].get('sticker')
    video = data['message'].get('video')
    audio = data['message'].get('audio')
    voice = data['message'].get('voice')


    if voice:
        voice = voice['file_id']
    if video:
        video = video['file_id']
    if audio:
        audio = audio['file_id']
    if sticker:
        sticker = sticker['file_id']
    if emoji:
        emoji = emoji['emoji']
    
    if photo:
        photo = photo[0]['file_id']
    return update_id, chat_id, text,photo, emoji, sticker, video, audio, voice

s = ''
while True:
    data = getData(get_last_update())
    update_id, chat_id,  text, photo, emoji, sticker, video, audio, voice = data
    if s != update_id:
        main(chat_id, text, photo, emoji, sticker, video, audio, voice)
        s = update_id
    
    time.sleep(0.1)
