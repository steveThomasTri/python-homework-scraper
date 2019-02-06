from selenium import webdriver
from selenium.webdriver.support.select import Select
import csv
import time
import datetime
import bs4 as BeautifulSoup

from config import user, password, the_assignment

page_link = "https://bootcampspot.com"
browser = webdriver.Chrome(executable_path=r'C:/selenium/chromedriver.exe')
browser.maximize_window()
browser.get(page_link)

input_email = browser.find_element_by_id("emailAddress")
input_email.send_keys(user)
input_password = browser.find_element_by_id("password")
input_password.send_keys(password)

sign_in = browser.find_elements_by_css_selector("button.btn-submit")
sign_in[0].click()

time.sleep(2)
cohort = browser.find_elements_by_css_selector("td.col-md-3:nth-child(3)")
for coho in cohort:
    if (coho.text == "CWCL201901DATA4"):
        coho.click()
        break

time.sleep(2)
cohorts = browser.find_elements_by_css_selector("span")
for coho in cohorts:
    if (coho.text == "CWCL20190122DATA"):
        coho.click()
        break

time.sleep(2)
gradebook = browser.find_element_by_xpath(".//a[contains(@href,'gradebook')]")
gradebook.click()

time.sleep(3)
assignment = Select(browser.find_element_by_id("assignment"))
assignment.select_by_visible_text(the_assignment)

time.sleep(1)
submissions = browser.find_elements_by_css_selector("a.text-link")

student_notes = open("student_notes.txt","a")
homework_file = open("homework_files.txt", "a")

for x in range (0,len(submissions)):
    #get link
    link = browser.find_elements_by_css_selector("a.text-link")
    link[x].click()
    time.sleep(3)
    student = browser.find_element_by_xpath(".//*[contains(@href,'students/')]")
    #print(student.text)
    student_notes.write(student.text + "\n")
    student_notes.write("--" * 12 + "\n")
    notes = browser.find_elements_by_css_selector("div.col-xs-12>p:nth-child(3)")
    #print(notes[0].text)
    student_notes.write(notes[0].text + "\n\n")

    homeworks = browser.find_elements_by_css_selector("div.col-gutter-lr>ul>li>a")
    for hw in homeworks:
        # print(hw.get_attribute("href"))
        homework_file.write(hw.get_attribute("href") + "\n")
    homework_file.write("\n")

    browser.back()
    time.sleep(2)
    assignment = Select(browser.find_element_by_id("assignment"))
    assignment.select_by_visible_text(the_assignment)

student_notes.close()
homework_file.close()
browser.close()