from selenium import webdriver
import csv
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By


import requests


url =   "https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx"



class Data():
    
    def __init__(self,insti,prgrm,quota,stype,gen,Or,Cr) -> None:
        self.insti = insti
        self.prgrm = prgrm
        self.quota = quota
        self.stype = stype
        self.gender = gen
        self.Or = Or
        self.Cr = Cr
driver = webdriver.Chrome()

def Parsing(url):
    driver.get(url=url)
    years = elementFind('//a[@class="chosen-single"]','//li[@class="active-result"]')
    time.sleep(1)
    for year in years:
        year.click()
        # try:

        #     year.click()
        # except:
        #     print("Unable to perform the action")
        
        # # if int(year.text)==type(int):
        # rounds = elementFind('//a[@class="chosen-single"]','//li[@class="active-result"]')
        # for rnd in rounds:
        #     print(year.text,rnd.text)
    # print(year.text)
    # year[1].click()
    # print(year[1].text)
        
def elementFind(locator:str,Locator2:str):
    temp =driver.find_element(By.XPATH,locator)
    # print(temp.text)
    if temp.text == '--Select--':
        temp.click()
    # for x in temp:
    #     if x.text =='--Select--' :
    #         x.click()
    try:
        dropdown = driver.find_elements(By.XPATH,Locator2)
        # for i in dropdown:
        #     print(i.text)
        return dropdown
    except:
        print("Some error occured")
Parsing(url=url)




# response = requests.get(url)

# soup = bs(response.text,'html.parser')
# print(soup)