from colorama import init, Fore
from colorama import Back
from colorama import Style
import os
import requests
import json
import ipinfo
import time
from urllib.request import urlopen
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
import speedtest

init(autoreset=True)

import os
clear = lambda: os.system('clear')

clear()

access_token = 'Поменяйте Token на свой через сайт https://ipinfo.io/dashboard/token'

def Ip_For_Pc():
    clear()
    public_ip = requests.get('https://api.ipify.org').text
    print(f"Public IP Address: {public_ip}")
    print(Fore.CYAN + "y) Больше инфо")
    print(Fore.CYAN + "Другое) Назад")
    num2 = input(Fore.MAGENTA +">> ")
    if num2 == "y":
        Ip_more_info()
    else:
        clear()
        Help()

def GeoIp_one():
    print(Fore.CYAN + "Ведите Ip")
    Ip = input(Fore.MAGENTA +">> ")
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(Ip)
    clear()
    print(Fore.GREEN + "Загрузка.")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Загрузка..")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Загрузка...")
    time.sleep(0.5)
    clear()
    print(Fore.GREEN + "Город - " + details.city)
    print(Fore.GREEN + "Регион - " + details.region)
    print(Fore.GREEN + "Страна - " + details.country)
    print(Fore.GREEN + "Локация - " + details.loc)
    print(Fore.GREEN + "Org - " + details.org)
    print(Fore.GREEN + "Часовой пояс - " + details.timezone)
    print(Fore.CYAN + "Другое) Назад")
    num3 = input(Fore.MAGENTA +">> ")
    if num3 == "1":
        clear()
        Help()
    else:
        clear()
        Help()

def Ip_more_info():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    clear()
    print(Fore.GREEN + "Загрузка.")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Загрузка..")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Загрузка...")
    time.sleep(0.5)
    clear()
    print(Fore.GREEN + "Ip - " + IP)
    print(Fore.GREEN + "Org - " + org)
    print(Fore.GREEN + "Город - " + city)
    print(Fore.GREEN + "Страна - " + country)
    print(Fore.GREEN + "Регион - " + region)
    print(Fore.CYAN + "Другое) Назад") 
    num3 = input(Fore.MAGENTA +">> ")
    if num3 == "1":
        clear()
        Help()
    else:
        clear()
        Help()

def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

def SpeedTestWifi():
    clear()
    print(Fore.GREEN + "Загрузка.")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Загрузка..")
    down = speedtest.Speedtest(secure=True).download()
    uplo = speedtest.Speedtest(secure=True).upload()
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Загрузка...")
    time.sleep(0.5)
    clear()
    print(Fore.GREEN + "Скорость скачивания - ",humansize(down))
    print(Fore.GREEN + "Скорость загрузки - ",humansize(uplo))
    print(Fore.GREEN + "Другое) Назад")
    num3 = input(Fore.MAGENTA +">> ")
    if num3 == "1":
        clear()
        Help()
    else:
        clear()
        Help()

def ChekNumberOne():
    clear()
    print("Ведите номер примеры: +7 0000000000 или +70000000000")
    number = input(Fore.MAGENTA +">> ")
    clear()
    print(Fore.GREEN + "Загрузка.")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Загрузка..")
    phoneNumber = phonenumbers.parse(number)
    timeZone = timezone.time_zones_for_number(phoneNumber)
    geolocation = geocoder.description_for_number(phoneNumber,"en")
    service = carrier.name_for_number(phoneNumber,"en")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Загрузка...")
    time.sleep(0.5)
    clear()
    print(Fore.GREEN + "Часовой пояс - ",timeZone)
    print(Fore.GREEN + "Локация - ",geolocation)
    print(Fore.GREEN + "Провайдер - ",service)
    print(Fore.GREEN + "Другое) Назад")
    num3 = input(Fore.MAGENTA +">> ")
    if num3 == "1":
        clear()
        Help()
    else:
        clear()
        Help()

