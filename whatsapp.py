from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import urllib.parse
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import os
import argparse
try:
    import autoit
except ModuleNotFoundError:
    pass
driver=None
Link='https://web.whatsapp.com/'
parser = argparse.ArgumentParser(description='PyWhatsapp Guide')
parser.add_argument('--chrome_driver_path', action='store', type=str, default='./chromedriver.exe', help='chromedriver executable path (MAC and Windows path would be different)')
parser.add_argument('--message', action='store', type=str, default='', help='Enter the msg you want to send')
parser.add_argument('--remove_cache', action='store', type=str, default='False', help='Remove Cache | Scan QR again or Not')
args = parser.parse_args()

if args.remove_cache == 'True':
    os.system('rm -rf User_Data/*')
def whatsapp_login():
    global wait, driver, Link
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=./User_Data/Default')
    driver = webdriver.Chrome(options=chrome_options,executable_path=r"C:\Users\rjain2778\hello\chromedriver_win32\chromedriver")
    wait = WebDriverWait(driver, 20)
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB IF DISPLAYED")
    driver.get(Link)
    driver.maximize_window()
    print("QR CODE SCANNED")

def send_message(name,msg,count):
    user_group_xpath = '//span[@title = "{}"]'.format(name)
    for retry in range(3):
        try:
            sleep(3)
            wait.until(EC.presence_of_element_located((By.XPATH, user_group_xpath))).click()
            break
        except Exception:
            print("retry:{} {} not found in your contact list".format(retry,name))
            if retry==2:return
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for index in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    print("Message send successfully.")

def send_attachment(name, file_name):
    user_group_xpath = '//span[@title = "{}"]'.format(name)
    print("in send_attachment method")
    for retry in range(3):
        try:
            sleep(3)
            wait.until(EC.presence_of_element_located((By.XPATH, user_group_xpath))).click()
            break
        except Exception:
            print("retry:{} {} not found in your contact list".format(retry,name))
            if retry==2:return
    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()
    attachment = driver.find_element_by_xpath(
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    attachment.send_keys(file_name)
    sleep(5)
    send = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send-light"]')))
    send.click()
    print("File send successfully.")

def send_message_to_unsavaed_contact(number,msg,count):
    print("In send_message_to_unsavaed_contact method")
    params = {'phone': str(number), 'text': str(msg)}
    end = urllib.parse.urlencode(params)
    final_url = Link + 'send?' + end
    print(final_url)
    driver.get(final_url)
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
    print("Page loaded successfully.")
    for retry in range(3):
        try:
            sleep(5)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button'))).click()
            break
        except Exception as e:
            print("Fail during click on send button.")
            if retry==2:return
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for index in range(count-1):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    print("Message sent successfully.")

def send_attachment(image_path):
    clipButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    clipButton.click()
    time.sleep(1)

    # To send Videos and Images.
    mediaButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
    mediaButton.click()
    time.sleep(3)
    autoit.control_focus("Open","Edit1")
    autoit.control_set_text("Open","Edit1",image_path)
    autoit.control_focus("Open", "Button")
    time.sleep(3)
    whatsapp_send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')
    whatsapp_send_button.click()

def sender():
    global unsaved_contacts
    if len(unsaved_contacts)>0:
        for i in unsaved_contacts:
            link="https://web.whatsapp.com/send?phone={}&text&source&data&app_absent".format(i)
            driver.get(link)
            send_attachment("F:\yercaud\IMG-20190817-WA0004.jpg")
                
if __name__ == "__main__":
    whatsapp_login()
    unsaved_contacts=[917449292765,917070609905]
# Run the loop through the database and call the required function