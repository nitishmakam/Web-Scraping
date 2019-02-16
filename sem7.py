from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import json
requests.adapters.DEFAULT_RETRIES=5
# df=pd.DataFrame(columns=["USN","UE15CS401","UE15CS402","UE15CS403","Elective 5","Elective 6","UE15CS404"])
subs=["USN","UE15CS401","UE15CS402","UE15CS403","Elective 5","Elective 6","UE15CS404"]
df=pd.DataFrame()
url="https://www.pesuacademy.com/Academy/tr/result/01FB15ECS"
for j in range(1,361):
    s=format(j,'03d')
    # browser.get(url+s)
    # pre = browser.find_element_by_tag_name("pre").text
    lm_json=requests.get(url+s,timeout=(3,5))
    if(lm_json.text):
        data = json.loads(lm_json.text)
        df.at[j,"USN"]=data["usn"]
        l=data["results"]
        for i in range(0,9):
            # df.at[j,subs[i+1]]=l[i]["grade"]
            df.at[j,l[i]["subjectCode"]]=l[i]["grade"]
    print("Fetching data for " + "01FB15ECS" + s)
df.to_csv('results.csv')

