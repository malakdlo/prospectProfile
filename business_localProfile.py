#! /Users/malaklopez/.pyenv/shims/python

import json, requests, sys, webbrowser, bs4, time, datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

####################################################################################################################################
#  SETUP
####################################################################################################################################
class Clientinfo:
    def __init__(self, **kwargs):
        self.properties = kwargs
        
    def get_properties(self):
        return self.properties
    
    def get_property(self, key):
        return self.properties.get(key, None)
    
    @property
    def businessName(self):
        return self.properties.get("businessName", None)
    
    @businessName.setter
    def businessName(self, g):
        self.properties["businessName"] = g
        
    @businessName.deleter
    def businessName(self):
        del self.properties["businessName"]
    
    
   
    @property
    def jsonUrl(self):
        return self.properties.get("jsonUrl", None)
    
    @jsonUrl.setter
    def jsonUrl(self, g):
        self.properties["jsonUrl"] = g
        
    @jsonUrl.deleter
    def jsonUrl(self):
        del self.properties["jsonUrl"]
        

    def getInfo(self):
        response = requests.get(self.jsonUrl)
        response.raise_for_status()
        jsonData = json.loads(response.text)
        clientData = {"LA Auto Care":jsonData[0], "Script Media":jsonData[1]}
        finalClient = clientData[clientName]
        try: 
            print("Heres the Business Info: ")
            for i in finalClient.items():
                print(i)
        except NoSuchElementException:
            print ("Item not found")
    
    def getName(self):
        response = requests.get(self.jsonUrl)
        response.raise_for_status()
        jsonData = json.loads(response.text)
        print(type(jsonData))
        print("Which client would you like to see?")
        n = 0
        for v in range(len(jsonData)):
            print(str(n) + ": " + str(jsonData[v]["Business Name"]))
            n = n + 1
        clientNumber = input("Enter Number: ")
        bname = jsonData[int(clientNumber)]["Business Name"]
        print(str(bname))
        return bname
    
        
        
    def testPass(self, businessName):
        self.testClient = businessName
        print(str(self.testClient))
    
    
    def getGoogleLinks(self, businessName):
        self.clientSearch = businessName
        print("Now looking for top 5 google search links")
        googleRes = requests.get('http://google.com/search?q=' + str(self.clientSearch))
        googleRes.raise_for_status()
        soup = bs4.BeautifulSoup(googleRes.text, "html.parser")
        linkElems = soup.select('.r a')
        numOpen = min(5, len(linkElems))
        print("The top five google results are: ")
        n = 1
        for i in range(numOpen):
            print(str(n) + ":" + " " + linkElems[i].get('href'))
            n = n + 1
            
            
    def getScreenShot(self, businessName):
        self.clientSearch = businessName
        # Setup Browser
        driver = webdriver.Chrome(executable_path="/Users/malaklopez/.pyenv/versions/venv/lib/python3.5/site-packages/selenium/webdriver/chrome/chromedriver")
        driver.set_window_size(1024, 768)
        driver.get('http://google.com/search?q=' + str(self.clientSearch))
        driver.get_screenshot_as_file(str(self.clientSearch) + ".png")
        
####################################################################################################################################
#  SETUP END
####################################################################################################################################
    
    
def main():
    dataDate = datetime.date.today()
    dateStr = str(dataDate)
    theClient = Clientinfo()
    theClient.jsonUrl = "https://script.google.com/macros/s/AKfycbwLtC5hN8_a4YXoIcdKR4KmYCPUzCvfsS3bP-at_j3X7UAKRffT/exec"
    name = theClient.getName()
    print(" ")
    theClient.getGoogleLinks(name)
    theClient.getScreenShot(name)
if __name__ == "__main__": main()
    
