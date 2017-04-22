# Purpose

To simplify the process of auditing and profiling sales prospects. Takes a Google Sheet of client info and creates a PDF with website info, Google Search screenshots, Google Maps industry comparison ++.

# Setup 

1. JSON API that returns client info, such as the Google Apps Script - Sheets executable URL in this script.

2. python 2.7 modules
    - json, requests, sys, webbrowser, bs4, time, datetime
    - selenium

3. Mac Terminal 

# Completed Steps

1. Get top 5 results for a google search of the client and take a screen shot of the result.

# To Do

### Site Performance
---

#### 1. Mobile Optimized - https://www.google.com/webmasters/tools/mobile-friendly/
* New Tab
* Load URL 
* Wait until window is loaded
* Set value of
    * /HTML[1]/BODY[1]/DIV[1]/DIV[3]/DIV[1]/FORM[1]/DIV[1]/INPUT[1]
    * ${website}
* Click 
    * /HTML[1]/BODY[1]/DIV[1]/DIV[3]/DIV[1]/FORM[1]/DIV[1]/DIV[1]/DIV[1]
* Wait until loaded
* Take a screen shot
* Store in client profile PDF folder
    
#### 2. Pagespeed - https://developers.google.com/speed/pagespeed/insights/
* New Tab
* Load URL 
* Wait until window is loaded
* Set value of
    * NAME - url
    * ${website}
* Click 
    * /HTML[1]/BODY[1]/DIV[1]/DIV[2]/DIV[1]/FORM[1]/DIV[1]/DIV[1]/DIV[1]
* Wait until loaded
* Take a screen shot
* Store in client profile PDF folder

### SEO 
---

#### 1. Maps Search - https://www.google.com/maps/search/ 
* New Tab
* Load URL 
* Wait until window is loaded
* Set value of
    * /HTML[1]/BODY[1]/JSL[1]/DIV[3]/DIV[8]/DIV[3]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/FORM[1]/DIV[1]/DIV[3]/DIV[1]/INPUT[1]
    * ${industry1} in ${city}, CA
* Click 
    * /HTML[1]/BODY[1]/JSL[1]/DIV[3]/DIV[8]/DIV[3]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/BUTTON[1]
* Wait until loaded
* Take a screen shot
* Store in client profile PDF folder

#### 2. Google Industry Comparison - Same as client search 
* Fill field
    * ID - tsf
* Click button
    * Name - btnK




# Optional

### 1. Set values from Yelp
* Client Name - /HTML[1]/BODY[1]/DIV[2]/DIV[2]/DIV[1]/DIV[1]/DIV[1]/DIV[3]/DIV[1]/DIV[1]/H1[1]
* Industry - /HTML[1]/BODY[1]/DIV[2]/DIV[2]/DIV[1]/DIV[1]/DIV[1]/DIV[3]/DIV[1]/DIV[2]/DIV[2]/SPAN[1]/A[1]
* Address - /HTML[1]/BODY[1]/DIV[2]/DIV[2]/DIV[1]/DIV[1]/DIV[1]/DIV[4]/DIV[1]/DIV[1]/DIV[2]/UL[1]/LI[1]/DIV[1]/STRONG[1]/ADDRESS[1]
* City - /HTML[1]/BODY[1]/DIV[2]/DIV[2]/DIV[1]/DIV[1]/DIV[1]/DIV[4]/DIV[1]/DIV[1]/DIV[2]/UL[1]/LI[1]/DIV[1]/SPAN[1]
* Phone - /HTML[1]/BODY[1]/DIV[2]/DIV[2]/DIV[1]/DIV[1]/DIV[1]/DIV[4]/DIV[1]/DIV[1]/DIV[2]/UL[1]/LI[3]/SPAN[3]
