from flask import Flask
from flask import request
from flask import Response 
from flask import render_template
import json
import parker_db as _db
import pandas as pd
app = Flask(__name__)

#Assume a grid of parking slots on the map with indexes representing the co-ordinates(lat, long)
#Open slots are marked by 0, filled slots marked by numbers > 0 (user ids)
slots = pd.DataFrame()
setup_done = 0

def load_parkings():
    global slots
    p = _db.get_all_parkings()
    for i in p:
        slots.set_value(i[0],i[1],i[2])
    print("Parkings Loaded and ready")

def vanilla_setup():
    _db.vanilla()

@app.route("/")
def welcome():
    global setup_done
    if(setup_done == 0):
        setup_done = 1
        vanilla_setup()
    message = '''WELCOME TO PARKER.. Your parking helper -- 
            (1) To list open parkings within a radius:
                e.g:  /list/?lat=2&lon=2&r=2
            (2) To list your total bookings:
                e.g: /mybookings/?user=1
            (3) To book a new parking slot:
                e.g. /book/?pid=1&user=1
            (4) To Cancel booking:
                e.g. /cancel/?pid=3&user=1'''
    return render_template('index.html', message=message) 

@app.route("/list/", methods=['GET'])
def get_open_list():
    load_parkings()
    open_slots = []
    count = 0
    lat = int(request.args.get('lat'))
    lon = int(request.args.get('lon'))
    r = int(request.args.get('r')) 
    #if(lat > 7 or lon > 9 or r > 3):
    #    return "Invalid or out of range parameters. Please try again with correct values"
    for i in range((lat - r), (lat + r)):
        for j in range((lon - r), (lon + r)):
            if(0<=i<=9 and 0<=j<=9):
                if(slots.iloc[i,j]==0):
                    count+=1
                    open_slots.insert(0, ("[lat:%d, lon:%d] " % (i,j)))
    open_slots.insert(0, "TOTAL SLOTS AVAILABLE: [%d]" % count)
    response_json = json.dumps(open_slots)
    return Response(response_json, 'application/json')

@app.route("/mybookings/", methods=['GET'])
def my_bookings():
    user = int(request.args.get('user'))
    mb = _db.get_records(user, 1)
    return Response(json.dumps(mb), 'application/json')


@app.route("/book/", methods=['GET'])
def book():
    pid = int(request.args.get('pid'))
    user = int(request.args.get('user'))
    #check if booking exists
    return (_db.insert_record(pid, user))

@app.route("/cancel/", methods=['GET'])
def cancel_booking():
    pid = int(request.args.get('pid'))
    user = int(request.args.get('user'))
    return(_db.update_record(pid, user))

if __name__ == "__main__":
    app.run()