def info_fo_site():
    clear()
    print("Ведите домен сайта примеры: google.com или youtube.com")
    number = input(Fore.MAGENTA +">> ")
    response = requests.get("https://" + number)
    if response.status_code == 200:
        print(Fore.GREEN + "Есть подключенние к сайту")
        response1 = requests.get("https://2ip.ru/a/" + number + "/")
        if response1.status_code == 200:
            print(Fore.GREEN + "Датабаза доступна")
            res = response1.text
            clear()
            print(Fore.GREEN + "Загрузка.")
            time.sleep(0.8)
            clear()
            print(Fore.GREEN + "Загрузка..")
            Name = res.splitlines()[1564][20:][:-5]
            Robotstxt = res.splitlines()[1601][28:]
            sitemaps = res.splitlines()[1610][28:][:-28]
            Page404 = res.splitlines()[1617][44:][:-41]
            SSLforwarding = res.splitlines()[1623][44:][:-41]
            WWWforwarding = res.splitlines()[1636][44:][:-41]
            ipsite = res.splitlines()[1648][5:][:-5]
            time.sleep(0.8)
            clear()
            print(Fore.GREEN + "Загрузка...")
            time.sleep(0.5)
            clear()
            print(Fore.GREEN + "Информация о сайте")
            print(Fore.GREEN + "Имя - " + Name)
            if Robotstxt == '                <span class="site_info__error">Отсутствует</span>':
                print(Fore.GREEN + "Robots.txt - Отсутствует")
            else:
                print(Fore.GREEN + "Robots.txt - " + Robotstxt)
            if sitemaps == '                <span class="site_info__error">Отсутствует</span>':
                print(Fore.GREEN + "Sitemap - Отсутствует")
            else:
                print(Fore.GREEN + "Sitemap - " + sitemaps)
            if Page404 == 'Найдена':
                print(Fore.GREEN + "Page404 - Найдена")
            else:
                print(Fore.GREEN + "Page404 - Не найдена")
            if SSLforwarding == 'Найдена':
                print(Fore.GREEN + "SSL forwarding - Найдена")
            else:
                print(Fore.GREEN + "SSL forwarding - Не найдена")
            if WWWforwarding == 'Найдена':
                print(Fore.GREEN + "WWW forwarding - Найдена")
            else:
                print(Fore.GREEN + "WWW forwarding - Не найдена")
            print(Fore.GREEN + "Ip - " + ipsite)
            print(Fore.GREEN + "Другое) Назад")
            num3 = input(Fore.MAGENTA +">> ")
            if num3 == "1":
                clear()
                Help()
            else:
                clear()
                Help()  
        else:
            print(Fore.GREEN + "Датабаза не доступна")
            print(Fore.GREEN + "Другое) Назад")
            num3 = input(Fore.MAGENTA +">> ")
            if num3 == "1":
                clear()
                Help()
            else:
                clear()
                Help()  
    else:
        print(Fore.GREEN + "Нет подключения к сайту")
        print(Fore.GREEN + "Другое) Назад")
        num3 = input(Fore.MAGENTA +">> ")
        if num3 == "1":
            clear()
            Help()
        else:
            clear()
            Help()

def Help():
    print(Fore.CYAN +'███████████████████████████████████████')
    print(Fore.CYAN +'████████ ██████████  ██████████████████')
    print(Fore.CYAN +'███████████████████ █ █████████████████')
    print(Fore.CYAN +'████████ ██████████ █ █████████████████')
    print(Fore.CYAN +'████████ ██████████  ██████████████████')
    print(Fore.CYAN +'████████ ██████████ ███████████████████')
    print(Fore.CYAN +'████████ ██████████ ███████████████████')
    print(Fore.CYAN +'███████████████████████████████████████')
    print(Fore.CYAN +"            Русская версия")
    print(Fore.CYAN +"1) Твой Ip и инфо о нём")
    print(Fore.CYAN +"2) Инфо о Ip (Город,Регион,Страна,Локация,Org,Часовой пояс)")
    print(Fore.CYAN +"3) Скорость интернета")
    print(Fore.CYAN +"4) Инфо о номере (Лок,провайдер,часовой пояс)")
    print(Fore.CYAN +"5) Информация о сайте https")
    print(Fore.CYAN +"6) Помощь")
    print(Fore.CYAN +"7) Выход")
Help()

while(True):
    num1 = input(Fore.MAGENTA +">> ")
    if num1 == "7":
        clear()
        print(Fore.GREEN +"Пока")
        quit()
    elif num1 == "6":
        clear()
        Help()
    elif num1 == "5":
        clear()
        info_fo_site()
    elif num1 == "4":
        clear()
        ChekNumberOne()
    elif num1 == "3":
        clear()
        SpeedTestWifi()
    elif num1 == "2":
        clear()
        GeoIp_one()
    elif num1 == "1":
        Ip_For_Pc()
    else:

        print(Fore.RED +"Нет команды")
