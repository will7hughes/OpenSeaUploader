import tkinter
import subprocess
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
from turtle import width
from PIL import ImageTk, Image
import urllib.request
from urllib import parse
from io import BytesIO
import os
import io
import sys
import pickle
import time
from decimal import *
import webbrowser
# from click import command
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import timedelta  
import dateutil.relativedelta
from datetime import timedelta, date
import locale
import json 
import ssl
import random
import timeit #HKN
import re #HKN
from functools import partial #HKN
from functions.gui import root
from functions.image_path import image_path
from functions.info import info
from functions.log import log
from functions.warn import warn
from functions.debug import debug
from classes.WebImage import WebImage
from functions.gui import json_path
from functions.gui import collection_link_input, description_credit_input
from functions.gui import description_footer_input, start_num_input, end_num_input, price
from functions.gui import file_format, external_link
from classes.InputField import input_save_list

##--START--######################################-----GLOBAL-----#####################################--START--##

ssl._create_default_https_context = ssl._create_unverified_context

# Local Date Format
locale.setlocale(locale.LC_ALL, '')
lastdate = date(date.today().year, 12, 31)
  
main_directory = os.path.join(sys.path[0])

# Header
imageurl = "https://cdn.shopify.com/s/files/1/0610/4868/4682/files/cover_uploader.jpg?v=1662277776"
img = WebImage(imageurl).get()
imagelab = tk.Label(root, image=img)
imagelab.grid(row=0, columnspan=2)
imagelab.bind("<Button-1>", lambda e:supportURL())

is_polygon = BooleanVar()
is_polygon.set(False)

is_listing = BooleanVar()
is_listing.set(True) 

is_numformat = BooleanVar()
is_numformat.set(False) 

is_sensitivecontent = BooleanVar()
is_sensitivecontent.set(False) 

##---END---######################################-----GLOBAL-----#####################################---END---##


##--START--######################################----UTILITY-----#####################################--START--##

def supportURL():
    webbrowser.open_new("https://www.infotrex.net/opensea/support.asp?r=app")

def coffeeURL():
    webbrowser.open_new("https://github.com/infotrex/bulk-upload-to-opensea/#thanks")

def save_duration():
    duration_value.set(value=duration_value.get())
    # log(duration_value.get())

def save_captcha():
    captcha_value.set(value=captcha_value.get())
    #log(captcha_value.get())

def open_chrome_profile():
    subprocess.Popen(
        [
            "start",
            "chrome",
            "--remote-debugging-port=8989",
            "--user-data-dir=" + main_directory + "/chrome_profile",
        ],
        shell=True,
    )

def is_numeric(val):
	if str(val).isdigit():
		return True
	elif str(val).replace('.','',1).isdigit():
		return True
	else:
		return False

