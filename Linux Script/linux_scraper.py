from splinter import Browser
from bs4 import BeautifulSoup
from config import user, password, the_assignment
import time

executable_path = {'executable_path': 'Type the path of your chromedriver here'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit("https://bootcampspot.com")
browser.find_by_css("#emailAddress").type(user)
browser.find_by_css("#password").type(password)
browser.find_by_css("button.btn-submit").click()
time.sleep(2)
browser.find_by_css("td.col-md-3:nth-child(3)").click()
browser.find_by_css("span").click()
browser.find_by_xpath(".//a[contains(@href,'gradebook')]").click()
browser.find_option_by_text(the_assignment).first.click()
submissions = browser.find_by_css("a.text-link")

#use files
student_notes = open("student_notes.txt","a")
homework_file = open("homework_files.txt", "a")
for x in range(0, len(submissions)):
    print(x)
    student = ""
    notes = ""
    
    browser.find_by_css("a.text-link")[x].click()
    student = browser.find_by_xpath(".//*[contains(@href,'students/')]")
    student_notes.write(student.text + "\n")
    student_notes.write("--" * 12 + "\n")
    notes = browser.find_by_css("div.col-xs-12>p:nth-child(3)")
    student_notes.write(notes[0].text + "\n\n")
    
    homeworks = browser.find_by_css("div.col-gutter-lr>ul>li>a")
    for hw in homeworks:
        homework_file.write(hw["href"] + "\n")
    #homework_file.write("\n")
    browser.back()
    browser.find_option_by_text(the_assignment).first.click()
student_notes.close()
homework_file.close()
browser.quit()
