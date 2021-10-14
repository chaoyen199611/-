import urllib, json, os, schedule, sys, requests, time
import pandas as pd
from time import ctime, gmtime, strftime

class youbikeCrawler:
    def __init__(self):
        print("Initialize youbikeCrawler...")
        # add folder to store csv file
        self.fileDir=os.path.join((os.path.abspath("."))+"\\data_before_preprocessing\\")
        if not os.path.exists(self.fileDir):
            os.makedirs(self.fileDir)
            print("add folder"+self.fileDir+"to store csv file")
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
        self.data=json.loads(response.read())
        # get type 'retVal' of the json file
        df=pd.json_normalize(self.data['data']['retVal'])
        print("Get dataset")
        return df

    def getUpdateTime(self):
        # get update date(yyyymmdd) and time
        Time=self.data['data']['updated_at']
        print("Dataset Time:"+str(Time))
        uDate=Time.split()[0].replace("-","")
        uTime=Time.split()[1].replace(":","")
        return uDate,uTime

    def jsonToCsv(self,uDate,uTime):
        # write csv file to '~\data_before_preprocessing'
        fileName=uDate+"_"+uTime+".csv"
        self.currDF.to_csv(self.fileDir+fileName,encoding="utf_8_sig")

    def process(self):
        print("Num of crawl works:"+str(self.workTime))
        self.workTime+=1
        try:
            self.currDF=self.getJson()
        except:
            print("Error in getJson")
            return 0
        crawlTime=strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print("Crawl Time: ",crawlTime)
        currUDate,currUTime=self.getUpdateTime()

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
        self.jsonToCsv(currUDate,currUTime)
        print("Write csv done")
        self.numData+=1
        print("Num of data:"+str(self.numData))
        print("================================")

def main():
    # default period time=10
    schTime=10
    args = sys.argv[1:]

    if len(args)>0:
        if args[0]!="-sch":
            print("ERROR:unknown parameter")
            return
        elif len(args)>1:
            if not args[1].isdigit():
                print("Please input a positive number")
                return
            if int(args[1])==0:
                print("Please input period > 0")
                return
            else:
                schTime=int(args[1])
        
    print("================================")
    print("schedule starts at "+strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("crawler works per "+str(schTime)+" minutes")
    print("================================")

    myCrawler=youbikeCrawler()
    myCrawler.process()
    # schedule the crawler process
    schedule.every(schTime).minutes.do(myCrawler.process)
    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__=='__main__':
    main()