def check_exists_by_xpath(driver, xpath):
    try:
        # driver.find_element_by_xpath(xpath)
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def collection_scraper():#HKN
    
    collection_links=[]
    first_top_list=[]
    line_count=0

    project_path = main_directory
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(executable_path=project_path + "/chromedriver.exe",options=options)
    wait = WebDriverWait(driver, 60)
    #driver.get(driver.current_url+"?search[sortAscending]=true&search[sortBy]=CREATED_DATE")# collection link
    log("Wait 55 Seconds")
    #time.sleep(55)
    for sny in range(55):
        log(str(55-sny))
        time.sleep(1)

    #wait = WebDriverWait(driver, 60)
    def wait_xpath(code):
        wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))

    my_divs = WebDriverWait(driver, 120).until(ExpectedConditions.presence_of_all_elements_located((By.XPATH, '//div[@role="gridcell" or @role="card"][contains(@style,"top")]')))

    for my_div in my_divs:
        #log(my_div.value_of_css_property("top"))
        top_list_item =int(my_div.value_of_css_property("top").replace("px", ""))
        if(top_list_item > 0):
            first_top_list.append(top_list_item)
        elif(top_list_item == 0):
            line_count = line_count + 1

    find_min = min(first_top_list)
    control_line = len(set(first_top_list))-1
    Top_value = 0

    next_nft = driver.find_element(By.XPATH, '//div[@role="gridcell"  or @role="card"][contains(@style,"top: '+ str(Top_value) +'px")]')
    driver.execute_script("arguments[0].scrollIntoView(true);",next_nft)
    log("Wait 5 Seconds")
    time.sleep(5)

    #total_items=int(Total_Items.input_field.get()) #HKN
    #collection_count_text = driver.find_element(By.XPATH, '//div[@class="AssetSearchView--results-count"]/p').text
    collection_count_text = driver.find_element(By.XPATH, '//div[@class="AssetSearchView--results collection--results AssetSearchView--results--phoenix"]//p').text
    c_num = ""
    for c in collection_count_text:
        if c.isdigit():
            c_num = c_num + c
    total_items = int(c_num)

    total_line =3
    if int(total_items/line_count) != (total_items/line_count):
        total_line = int(total_items/line_count) +1
    else:
        total_line = total_items/line_count

    for my_line in range(total_line):#total_line or some integer like 20
        #presence_of_all_elements_located
        if my_line !=0 and my_line%50==0:
            for sny in range(60):
                log(str(60-sny))
                time.sleep(1)

        if my_line<(total_line-control_line-1):
            WebDriverWait(driver, 120).until(ExpectedConditions.visibility_of_all_elements_located((By.XPATH, '//div[@role="gridcell" or @role="card"][contains(@style,"top: '+ str(Top_value + find_min * control_line) +'px")][last()='+str(line_count)+']')))
        elif my_line == (total_line-control_line-1):
            log("Wait  30 Seconds")
            time.sleep(30)

        last_string='[last()='+str(line_count)+']'
        if (my_line + 1) == total_line:
            last_string =""
        nftler = WebDriverWait(driver, 120).until(ExpectedConditions.visibility_of_all_elements_located((By.XPATH, '//div[@role="gridcell" or @role="card"][contains(@style,"top: '+ str(Top_value) +'px")]'+ last_string)))
        for my_nft in nftler:
            #for sayi in range(5):
                #WebDriverWait(driver, 120).until(ExpectedConditions.visibility_of_all_elements_located((By.XPATH, '//div[@role="gridcell" or @role="card"][contains(@style,"top: '+ str(Top_value) +'px")]['+str(sayi+1)+']//div[@class="AssetCardFooter--name"][string-length(text()) > 0]' )))
            wait_E = True
            while wait_E:
                try:
                    #nft_Name = my_nft.find_element(By.XPATH, './/div[@class="AssetCardFooter--name"]').text
                    nft_Name = my_nft.find_element(By.XPATH, './/a//img').get_attribute('alt')
                    nft_Link = my_nft.find_element(By.XPATH, './/a').get_attribute('href')
                    log(my_nft.find_element(By.XPATH, './/a').get_attribute('href'))
                    with open(os.path.join(sys.path[0], "Scraper.txt"),  'a') as outputfile:  # Use file to refer to the file object
                        outputfile.write(nft_Name + "," + nft_Link + "\n")
                    wait_E = False
                except:
                    log("Nftnin bir bilgisi bulunamadı tekrar deneniyor")
                    wait_E = True
            
            #time.sleep(0.1)
        log("My Line : " + str(my_line))
        if (my_line + 1) != total_line:
            Top_value = Top_value + find_min
            WebDriverWait(driver, 120).until(ExpectedConditions.presence_of_element_located((By.XPATH, '//div[@role="gridcell" or @role="card"][contains(@style,"top: '+ str(Top_value) +'px")]')))
            next_nft = driver.find_element(By.XPATH, '//div[@role="gridcell" or @role="card"][contains(@style,"top: '+ str(Top_value) +'px")]')
            driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0,60);",next_nft) 
        #time.sleep(2)
        
        #driver.execute_script('element = document.body.querySelector("style[top="'+ str(Top_value) +'px"]"); element.scrollIntoView();')

        #my_script = """myInterval = setInterval(function() {document.documentElement.scrollTop +="""+str(Top_value/4)+""";}, 500);
        #setTimeout(function() {clearInterval(myInterval)}, 2000);
        #"""
        #driver.execute_script(my_script)
        #driver.execute_script('document.documentElement.scrollTop +='+ str(Top_value))
        #time.sleep(10)

def remove_duplicates(liste):
    liste2 = []
    if liste: 
        for item in liste:
            if item not in liste2:
                liste2.append(item)
    else:
        return liste
    return liste2
   
def modify_Scrape_txt():#HKN
    
    def num_sort(test_string):
        return list(map(int, re.findall(r'(?<=#)(.*)(?=,)', test_string)))[0]
    Lines = []
    with open(os.path.join(sys.path[0], "Scraper.txt"),  'r') as scraped_list:  # Use file to refer to the file object
        #scraped_list.seek(0)
        Lines = scraped_list.readlines()
        Lines = remove_duplicates(Lines)
        Lines.sort(key=num_sort)   
        #Lines = remove_duplicates(Lines).sort()
    with open(os.path.join(sys.path[0], "modified_Scraper.txt"),  'a') as outputfile:  # Use file to refer to the file object
        for line in Lines:
            outputfile.write(str(line))    

def form_is_valid():
    collection_link = collection_link_input.input_field.get()
    cl_expected_start = "https://opensea.io/collection/"
    cl_expected_end ="/assets/create"

    cl_start_len = len(cl_expected_start)
    cl_start = collection_link[0:cl_start_len]
    
    cl_end_len = len(cl_expected_end)
    cl_end = collection_link[-cl_end_len:]

    file_expected_end = "/src"
    f_end = json_path.get_end()

    if end_num_input.input_field.get() <= start_num_input.input_field.get():
        warn("Invalid Form", "Invalid Input \n\tEnd number [" + str(end_num_input.input_field.get()) + " ] " + "\nShould be less than \n\tStart number [ " + str(start_num_input.input_field.get()) + " ]")
        return False
    elif cl_start != cl_expected_start:
        warn("Invalid Form", "Invalid Input \n\tCollection Link should Start with https://opensea.io/collection/{Insert your collection name}\n\tThen should end in /assets/create\nExample: https://opensea.io/collection/willow-away/assets/create")
        return False
    elif cl_end != cl_expected_end:
        warn("Invalid Form", "Invalid Input \n\tCollection Link should End with /assets/create\nExample: https://opensea.io/collection/willow-away/assets/create")
        return False
    elif f_end != file_expected_end:
        warn("Invalid Form", "Invalid Input \n\tSave Location should be in a directory ending in /src\nExample: C:Users/Willow/OpenSeaUploader/src")
        return False
    else:
        return True

