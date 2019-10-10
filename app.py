from flask import Flask
import time
import psycopg2
from bs4 import BeautifulSoup as bs
import requests
import json

previous_time = time.time() -180

app = Flask(__name__)

table_name='temp1'


def get_datas(cursor):
    
    select_query = "SELECT * FROM "+table_name+";"
    cursor.execute(select_query)
    datas = cursor.fetchall()
    return datas

def update_data(url,id,cursor):
    
    page = requests.get(url)
    page = bs(page.text,'html.parser')
       
    try:
        results=[]
        for data in page.findAll('div',{'class':'user-information__achievements-data'}):
            results.append(data.contents[0])
        badges = results[0]
        points = (results[1][1:-1]).replace(",","")
        trails = results[2][1:-1]
        update_query = "UPDATE "+table_name+" SET badges= "+badges+" ,points="+points+", trails="+trails+" WHERE id ='"+str(id)+"';"
        print(update_query)
        cursor.execute(update_query)
    except Exception:
        print("Error")
        update_data(url,id,cursor)
		
@app.route('/')
def root():
    return '<a href="https://theappcode.herokuapp.com./static/index.html">Click Here, to view Score</a>';


@app.route('/<name>/<roll_number>/<url>')
def temp(name,roll_number,url):
    connection = psycopg2.connect(user = "zankzcqmyuheau",
                                  password = "b3913eb5fdb660bd936979c8092adc0c2bef6b1294caf4b2395d5d387f511407",
                                  host = "ec2-46-137-113-157.eu-west-1.compute.amazonaws.com",
                                  port = "5432",
                                  database = "d5de9d996c3btd")
    cursor = connection.cursor()

    url = "https://trailhead.salesforce.com/en/me/"+str(url);

    page = requests.get(url)
    page = bs(page.text,'html.parser')
    results=[]
    for data in page.findAll('div',{'class':'user-information__achievements-data'}):
        results.append(data.contents[0])
    if len(results) ==0 :
        return {"message":"Private Url"}
    badges=results[0]
    points = results[1][1:-1].replace(",","")
    trails = results[2][1:-1]
    insert_query = "INSERT INTO "+table_name+" (name, roll_number, badges, points, trails,url) VALUES('"+name+"','"+roll_number.lower()+"', "+badges+","+points+","+trails+", '"+url+"') ON CONFLICT (roll_number) DO NOTHING;"
    print(insert_query)
    cursor.execute(insert_query)

    connection.commit()
    connection.close()
    #return {"message":"Error"}
    return {"message":"Success"}

    
@app.route('/update')
def update():
    current_time = time.time()
    global previous_time
    if (current_time - previous_time) <180 :
        return {"message":"Wait an another 3 mins","current_time":current_time,"previous_time":previous_time,"difference":int(current_time - previous_time)}
    previous_time = current_time
    connection = psycopg2.connect(user = "zankzcqmyuheau",
                                  password = "b3913eb5fdb660bd936979c8092adc0c2bef6b1294caf4b2395d5d387f511407",
                                  host = "ec2-46-137-113-157.eu-west-1.compute.amazonaws.com",
                                  port = "5432",
                                  database = "d5de9d996c3btd")
    cursor = connection.cursor()
    datas = get_datas(cursor)
    for i in datas:
        url,id=i[-1],i[0]
        update_data(url,id,cursor)
    connection.commit()
    connection.close()
    return {"message":"Success","current_time":current_time,"previous_time":previous_time,"difference":int(current_time - previous_time)},200
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

