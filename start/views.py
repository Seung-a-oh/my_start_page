from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
import datetime

from start.models import School, Depart, Memo

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKschool/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"}

def index(request):
    
    time = get_time()
    weather = get_weather()
    get_school_bullet()
    school = School.objects.all()
    get_depart_bullet()
    depart = Depart.objects.all()
    # content = memo()
    content = Memo.objects.all()
    print(content)

    return render(request, 'start/index.html', {
        'times':time, 'weathers':weather, 'schools':school,'departs':depart, 'memos':content})


def create_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def get_time():
    date = datetime.datetime.now()

    time = {
                'time': date
    }

    return time

def get_weather():
    weather_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%97%B0%EC%88%98%EB%8F%99+%EB%82%A0%EC%94%A8"
    weather_soup = create_soup(weather_url)
    weather = weather_soup.find("p", attrs={"class":"summary"}).get_text()
    cur_temp = weather_soup.find("div",attrs={"class":"temperature_text"}).get_text().replace(" 현재 온도","")
    lowest = weather_soup.find("span",attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest = weather_soup.find("span",attrs={"class":"highest"}).get_text().replace("최고기온","")
    rainfall = weather_soup.find("div",attrs={"class":"day_data"}).find_all("span",attrs={"class":"rainfall"})
    rain_am = rainfall[0].get_text()
    rain_pm = rainfall[1].get_text()

    weather = {'cur_temp':cur_temp, 
                'lowest':lowest, 
                'highest':highest, 
                'weather':weather, 
                'rain_am':rain_am, 
                'rain_pm':rain_pm,  
    }

    return weather


# using db
def get_school_bullet():
    url = "https://home.sch.ac.kr/sch/06/010100.jsp"
    school_url = create_soup(url)
    schools = school_url.find_all("td",attrs={"class":"subject"},limit=5)

    school_title = {}
    for index, school in enumerate(schools):
        title = school.find("a").get_text().strip()
        link = school.find("a")["href"]
        # school_title[index+1] = [title, link]
        School.objects.get_or_create(index=index, title=title, link=link)

    # schools = School.objects.all()
    # school_title = {'schools':schools}

    return school_title


# none db ver
# def get_school_bullet():
#     url = "https://home.sch.ac.kr/sch/06/010100.jsp"
#     school_url = create_soup(url)
#     schools = school_url.find_all("td",attrs={"class":"subject"})

#     school_title = {}
#     for index, school in enumerate(schools):
#         title = school.find("a").get_text().strip()
#         link = school.find("a")["href"]
#         school_title[index+1] = [title, link]

#     return school_title


def get_depart_bullet():
    url = "https://home.sch.ac.kr/iot/03/0101.jsp"
    depart_url = create_soup(url)
    departs = depart_url.find_all("td",attrs={"class":"subject"}, limit=5)

    depart_title = {}
    for index, depart in enumerate(departs):
        title = depart.find("a").get_text().strip()
        link = depart.find("a")["href"]
        Depart.objects.get_or_create(index=index, title=title, link=link)

    return depart_title


def memo():
    return 




# def get_calender():
#     url = "https://home.sch.ac.kr/sch/05/010000.jsp"
#     calender_url = create_soup(url)

#     month = datetime.datetime.now().month
#     cur_month = "section month_"+str(month)+" active"
    
#     cals = calender_url.find("div",attrs={"class":cur_month})
#     print(cals)



# def get_quiz():
#     url = "https://cafe.naver.com/soojebi/99590"
#     quiz_url = create_soup(url)
#     quizz = quiz_url.find("a", attrs={"div":"inner_list"}).find("a",attrs={"class":"article"})
#     print("-------------------------------")
#     print(quizz)
#     print("-------------------------------")