def save():
    if form_is_valid():
        try:
            input_save_list.insert(0, json_path.get_path())
            collection_link_input.save_inputs(1)
            description_credit_input.save_inputs(2)
            description_footer_input.save_inputs(3)
            start_num_input.save_inputs(4)
            end_num_input.save_inputs(5)
            price.save_inputs(6)
            file_format.save_inputs(7)
            external_link.save_inputs(8)
            #Total_Items.save_inputs(10)
            #Control_Line_Number.save_inputs(11)
            #Items_In_Line.save_inputs(12)

            info("Form Saved")
        except:
            warn("Failed to Save Form", "Check the README.md for form information. Verify form is properly filled out. Check the console for the error.\n")
    else:
        log("Form is not valid. Check the README.md for form information. Verify form is properly filled out.")

##---END---######################################----UTILITY-----#####################################---END---##


##--START--######################################------MAIN------#####################################--START--##

def main_program_loop(prgrm):

    project_path = main_directory
    file_path = json_path.get_path()
    collection_link = collection_link_input.input_field.get() # https://opensea.io/collection/willow-away/assets/create
    loop_description_credit = description_credit_input.input_field.get() # Digital art generated by DALL-E 2 using OpenAI.
    loop_description_footer = description_footer_input.input_field.get() # Willow generated this image in part with GPT-3, OpenAI's large-scale language-generation model. Upon generating draft language, Willow reviewed, edited, and revised the language to their own liking and takes ultimate responsibility for the content of this publication.
    start_num = start_num_input.input_field.get()
    end_num = end_num_input.input_field.get()
    loop_price = price.input_field.get()
    listing_price = loop_price
    loop_file_format = file_format.input_field.get() # png, jpg, jpeg, gif
    loop_external_link = external_link.input_field.get()


    sleeptime = random.uniform(0.8, 1.9) #HKN
    sleeptime_short = random.uniform(0.4, 0.8)
    sleeptime_mini = random.uniform(0.1, 0.2)
    sleeptime_blip = random.uniform(0.05, 0.1)

    def sleeptime():
        time.sleep(random.uniform(0.8, 1.9))

    def sleeptime_short():
        time.sleep(random.uniform(0.4, 0.8))

    def sleeptime_mini():
        time.sleep(random.uniform(0.1, 0.2))

    def sleeptime_blip():
        time.sleep(random.uniform(0.05, 0.1))
    
    Lines = []
    if is_listing.get() and prgrm == "OnlyListing":
        with open(os.path.join(sys.path[0], "modified_Scraper.txt"),  'r') as scraped_list:  # Use file to refer to the file object
            Lines = scraped_list.readlines()
        if len(Lines) < 1:
            messagebox.showwarning("showwarning", "No Collected Data Found")
            return

    if prgrm == "RenameImages":

        images_folder = image_path()
        basepath = os.path.dirname(__file__)

        processed_image_count = 0
        end_index = end_num - start_num
        debug("end_index: " + str(end_index))
        for existing_image_index, existing_filename in enumerate(os.listdir(images_folder)):
            
            debug("format, processed_image_count, existing: " + str(loop_file_format) + ", " + str(processed_image_count) + ", " + str(existing_image_index))

            # Only process images within the Start/End Number
            if processed_image_count < end_index:

                new_image_path = f"{str(start_num)}.{loop_file_format}"
                new_image_path = f"{images_folder}/{new_image_path}"
                existing_image_path = os.path.abspath(os.path.join(basepath, "src", "images", existing_filename))

                # Check if the existing image has an integer value as it's last character
                start_to_last_char = len(loop_file_format)+2
                end_to_last_char = len(loop_file_format)+1
                debug("start_to_last_char, end_to_last_char: " + str(start_to_last_char) + ", " + str(end_to_last_char))
                existing_image_last_char = existing_image_path[-start_to_last_char:-end_to_last_char]
                last_char_is_int = False
                try:
                    int(existing_image_last_char)
                    # Will throw if it fails to cast to int, the following code won't run if it is not able to cast to int
                    last_char_is_int = True
                except ValueError:
                    pass
                
                debug("last_char_is_int, char " + str(last_char_is_int) + ", " + str(existing_image_last_char))
                # Only rename image files that do NOT end in a number (that way we don't rename images already processed)
                if last_char_is_int == False:
                    try:
                        os.rename(existing_image_path, new_image_path)
                        processed_image_count = processed_image_count + 1
                        log("Renamed: " + existing_image_path + "\nTo: " + new_image_path)
                    except FileExistsError:
                        warn("Failed to Rename Images", "[ " + existing_image_path + " ] to [ " + new_image_path + " ] Already Exists.\n\tCheck your Start/End Number.\nYou don't want to overwrite existing work.\n\tOtherwise, delete the existing file and re-run Rename Images")
                        pass
        log("Rename Images Complete\n")
        return

    # Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(executable_path=project_path + "/chromedriver.exe",options=options)
    wait = WebDriverWait(driver, 60)

    # Wait for methods
    def wait_css_selector(code):
        wait.until(
            ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, code))
        )
        
    def wait_css_selectorTest(code):
        wait.until(
            ExpectedConditions.elementToBeClickable((By.CSS_SELECTOR, code))
        )    

    def wait_xpath(code):
        wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))
        
        
    def wait_xpath_clickable(code):
        wait.until(ExpectedConditions.element_to_be_clickable((By.XPATH, code)))
    
    def check_exists_by_tagname(tagname):
        try:
            # driver.find_element_by_tagname(tagname)
            driver.find_element(By.TAG_NAME, tagname)
        except NoSuchElementException:
            return False
        return True
            
    def delay(waiting_time=30):
            driver.implicitly_wait(waiting_time)

    while end_num >= start_num:
        if is_numformat.get():
            start_numformat = f"{ start_num:04}"
        else:
             start_numformat = f"{ start_num:01}"
        #HKN S Only Listing
        listing_item_name = ""
        if is_listing.get() and prgrm == "OnlyListing":#HKN  Only Listing
            splited_line = Lines[(int(start_numformat) - 1)].split(",")
            for splited_part in range(len(splited_line)):
                if len(splited_line) < 3:
                    loop_price = float(price.input_field.get())
                elif len(splited_line) == 3:
                    loop_price = splited_line[2].strip() #if a special price is entered for the selected nft
                
                listing_price = loop_price
            log('Number : ',  start_numformat, "Start Listing NFT : " +  splited_line[0].strip())
            listing_item_name = splited_line[0].strip()
            time.sleep(random.uniform(0.1, 0.5))
            driver.get(splited_line[1].strip())
            if start_num%40==0:
                time.sleep(5)
        #HKN F Only Listing 
        if prgrm =="Full":#HKN
            sleeptime()
            driver.get(collection_link)

            #HKN S
            wait_E = True
            while wait_E:
                try:
                    WebDriverWait(driver, 20).until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Add properties']" )))
                    wait_E = False
                except:
                    log("Refresh")
                    with open(os.path.join(sys.path[0], "Log.txt"),  'a') as outputfile:  # Use file to refer to the file object
                        outputfile.write("Starting Point This Page Needed To Be Refreshed \n")
                    driver.get(collection_link)
                    time.sleep(5)
                    wait_E = True    
            #HKN F

	        #HKN Start
            wait_xpath('//*[@id="name"]')
            
            nft_title = ""

            jsonFile = file_path + "/json/"+ str(start_numformat) + ".json"
            if os.path.isfile(jsonFile) and os.access(jsonFile, os.R_OK):

                # checks if file exists
                jsonData = json.loads(open(file_path + "\\json\\"+ str(start_numformat) + ".json").read())

                log("\n" + str(start_numformat) + " - Creating NFT")
                log("--Name")
                
                name = driver.find_element(By.XPATH, '//*[@id="name"]')
                sleeptime()
                name_i = 1
                kacinci = 0
                start = timeit.default_timer()
                stop = timeit.default_timer()
                yenilendi = False
                while name_i == 1:
                    if yenilendi == True :
                        wait_xpath('//*[@id="name"]')
                        name = driver.find_element(By.XPATH, '//*[@id="name"]')
                        yenilendi = False
                    if len(name.get_attribute("value")) == 0:
                        if kacinci < 10 :
                            kacinci = kacinci + 1
                            if kacinci == 1:
                                start = timeit.default_timer()
                            
                            if "name" in jsonData:
                                wait_xpath('//*[@id="name"]')
                                name = driver.find_element(By.XPATH, '//*[@id="name"]')
                                nft_title = jsonData["name"]
                                name.send_keys(nft_title)
                                log(nft_title)
                            else:
                                log("Name not found in json file")
                                exit()

                            time.sleep(3)
                        else :
                            with open(os.path.join(sys.path[0], "Log.txt"),  'a') as outputfile:  # Use file to refer to the file object
                                outputfile.write("This Page Needed To Be Refreshed \n")
                            yenilendi = True
                            kacinci = 0
                            driver.refresh()
                    else:
                        name_i = 0
                        stop = timeit.default_timer()
                        with open(os.path.join(sys.path[0], "Log.txt"),  'a') as outputfile:  # Use file to refer to the file object
                            outputfile.write("Total Retries : " + str(kacinci) + " :: " +"Total Time : " + str((stop - start)) + "\n")
            
                wait_xpath('//*[@id="media"]')
                imageUpload = driver.find_element(By.XPATH, '//*[@id="media"]')
                imagePath = os.path.abspath(file_path + "\\images\\" + str(start_numformat) + "." + loop_file_format)  # change folder here
                imageUpload.send_keys(imagePath)
                time.sleep(random.uniform(2.1, 4.9))
                #HKN Finish

                ext_link = driver.find_element(By.XPATH, '//*[@id="external_link"]')
                ext_link.send_keys(loop_external_link)
                sleeptime_mini()

                log("--Description")
                if "description" in jsonData:
                    desc = driver.find_element(By.XPATH, '//*[@id="description"]')
                    nft_description = jsonData["description"]
                    desc.send_keys(nft_description)
                    sleeptime_mini()
                    desc.send_keys(Keys.ENTER)
                    desc.send_keys(Keys.ENTER)
                    sleeptime_mini()
                    desc.send_keys(loop_description_credit)
                    sleeptime_mini()
                    desc.send_keys(Keys.ENTER)
                    desc.send_keys(Keys.ENTER)
                    sleeptime_mini()
                    desc.send_keys(loop_description_footer)
                    sleeptime()
                    log(nft_description)
                
                #log(str(jsonMetaData))
                wait_css_selector("button[aria-label='Add properties']")
                properties = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add properties']")
                driver.execute_script("arguments[0].click();", properties)
                sleeptime()

                if "traits" in jsonData:
                    log("--Traits")
                    jsonMetaData = jsonData['traits']

                    for key in jsonMetaData:
                        input1 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[1]/div/div/input')
                        input2 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[2]/div/div/input')
                        trait_type = str(key['trait_type'])
                        trait_value = str(key['value'])
                        input1.send_keys(trait_type)
                        sleeptime_blip()
                        input2.send_keys(trait_value)
                        log(trait_type + ": " + trait_value)
                        addmore_button = driver.find_element(By.XPATH, '//button[text()="Add more"]')
                        driver.execute_script("arguments[0].click();", addmore_button)
                        sleeptime_mini()
                    sleeptime_short()

                    try:
                        save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
                        driver.execute_script("arguments[0].click();", save_button)
                        sleeptime()
                    except:
                        driver.find_element(By.XPATH, '//button[text()="Save"]').click()
                        sleeptime()
                else:
                    log("Traits not found")
                    exit()

                if "levels" in jsonData:
                    log("-Levels")
                    jsonMetaData = jsonData['levels']
                
                    wait_css_selector("button[aria-label='Add levels']")
                    levels = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add levels']")
                    driver.execute_script("arguments[0].click();", levels)
                    sleeptime()
                    wait_xpath('//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[1]/div/div/input')#HKN
                    for key in jsonMetaData:
                        input1 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[1]/div/div/input')
                        input2 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[2]/div/div/input')
                        input3 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[3]/div/div/input')
                        input1.send_keys
                        input1.send_keys(str(key['level_type']))

                        # Set max value 10 for Rank
                        for y in range(4):
                            input3.send_keys(Keys.ARROW_DOWN)
                            # log("ARROW_DOWN")
                            sleeptime_blip()
                        input3.send_keys(0)
                        sleeptime_mini()

                        # Set value
                        value1 = int(key["value"])
                        log("Rank: " + str(value1))
                        for x in range(3, value1):
                            input2.send_keys(Keys.ARROW_UP)
                            # log("ARROW_UP")
                            time.sleep(0.2)
                        sleeptime()

                        #addmore_button = driver.find_element(By.XPATH, '//button[text()="Add more"]')
                        #driver.execute_script("arguments[0].click();", addmore_button)
                    sleeptime()

                    try:
                        save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
                        driver.execute_script("arguments[0].click();", save_button)
                        sleeptime()
                    except:
                        driver.find_element(By.XPATH, '//button[text()="Save"]').click()
                        sleeptime()
                else:
                    log("Levels not found!") 
            
                if "stats" in jsonData:
                    log("-Stats")
                    jsonMetaData = jsonData['stats']
                
                    wait_css_selector("button[aria-label='Add stats']")
                    stats = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add stats']")
                    driver.execute_script("arguments[0].click();", stats)
                    sleeptime()
                    wait_xpath('//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[1]/div/div/input')#HKN
                    for key in jsonMetaData:
                        input1 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[1]/div/div/input')
                        input2 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[2]/div/div/input')
                        input3 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[3]/div/div/input')
                        input1.send_keys(str(key['stat_type']))
                        sleeptime_blip()
                        
                        # set max to 1,000 for Collection
                        max_value = int(key["max_value"])
                        for y in range(4):
                            input3.send_keys(Keys.ARROW_DOWN)
                            # log("ARROW_DOWN")
                            sleeptime_blip()
                        sleeptime()
                        input3.send_keys(0)
                        sleeptime_blip()
                        input3.send_keys(0)
                        sleeptime_blip()
                        input3.send_keys(0)
                        sleeptime_short()

                        value1 = int(key["value"])            
                        log("Collection: " + str(value1))

                        for x in range(3):
                            input2.send_keys(Keys.ARROW_DOWN)
                            # log("ARROW_DOWN")
                            sleeptime_blip()
                        sleeptime()

                        for x in range(value1):
                            input2.send_keys(Keys.ARROW_UP)
                            # log("ARROW_UP")
                            sleeptime_blip()

                        #addmore_button = driver.find_element(By.XPATH, '//button[text()="Add more"]')
                        #driver.execute_script("arguments[0].click();", addmore_button)
                    sleeptime()

                    try:
                        save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
                        driver.execute_script("arguments[0].click();", save_button)
                        sleeptime()
                    except:
                        driver.find_element(By.XPATH, '//button[text()="Save"]').click()
                        sleeptime()
                else:
                    log("Levels not found!") 
                
                if is_listing.get():
                    if "price" in jsonData:
                        listing_price_int = jsonData["price"]
                        if listing_price_int > 2 or listing_price_int < 0.01:
                            log("Warning - Listing price should be between 2 and 0.01. Change your price in the json file or edit the code")
                            is_listing.set(False)
                            listing_price = loop_price #Setting to default, just in case
                        listing_price = str(listing_price_int)
                    else:
                        log("Warning - Cannot list item without a price defined in the json file")
                        is_listing.set(False)
                        listing_price = loop_price #Setting to default, just in case

            # Select Polygon blockchain if applicable
            if is_polygon.get():
                log("Polygon")
            else:
                log("Ethereum")
                try:
                    wait_xpath('//*[@id="chain"]')
                    default_blockchain = driver.find_element(By.ID, "chain").get_attribute("value")
                    blockchain_dropdown = driver.find_element(By.ID, "chain")
                    blockchain_dropdown.click()
                    sleeptime_mini()
                except:
                    log("Failed to click blockchain dropdown")
                    exit()
                
                try:
                    blc_dp = driver.find_element(By.CSS_SELECTOR, "div[id^=tippy-]")
                    eth_button = blc_dp.find_element(By.XPATH, "//span[.='Ethereum']")
                    driver.execute_script("arguments[0].click();", eth_button)
                    sleeptime()
                except:
                    log("Struggled to select Ethereum")
                    try:
                        eth_button = driver.find_element(By.XPATH, "//span[.='Ethereum']")
                        driver.execute_script("arguments[0].click();", eth_button)
                        sleeptime()
                    except:
                        log("Failed to select Ethereum")
                        exit()
            
            # delay()
            create = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div/div[1]/span/button')
            driver.execute_script("arguments[0].click();", create)
            sleeptime()
            
            #HKN S
            wait_E = True
            while wait_E:
                try:
                    #wait_xpath('//h4[text()="Almost done"]')
                    WebDriverWait(driver, 15).until(ExpectedConditions.presence_of_element_located((By.XPATH, '//h4[text()="Almost done"]' )))
                    wait_E = False
                except:
                    log("Click Again")
                    driver.execute_script("arguments[0].click();", create)
                    wait_E = True    
            #HKN F

            main_page = driver.current_window_handle

            if check_exists_by_xpath(driver, '//h4[text()="Almost done"]'):
                log("Solving Captcha. I am not a robot ;)")
                wait_xpath('//h4[text()="Almost done"]')
                captcha_element = driver.find_element(By.XPATH,'//h4[text()="Almost done"]')

                if check_exists_by_tagname('iframe'):
                    # log("have iframe")

                    captcha_solver = captcha_value.get()

                    if captcha_solver == "2captcha": # 2 captcha
                        delay()
                        solved_info = WebDriverWait(driver, 300).until(ExpectedConditions.presence_of_element_located((By.XPATH, "//*[@class='captcha-solver-info']" )))#HKN
                        # solved_status = WebDriverWait(driver, 10).until(ExpectedConditions.presence_of_element_located((By.XPATH, "//*[@class='captcha-solver-info']" ))).get_attribute("innerHTML")
                        # log(str(solved_status))
                        wait_xpath("//div[@class='captcha-solver']")
                        captcha_solver_button = driver.find_element(By.XPATH, "//div[@class='captcha-solver']")
                        driver.execute_script("arguments[0].click();", captcha_solver_button)
                        sleeptime()
                        WebDriverWait(driver, 300).until(ExpectedConditions.presence_of_element_located((By.XPATH, "//*[@data-state='solving']" )))#HKN
                        log("solving")
                        #WebDriverWait(driver, 300).until(ExpectedConditions.presence_of_element_located((By.XPATH, "//*[@data-state='solved']")))#HKN
                        #log("solved")#HKN
                    
                    elif captcha_solver == "buster": # !!! Buster Captcha

                        iframes = driver.find_elements(By.TAG_NAME, "iframe")
                        driver.switch_to.frame(iframes[0])

                        try:
                            checkbox_button = WebDriverWait(driver, 10).until(ExpectedConditions.element_to_be_clickable((By.ID ,"recaptcha-anchor")))
                            checkbox_button.click()
                        except:
                            pass
                
                        driver.switch_to.default_content() 
                        # driver.switch_to.frame(iframes[-1])

                        # click on audio challenge
                        WebDriverWait(driver, 10).until(ExpectedConditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='recaptcha challenge expires in two minutes']")))
                        time.sleep(1)
                
                        try:
                            # capt_btn = WebDriverWait(driver, 50).until(ExpectedConditions.element_to_be_clickable((By.XPATH ,'//*[@id="recaptcha-audio-button"]')))
                            wait_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[4]')
                            capt_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[4]')
                            capt_btn.click()
                            sleeptime()
                        except:
                            # capt_btn = WebDriverWait(driver, 10).until(ExpectedConditions.element_to_be_clickable((By.XPATH ,'//*[@id="solver-button"]')))
                            capt_btn = driver.find_element_by_xpath("//button[@id='solver-button']")
                            driver.execute_script("arguments[0].click();", capt_btn)
                            sleeptime()

                        driver.switch_to.default_content()  
                        sleeptime()

                else:
                    pass

                    
            else:
                log("No Captcha to solve. Phew, that was close ;)")

            try:
                WebDriverWait(driver, 360).until(ExpectedConditions.presence_of_element_located((By.XPATH, '//a[text()="Sell"] | /html/body/div[6]/div/div/div/div[2]/button/i | //div[@class="item--collection-detail"]')))
                time.sleep(4)
            except:
                if "https://opensea.io/assets" in str(driver.current_url):
                    #driver.get(driver.current_url)
                    log("Assets page refreshed")
                    driver.refresh()
                    time.sleep(5)

            #HKN S
            wait_E = True
            while wait_E:
                try:
                    WebDriverWait(driver, 15).until(ExpectedConditions.presence_of_element_located((By.XPATH, '//div[@class="item--collection-detail"]')))
                    wait_E = False
                except:
                    if "https://opensea.io/assets" in str(driver.current_url):
                        #driver.get(driver.current_url)
                        log("Assets page refreshed 222")
                        with open(os.path.join(sys.path[0], "Log.txt"),  'a') as outputfile:  # Use file to refer to the file object
                            outputfile.write("This Page Needed To Be Refreshed for assets page refreshed 222 \n")
                        driver.refresh()
                        time.sleep(5)
                    wait_E = True    
            #HKN F
            WebDriverWait(driver, 360).until(ExpectedConditions.presence_of_element_located((By.XPATH, '//div[@class="item--collection-detail"]')))     
        
            with open(os.path.join(sys.path[0], "URL.txt"),  'a') as outputfile:  # Use file to refer to the file object
                outputfile.write(nft_title + str(start_numformat) + "," + driver.current_url + "\n")
            #HKN Bitiş

        log(str(start_numformat) + " - NFT Created: " +  nft_title + "\n")

        #LISTING START - listing start
        main_page = driver.current_window_handle
        if is_listing.get():
            log(str(start_numformat) + " - Listing NFT: " +  nft_title)
            time.sleep(2)
            try:
                wait_xpath('//a[text()="Sell"]')
                sell = driver.find_element(By.XPATH, '//a[text()="Sell"]')
                driver.execute_script("arguments[0].click();", sell)
                sleeptime()
            except:
                if "https://opensea.io/assets" in str(driver.current_url):
                    driver.get(driver.current_url +"/sell")
                    sleeptime()
                else:
                    return
            
            wait_css_selector("input[placeholder='Amount']")
            amount = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Amount']")
            amount.send_keys(str(listing_price))
            sleeptime()

            log("--Duration")
            #duration
            duration_date = duration_value.get()
            #log(duration_date)
            
            #if duration_date != 30:
            amount.send_keys(Keys.TAB)
            sleeptime()
            
            wait_xpath('//*[@role="dialog"]/div[1]/div[1]/div/input')
            select_durationday = driver.find_element(By.XPATH, '//*[@role="dialog"]/div[1]/div[1]/div/input')
            select_durationday.click()
            if duration_date == 1 : 
                range_button_location = '//span[normalize-space() = "1 day"]'
                log("1 day")
            if duration_date == 3 : 
                range_button_location = '//span[normalize-space() = "3 days"]'
                log("3 days")
            if duration_date == 7 : 
                range_button_location = '//span[normalize-space() = "7 days"]'
                log("7 days")
            if duration_date == 30 : 
                range_button_location = '//span[normalize-space() = "1 month"]'    
                log("1 month")
            if duration_date == 90 : 
                range_button_location = '//span[normalize-space() = "3 months"]' 
                log("3 months")
            if duration_date == 180 : 
                range_button_location = '//span[normalize-space() = "6 months"]'
                log("6 months")

            wait.until(ExpectedConditions.presence_of_element_located(
                (By.XPATH, range_button_location)))
            ethereum_button = driver.find_element(
                By.XPATH, range_button_location)
            ethereum_button.click()
            sleeptime()# dikkat
            select_durationday.send_keys(Keys.ENTER)
            log("Ethereum")
            sleeptime()

            delay()
            wait_css_selector("button[type='submit']")
            listing = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            driver.execute_script("arguments[0].click();", listing)

            #HKN S
            wait_E = True
            while wait_E:
                try:
                    wait_xpath('//div[@role="dialog"]//h4[contains(text(), "Complete your listing")]')#HKN
                    wait_E = False
                except:
                    wait_css_selector("button[type='submit']")
                    listing = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                    driver.execute_script("arguments[0].click();", listing)
                    wait_E = True    
            #HKN F
            
            login_page=""#HKN
            time.sleep(2)#HKN

            for handle in driver.window_handles:
                if handle != main_page:
                    login_page = handle
                    #break
            #HKN S
            wait_E = True
            attempts_n = 1
            while wait_E:
                if login_page !="":
                    driver.switch_to.window(login_page)
                    wait_E = False
                else:
                    time.sleep(2)
                    if len(driver.window_handles) == 2:
                        for handle in driver.window_handles:
                            if handle != main_page:
                                login_page = handle
                    elif attempts_n > 4:
                        try:
                            #WebDriverWait(driver, 3).until(ExpectedConditions.presence_of_element_located((By.XPATH, '//div[@role="dialog"]//h4[contains(text(), "Complete your listing")]')))#HKN
                            wait_css_selector("button[type='submit']")
                            listing = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                            driver.execute_script("arguments[0].click();", listing)
                        except:
                            log("i can't click")
                    attempts_n = attempts_n + 1
                                  
            #HKN F
            
            log("--Sign")
            if is_polygon.get():
                try:
                    driver.find_element(By.XPATH, "//*[@id='app-content']/div/div[2]/div/div[3]/div[1]").click()
                    time.sleep(0.7)
                except: 
                    wait_xpath("//div[@class='signature-request-message__scroll-button']")
                    polygonscrollsign = driver.find_element(By.XPATH, "//div[@class='signature-request-message__scroll-button']")


                    driver.execute_script("arguments[0].click();", polygonscrollsign)
                    time.sleep(0.7)

                try:
                    wait_xpath('//*[@id="app-content"]/div/div[2]/div/div[4]/button[2]')
                    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/button[2]').click()
                    time.sleep(0.7)
                except:
                    wait_xpath('//button[text()="Sign"]')
                    metasign = driver.find_element(By.XPATH, '//button[text()="Sign"]')
                    driver.execute_script("arguments[0].click();", metasign)
                    time.sleep(0.7)
                
            else:
                try:
                    driver.find_element(By.XPATH, "//*[@id='app-content']/div/div[2]/div/div[3]/div[1]").click()
                    time.sleep(0.7)
                except:
                    WebDriverWait(driver, 240).until(ExpectedConditions.presence_of_element_located((By.XPATH, "//div[@class='signature-request-message__scroll-button']")))#HKN
                    wait_xpath("//div[@class='signature-request-message__scroll-button']")
                    scrollsign = driver.find_element(By.XPATH, "//div[@class='signature-request-message__scroll-button']")
                    driver.execute_script("arguments[0].click();", scrollsign)
                    time.sleep(0.7)

                try:
                    wait_xpath('//*[@id="app-content"]/div/div[2]/div/div[4]/button[2]')
                    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/button[2]').click()
                    time.sleep(0.7)
                except:
                    wait_xpath('//button[text()="Sign"]')
                    metasign = driver.find_element(By.XPATH, '//button[text()="Sign"]')
                    driver.execute_script("arguments[0].click();", metasign)
                    time.sleep(0.7)
            with open(os.path.join(sys.path[0], "Log_Listing.txt"),  'a') as outputfile:  # Use file to refer to the file object
                outputfile.write(listing_item_name + "\n")
  
        #change control to main page
        driver.switch_to.window(main_page)
        sleeptime()
        
        log(str(start_numformat) + " - NFT Listed: " +  nft_title + "\n")

        start_num = start_num + 1
        sleeptime()
        sleeptime_short()
    
    driver.get("https://www.opensea.io")
    info("Upload Complete")

