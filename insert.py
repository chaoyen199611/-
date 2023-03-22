import  mysql.connector
import pandas as pd

def insert():
    cnx=mysql.connector.connect(user="joeyhuang",database="youbike",password="open0813")
    cursor = cnx.cursor()

    df = pd.read_csv('stationinfo.csv')
    add_bike_station=("INSERT INTO stationinfo"
        "(name,area,id,total_space,lat,lng)"
        "VALUES (%s,%s,%s,%s,%s,%s)")

    for i in range(len(df)):
        name=df.loc[i]["name"]
        area=df.loc[i]["area"]
        id=df.loc[i]["id"].item()
        total_space=df.loc[i]["total_space"].item()
        lat=float(df.loc[i]["lat"])
        lng=float(df.loc[i]["lng"])

        data_bike_station=(name,area,id,total_space,lat,lng)

        cursor.execute(add_bike_station,data_bike_station)
        cnx.commit()

    cursor.close()
    cnx.close()

if __name__=="__main__":
    insert()