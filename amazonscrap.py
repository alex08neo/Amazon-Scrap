from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import re
browser=webdriver.Chrome(executable_path="d:/chromedriver.exe")
browser.maximize_window()
browser.get("https://www.amazon.in/")
browser.find_element_by_tag_name("body")
searchbycategory=browser.find_element_by_id('searchDropdownBox')
print("Welcome To Amazon Scrap".center(60,"-"))
print("Categories".center(60))
for i in searchbycategory.find_elements_by_tag_name('option'):
    print(i.text)
s=input("\nEnter the Category : ")
for i in searchbycategory.find_elements_by_tag_name('option'):
    if s.lower() in i.text.lower():
        i.click()
        break
    
sear=input("\nWhat Do You want to Search  :  ").capitalize()    
searchbyname=browser.find_element_by_id('twotabsearchtextbox')
searchbyname.send_keys(sear)
writ="*"*10+"  Category : "+s+" and Search by "+sear+"  "+"*"*10+"\n\n"
open("Amazon.txt","a").write(writ)
a=0
c=''
browser.find_element_by_xpath("//input[contains(@value,'Go')]").click()
txt=browser.find_element_by_id("s-result-count").text
for i in txt.split():
    for j in i.split(","):
        if j.isdigit():
            c=c+j
l=int(c)
print("\n")
print("List Of Searched Elements with Price".center(60))
print("\n")
while (a<=l):
    menulist=browser.find_element_by_id("s-results-list-atf")
    for i in menulist.find_elements_by_tag_name("li"):
        a+=1
        string=''
        try:
            name=i.find_element_by_tag_name("h2").text
            price=i.find_element_by_css_selector("span.a-size-base.a-color-price").text
            print(name,price)
            string=name+"\t"+price+"\n"
            open("Amazon.txt","a").write(string)
        except:
            pass
    try:
        browser.find_element_by_class_name("pagnNext").click()
    except:
        break
    print("\n")
open("Amazon.txt","a").write("\n\n")  
browser.quit()
##fi=open("Amazon.txt","r").read()
##print(fi)