##---END---######################################------MAIN------#####################################---END---##  


##--START--######################################------GUI-------#####################################--START--##

# Radio Buttons
duration_value = IntVar()
duration_value.set(value=180)
duration_date = Frame(root, padx=0, pady=1)
duration_date.grid(row=15, column=1, sticky=(N, W, E, S))
tk.Radiobutton(duration_date, text='1 day', variable=duration_value, value=1, anchor="w", command=save_duration, width=6,).grid(row=0, column=1)
tk.Radiobutton(duration_date, text="3 days", variable=duration_value, value=3, anchor="w", command=save_duration, width=6, ).grid(row=0, column=2)
tk.Radiobutton(duration_date, text="7 days", variable=duration_value, value=7, anchor="w", command=save_duration, width=6,).grid(row=0, column=3)
tk.Radiobutton(duration_date, text="30 days", variable=duration_value, value=30, anchor="w", command=save_duration, width=7,).grid(row=0, column=4)
tk.Radiobutton(duration_date, text="90 days", variable=duration_value, value=90, anchor="w",command=save_duration,  width=7,).grid(row=0,  column=5)
tk.Radiobutton(duration_date, text="180 days", variable=duration_value, value=180, anchor="w", command=save_duration, width=7).grid(row=0, column=6)
duration_date.label = Label(root, text="Duration:", anchor="nw", width=20, height=2 )
duration_date.label.grid(row=15, column=0, padx=12, pady=0)

