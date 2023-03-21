import json,urllib.request
import pandas as pd

class crawlerAgent:
    def __init__(self):
        self.url="https://ybjson02.youbike.com.tw:60009/yb2/Kaohsiung/gwjs.json"

    def get(self):
        response=urllib.request.urlopen(self.url)
        data=json.loads(response.read())
        df=pd.json_normalize(data['retVal'])
        df.drop(["scity","scityen","ar","snaen","sareaen","aren","sbi_detail.eyb","sbi_detail.yb2"],axis=1,inplace=True)
        df["sna"].replace("YouBike2.0_","",regex=True,inplace=True)

        df.to_csv('test.csv',index=False,encoding="utf_8_sig")
        station_info=df
        
        station_info.drop(["sbi","mday","bemp","act"],axis=1,inplace=True)
        

        station_info.rename(
            columns={"sna":"name","sarea":"area","sno":"id","tot":"total_space"},
            inplace=True,
        )

        station_info.to_csv('stationinfo.csv',index=False,encoding="utf_8_sig")
        print(station_info)
        

def main():
    agent=crawlerAgent()
    agent.get()


if __name__=='__main__':
    main()