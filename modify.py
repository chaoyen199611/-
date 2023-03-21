import pandas as pd


def main():
    df = pd.read_csv('stationinfo.csv')

    df["id"]=pd.to_numeric(df["id"])
    df["total_space"]=pd.to_numeric(df["total_space"])
    df["lat"]=pd.to_numeric(df["lat"])
    df["lng"]=pd.to_numeric(df["lng"])
    print(df)




if __name__=='__main__':
    main()