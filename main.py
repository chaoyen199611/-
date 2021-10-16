import schedule, sys,time
from time import strftime
from Youbike_Crawler import youbikeCrawler


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
