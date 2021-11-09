import datetime
import mysql.connector



def insert_bikestation_Data(df,dataset_time,worktime):
    cnx=mysql.connector.connect(user="root",database="youbike",password="open0813")
    cursor=cnx.cursor()
    df.drop(columns=["sna","ar","act"],inplace=True)
    df.reset_index(drop=True, inplace=True)
    add_bike_station= ("INSERT INTO bike_station "
               "(station_id,station_total_space, bike_left, free_space, update_time) "
               "VALUES (%s, %s, %s, %s, %s)")

    minus_minutes=datetime.timedelta(minutes=10)
    dataset_time= datetime.datetime.strptime(dataset_time, '%Y-%m-%d %H:%M:%S')
    test_time=dataset_time-minus_minutes

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

        if worktime==1:
            cursor.execute(add_bike_station,data_bike_station)
            cnx.commit()
        else:
            if test_time<update_time :
                cursor.execute(add_bike_station,data_bike_station)
                cnx.commit()    
            else:
                continue 
    cursor.close()
    cnx.close()

def insert_weather_Data(df,time):
    cnx=mysql.connector.connect(user="root",database="youbike",password="open0813")
    cursor=cnx.cursor()
    add_weather= ("INSERT INTO weather"
               "(temp,feels_like, pressure, humid_percentage,wind_speed,clouds,icon,weather_condition,time) "
               "VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)")
    temp=int(df.loc[0]['main.temp'])
    feels=int(df.loc[0]['main.feels_like'])
    pressure=float(df.loc[0]['main.pressure'])
    humid=int(df.loc[0]['main.humidity'])
    wind=float(df.loc[0]['wind.speed'])
    clouds=int(df.loc[0]['clouds.all'])
    icon=str(df.loc[0]['icon'])
    weather=str(df.loc[0]['Weather'])
    data_weather=(temp,feels,pressure,humid,wind,clouds,icon,weather,time)
    cursor.execute(add_weather,data_weather)
    cnx.commit()   
    cursor.close()
    cnx.close()