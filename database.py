import datetime
import mysql.connector


def insertData(df):
    cnx=mysql.connector.connect(user="root",database="youbike",password="open0813")
    cursor=cnx.cursor()
    df.drop(columns=["sna","ar","act"],inplace=True)
    df.reset_index(drop=True, inplace=True)
    add_bike_station= ("INSERT INTO bike_station "
               "(station_id,station_total_space, bike_left, free_space, update_time) "
               "VALUES (%s, %s, %s, %s, %s)")
    for i in range(len(df)):
        tmp=df.loc[i]["mday"]
        date_time_str=tmp[:4]+"-"+tmp[4:6]+"-"+tmp[6:8]+" "+tmp[8:10]+":"+tmp[10:12]+":"+tmp[12:14]
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        update_time=date_time_obj
        station_id=df.loc[i]["sno"]
        station_total_space=df.loc[i]["tot"]
        bike_left=df.loc[i]["sbi"]
        free_space=df.loc[i]["bemp"]
        data_bike_station=(station_id,station_total_space,bike_left,free_space,update_time)
        cursor.execute(add_bike_station,data_bike_station)
        cnx.commit()
    
    cursor.close()
    cnx.close()