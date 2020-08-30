# -*- encoding: utf-8 -*-
#-*- coding:utf-8 -*-
import requests
import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib import parse
#길드입력받기
def get_Guild() :
    guildWorld = None
    guildName = None
    guildName = input('길드 이름을 입력하세요:')
    guildWorld = input('길드 가 속한 월드를 입력하세요:')
    return guildName,guildWorld
#길드내 유저명 불러오기
def f_input_world(world) :
        worldName = None
        if world == "루나" :
            return("luna")
        elif world == "스카니아" :
            return("scania")
        elif world == "엘리시움" :
            return("elysium")
        elif world == "리부트" :
            return("reboot")
        elif world == "크로아" :
            return("croa")
        elif world == "오로라" :
            return("aurora")
        elif world == "베라" :
            return("bera")
        elif world == "레드" :
            return("red")
        elif world == "유니온" :
            return("union")
        elif world == "제니스" :
            return("zenith")
        elif world == "이노시스" :
            return("enosis")
        elif world == "리부트2" :
            return("reboot2")
        elif world == "아케인" :
            return("arcane")
        elif world == "노바" :
            return("nova")
        else :
            return("지정되지 않은 값")
#길드 멤버 닉네임 불러오기
def get_Username(guildName,guildWorld) :
    word = guildWorld+"/"+guildName
    url_tmp = "www.maple.gg/guild/"+ word 
    url = "http://" + parse.quote(url_tmp)+"/members?sort=level"
    req = requests.get(url)
    html = req.text
    guild_Member = []
    bs = BeautifulSoup(html, 'html.parser')
    tags = bs.find_all('a',{'class':'font-size-14 text-grape-fruit'})
    for tag in tags:
        #print(" ".join(tag.text.split())) 
        member = (tag.text)
        guild_Member.append(member)
    return guild_Member
def get_Admin_Username(guildName,guildWorld) :
    word = guildWorld+"/"+guildName
    url_tmp = "www.maple.gg/guild/"+ word 
    url = "http://" + parse.quote(url_tmp)+"/members?sort=level"
    req = requests.get(url)
    html = req.text
    guild_Member = []
    bs = BeautifulSoup(html, 'html.parser')
    tags = bs.find_all('a',{'class':'font-size-14 text-black'})
    for tag in tags:
        #print(" ".join(tag.text.split())) 
        member = (tag.text)
        guild_Member.append(member)
    return guild_Member
#층수
def get_UserFloor(html) :
    userFloor = []
    err = 'X'
    bs = BeautifulSoup(html, 'html.parser')
    tags = bs.find_all('div',{'class':'user-summary-box-content text-center position-relative'})
    if tags:
        for tag in tags:
            floor = (" ".join(tag.h1.text.split()))
            userFloor.append(floor)
    else :
        userFloor.append(err)
    return userFloor
#레벨
def get_UserLevel(html) :
    userLevel = []
    bs = BeautifulSoup(html, 'html.parser')
    lis = bs.find_all('li',{'class':'user-summary-item'})
    for li in lis:
        if 'Lv' in li.text :
            level = re.findall("\d+",(" ".join(li.text.split())))
            userLevel.append(level)
    return userLevel
#마지막 접속일
def get_UserDate(html) :
    userDate = []
    err = 'X'
    bs = BeautifulSoup(html, 'html.parser')
    spans = bs.find_all('span',{'class':'font-size-12 text-white'})
    if spans :
        for span in spans:
            date = re.findall("\d+",(" ".join(span.text.split())))
            userDate.append(date)
    else :
        userDate.append(err)
    return userDate
#직업
def get_UserJob(html) :
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    userJob = []
    err = 'X'
    bs = BeautifulSoup(html, 'html.parser')
    lis2 = bs.find_all('li',{'class':'user-summary-item'})
    for li2 in lis2:
        job = (li2.text)
            #job = (" ".join(li2.text.split()))
            #print(job)
        result = hangul.sub('', job)
        userJob.append(result.replace("인기도",""))
    userJobs = [x for x in userJob if x]     
    return userJobs

def get_UserInfohtml(userNames) :
    htmls = []
    a = 0
    for name in userNames :
        word = name
        url_tmp = "www.maple.gg/u/" + word
        url = "http://" + parse.quote(url_tmp)
        req = requests.get(url)
        html = req.text
        htmls.append(html)
        a = a+1
        print(int(a/len(userNames)*100),'%')
    return htmls

