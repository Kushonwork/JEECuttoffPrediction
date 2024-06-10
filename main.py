
from selenium import webdriver
import bs4
import requests
import html5lib
from selenium.webdriver.common.keys import Keys
import time
import csv
driver=webdriver.Chrome(executable_path=r'C:\Users\Aditya Choudhary\Downloads\chromedriver_win32\chromedriver.exe')
url='https://josaa.nic.in/Result/Result/OpeningClosingRankArchieve.aspx'

class user:
    def __init__(self,name,rank_adv,rank_mains):
        self.name=name
        self.rank_adv=rank_adv
        self.rank_mains=rank_mains
    def data(self):
        #rank=self.rank_adv
        driver.get(url)
        years=formfill_element('//a[@class="chosen-single"]','//li[@class="active-result"]')#year
        time.sleep(1)
        
        rounds=formfill_element('//a[@class="chosen-single"]','//li[@class="active-result"]')#rounds
        soups=[]
        #driver.get(url)
        for i in range(len(years)):
            for j in range(len(rounds)):
                driver.get(url)
                driver.implicitly_wait(5)
                formfill_general(i)    
                #years[i].click()
                formfill_general(j) 
                #rounds[j].click()
                formfill_general(4,'Indian Institute of Technology')
                #time.sleep(5)
                formfill_general(0)
                formfill_general(0)
                driver.find_element_by_xpath('//input[@type="submit"]').click()
                time.sleep(1)
                try:
                    #c=scraper(self.name)
                    scraper(self.name)
                except:
                    pass
                #tempsoup=bs4.BeautifulSoup(driver.page_source)
                #print(tempsoup.prettify())

class course:
    def __init__(self,insti,coursename,seattype,gender,orank,crank):
        self.insti=insti
        self.coursename=coursename
        self.seattype=seattype
        self.gender=gender
        self.orank=orank
        self.crank=crank               
def scraper(name):
    tempel=driver.find_elements_by_tag_name('td')
    start=13
    courselist=[]
    handle=open(f'export data {name}','a')
    writer=csv.writer(handle)
    headings=driver.find_elements_by_xpath('//a[@class="chosen-single"]')
    year,round=headings[0].text,headings[1].text
    writer.writerow([headings[0].text,headings[1].text])
    while True:
        tempcourse=course(tempel[start].text,tempel[start+1].text,tempel[start+3].text,tempel[start+4].text,tempel[start+5].text,tempel[start+6].text)
        courselist.append(tempcourse)
        print(tempcourse.insti,tempcourse.coursename,tempcourse.seattype,tempcourse.gender,tempcourse.orank,tempcourse.crank)
        writer.writerow([tempcourse.insti,tempcourse.coursename,tempcourse.seattype,tempcourse.gender,tempcourse.orank,tempcourse.crank,year,round])
        start+=7
        if start==len(tempel)-7:
            handle.close()
            break

    #return courselist        
def formfill_general(index,args=''):
    #driver.get(url)
    #driver.find_element_by_xpath(locator1).click()
    #driver.find_element_by_xpath(locator2).click()
    temp=driver.find_elements_by_xpath('//a[@class="chosen-single"]')
    for x in temp:
        if x.text=='--Select--':
            x.click()
    elements=driver.find_elements_by_xpath('//li[@class="active-result"]')
    if args!='':
        #elements[index].click()
        flag=None
        try:
            for x in elements:
                if x.text==args :
                #for x in temp:
                 #   if x.text=='--Select--':
                  #      x.click()
                    flag=x
                    x.click()
                    break
        except:
            for y in temp:
                if y.text=='--Select--':
                    y.click()
                    time.sleep(2)
                    driver.implicitly_wait(5)
                    flag.click()
    else:
        #for x in elements:
            #if x.text==args :
                #x.click()
        elements[index].click()
    driver.implicitly_wait(5)
    time.sleep(2)
def formfill_element(locator1,locator2):
    #driver.get(url)
    temp=driver.find_elements_by_xpath(locator1)
    for x in temp:
        if x.text=='--Select--':
            x.click()
    elements=driver.find_elements_by_xpath(locator2)
    driver.find_element_by_xpath(locator2).click()
    return elements
#def export(user,courselist):
#    handle=open(f'export data {user}','a')
#    writer=csv.writer(handle)
def data_reader(filename):
    pass


#main
try:
    u=user('xyz',1903,4365)
    u.data()
except Exception as e:
    print(e)



