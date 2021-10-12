import urllib, json
import requests
import pandas as pd
url = "http://od-oas.kcg.gov.tw/api/service/Get/b4dd9c40-9027-4125-8666-06bef1756092"
response=urllib.request.urlopen(url)
data=json.loads(response.read())
df=pd.json_normalize(data['data']['retVal'])
time=data['data']['updated_at']
date=time.split()[0].replace("-","")
filename=date+"_"+time.split()[1].replace(":","")+".csv"
print(date)
df.to_csv(filename,encoding="utf_8_sig")