captcha_value = StringVar()
captcha_value.set(value="buster")
captcha_date = Frame(root, padx=0, pady=1)
captcha_date.grid(row=16, column=1, sticky=(N, W, E, S))
tk.Radiobutton(captcha_date, text='2 Captcha', variable=captcha_value, value="2captcha", anchor="w", command=save_captcha, width=8,).grid(row=0, column=1)
tk.Radiobutton(captcha_date, text="Buster", variable=captcha_value, value="buster", anchor="w", command=save_captcha, width=8, ).grid(row=0, column=2)
captcha_date.label = Label(root, text="Captcha:", anchor="nw", width=20, height=2 )
captcha_date.label.grid(row=16, column=0, padx=12, pady=0)

# Checkboxes
isSensitive = tkinter.Checkbutton(root, text='Sensitive Content', var=is_sensitivecontent,   width=49, anchor="w")
isSensitive.grid(row=17, column=1)
isCreate = tkinter.Checkbutton(root, text='Complete Listing', var=is_listing, width=49, anchor="w")
isCreate.grid(row=19, column=1)
isPolygon = tkinter.Checkbutton(root, text='Polygon Blockchain',  var=is_polygon, width=49, anchor="w")
isPolygon.grid(row=20, column=1)

# Buttons
open_browser = tkinter.Button(root, width=50, height=1,  text="Open Chrome Browser", command=open_chrome_profile)
open_browser.grid(row=23, column=0, columnspan=2, pady=2)
button_save = tkinter.Button(root, width=50, height=1,  text="Save This Form", command=save) 
button_save.grid(row=22, column=0, columnspan=2, pady=2)
button_start = tkinter.Button(root, width=44, height=2, bg="#1b5e1f", fg="white", text="Start", command=partial(main_program_loop, "Full"))#command=lambda: main_program_loop("Full")
button_start['font'] = font.Font(size=10, weight='bold')
button_start.grid(row=25, column=0, columnspan=2, pady=2)

button_onlyListing = tkinter.Button(root, width=44, height=2, bg="#2eb5cd", fg="white", text="List Only", command=partial(main_program_loop, "OnlyListing"))
button_onlyListing['font'] = font.Font(size=10, weight='bold')
button_onlyListing.grid(row=29,  column=0, columnspan=2, pady=2)

button_renameImages = tkinter.Button(root, width=44, height=2, bg="#4c8c49", fg="white", text="Rename Images", command=partial(main_program_loop, "RenameImages"))
button_renameImages['font'] = font.Font(size=10, weight='bold')
button_renameImages.grid(row=30,  column=0, columnspan=2, pady=2)

##---END---######################################------GUI-------#####################################---END---##

root.mainloop()
