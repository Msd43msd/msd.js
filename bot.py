import requests
from time import sleep
from os import environ
from sms import SendSms

token = environ.get('TOKEN')

def getUpdate():
    url = 'https://api.telegram.org/bot5868031897:AAGCr2ZZ8O4NOHEFVcH3xVX4kxm28TjE0LI/getUpdates'.format(token)
    r = requests.get(url)
    x = 0
    while 1 :
        try:
            r.json()["result"][x]
            x+=1
        except IndexError:
            return (r.json()["result"][x-1]["message"]["chat"]["id"]), r.json()["result"][x-1]["message"]["text"], (r.json()["result"][x-1]["message"]["date"])

def sendMessage(text, id):
    requests.get(f"https://api.telegram.org/bot5868031897:AAGCr2ZZ8O4NOHEFVcH3xVX4kxm28TjE0LI/sendMessage?chat_id=-830362976&text=" + text, timeout=3)
    
    
date_list = []
while 1:
    try:
        id, text, date = getUpdate()
        if text == "/sms" and date not in date_list:
            date_list.append(date)
            sendMessage("SMS göndermek istediğiniz numarayı %2B90 olmadan yazınız.", id)
            while True:
                id, text, date = getUpdate()
                if len(text) != 10 and date not in date_list:
                    date_list.append(date)
                    sendMessage("Lütfen 10 haneli telefon numarası giriniz.", id)
                elif text == environ.get('SAHIP') and date not in date_list:
                    date_list.append(date)
                    sendMessage("Bu önemli şahsiyeti rahatsız etmek istemiyorum.\nFarklı telefon numarası yazınız!", id)
                elif len(text) == 10 and date not in date_list:
                    date_list.append(date)
                    telno = text
                    sendMessage("Kaç adet SMS göndermek istiyorsunuz?", id)
                    while 1:
                        id, text, date = getUpdate()
                        if date not in date_list:
                            try:
                                intcheck_adet = int(text)
                                date_list.append(date)
                                sendMessage("Kaç saniye aralıklarla göndermek istiyorsunuz?", id)
                                while 1:
                                    id, text, date = getUpdate()
                                    if date not in date_list:
                                        try:
                                            intcheck_saniye = int(text)
                                            date_list.append(date)
                                            sendMessage(f"{intcheck_adet} adet SMS {intcheck_saniye} saniye aralıklarla gönderiliyor...", id)
                                            sms = SendSms(telno)
                                            while sms.adet < intcheck_adet:
                                                for attribute in dir(SendSms):
                                                    attribute_value = getattr(SendSms, attribute)
                                                    if callable(attribute_value):
                                                        if attribute.startswith('__') == False:
                                                            if sms.adet == intcheck_adet:
                                                                break
                                                            exec("sms."+attribute+"()")
                                                            sleep(intcheck_saniye)
                                            sendMessage(telno+" --> "+str(sms.adet)+" adet SMS gönderildi.", id)
                                            break
                                        except ValueError:
                                            date_list.append(date)
                                            sendMessage("Lütfen sayısal değer giriniz.", id)
                            except ValueError:
                                date_list.append(date)
                                sendMessage("Lütfen sayısal değer giriniz.", id)
                        
        elif text == "/start" and date not in date_list:
            date_list.append(date)
            sendMessage("Merhaba!\nBirilerini rahatsız etmek istiyorsan doğru yere geldin.\n'/sms' komutu ile sms göndermeye başlayabilirsin\nİyi eğlenceler!\n\nKaynak kodu:https://github.com/tingirifistik/Enough\nTwitter: @_tingirifistik\n\n ", id)
        
        elif text != "/sms" and text != "/start" and date not in date_list:
            date_list.append(date)
            sendMessage("Yazdığınızı anlayamadım.", id)
    except:
        pass
