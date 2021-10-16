import urllib, json, os, time,requests
import pandas as pd
from time import strftime

class youbikeCrawler:
    def __init__(self):
        print("Initialize youbikeCrawler...")
        # add folder to store csv file
        self.fileDir=os.path.join((os.path.abspath("."))+"\\data_before_preprocessing\\")
        if not os.path.exists(self.fileDir):
            os.makedirs(self.fileDir)
            print("add folder"+self.fileDir+"to store csv file")
        print(self.fileDir)
        # set url of th youbike data
        self.url="http://od-oas.kcg.gov.tw/api/service/Get/b4dd9c40-9027-4125-8666-06bef1756092"
        # set list of data update time
        self.uDate=[]
        self.uTime=[]
        # record crawl times
        self.workTime=1
        self.numData=0
        print("================================")

    def getJson(self):
        response=urllib.request.urlopen(self.url)
        data=json.loads(response.read())
        # get type 'retVal' of the json file
        df=pd.json_normalize(data['data']['retVal'])
        print("Get dataset")
        return df,data

    def getUpdateTime(self,data):
        # get update date(yyyymmdd) and time
        Time=data['data']['updated_at']
        print("Dataset Time:"+str(Time))
        uDate=Time.split()[0].replace("-","")
        uTime=Time.split()[1].replace(":","")
        return uDate,uTime

    def jsonToCsv(self,uDate,uTime,currDF):
        # write csv file to '~\data_before_preprocessing'
        self.fileDir=os.path.join((os.path.abspath("."))+"\\data_before_preprocessing\\")
        year=uDate[:4]
        month=uDate[4:6]
        day=month+uDate[6:]
        print(self.fileDir)
        self.fileDir=os.path.join(self.fileDir,year)
        if not os.path.exists(self.fileDir):
            os.makedirs(self.fileDir)
        self.fileDir=os.path.join(self.fileDir,month)
        if not os.path.exists(self.fileDir):
            os.makedirs(self.fileDir)
        self.fileDir=os.path.join(self.fileDir,day+'/')
        if not os.path.exists(self.fileDir):
            os.makedirs(self.fileDir)
        fileName=uDate+"_"+uTime+".csv"
        currDF.to_csv(self.fileDir+fileName,encoding="utf_8_sig")

    def process(self):
        print("Num of crawl works:"+str(self.workTime))
        self.workTime+=1
        currDF,data=self.getJson()
       # try:
            
       # except:
        #    print("Error in getJson")
         #   return 0
        crawlTime=strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print("Crawl Time: ",crawlTime)
        currUDate,currUTime=self.getUpdateTime(data)

        # current data is the same as we get previously,return
        if(self.workTime>2 and currUDate==self.uDate[-1] and currUTime==self.uTime[-1]):
            mcurr=int(crawlTime[14:16])
            mpre=int(self.uTime[-1][2:4])
            errorTime=mcurr-mpre
            print("!!!! Repeat dataset !!!!")
            print("This dataset is upload "+str(errorTime)+" minutes ago")
            print("================================")
            return 0

        # record the update time of data
        self.uDate.append(currUDate)
        self.uTime.append(currUTime)
        self.jsonToCsv(currUDate,currUTime,currDF)
        print("Write csv done")
        self.numData+=1
        print("Num of data:"+str(self.numData))
        print("================================")
