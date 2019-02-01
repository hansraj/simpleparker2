import sqlite3
from datetime import datetime
import pandas as pd
 
def create_con():
    try:
        conn = sqlite3.connect("parker.db")
        cur = conn.cursor()
        return conn, cur
    except Error as e:
        print (e)
    return None
 
def create_tables():
    conn, cur = create_con()
    # create a table
    cur.execute("""CREATE TABLE parkings (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, type text, lat text, lon text, is_active int) """)
    cur.execute("""CREATE TABLE bookings (id INTEGER PRIMARY KEY AUTOINCREMENT, pid int, uid int, charge float, is_active int, create_date text) """)
    cur.execute("""CREATE TABLE users (id int, username text, name text, email_id text, mobile_number text, is_active text) """)
    cur.execute("INSERT INTO users VALUES(1, 'user1', 'Test User 1', 'user1@gmail.com', '9898893820', 'Y')")
    parking_dataset = [
            ('S0', '4W', '0', '0', 0),('S1', '4W', '0', '1', 0),('S2', '4W', '0', '2', 0),('S3', '4W', '0', '3', 0), ('S4', '4W', '0', '4', 0),('S5', '4W', '0', '5', 0), ('S6', '4W', '0', '6', 0),('S7', '4W', '0', '7', 0), ('S8', '4W', '0', '8', 0),('S9', '4W', '0', '9', 0),
            ('S10', '4W', '1', '0', 0),('S11', '4W', '1', '1', 0),('S12', '4W', '1', '2', 0),('S13', '4W', '1', '3', 0), ('S14', '4W', '1', '4', 0),('S15', '4W', '1', '5', 0), ('S16', '4W', '1', '6', 0),('S17', '4W', '1', '7', 0), ('S18', '4W', '1', '8', 0),('S19', '4W', '1', '9', 0),
            ('S20', '4W', '2', '0', 0),('S21', '4W', '2', '1', 0),('S22', '4W', '2', '2', 0),('S23', '4W', '2', '3', 0), ('S24', '4W', '2', '4', 0),('S25', '4W', '2', '5', 0), ('S26', '4W', '2', '6', 0),('S27', '4W', '2', '7', 0), ('S28', '4W', '2', '8', 0),('S29', '4W', '2', '9', 0),
            ('S30', '4W', '3', '0', 0),('S31', '4W', '3', '1', 0),('S32', '4W', '3', '2', 0),('S33', '4W', '3', '3', 0), ('S34', '4W', '3', '4', 0),('S35', '4W', '3', '5', 0), ('S36', '4W', '3', '6', 0),('S37', '4W', '3', '7', 0), ('S38', '4W', '3', '8', 0),('S39', '4W', '3', '9', 0),
            ('S40', '4W', '4', '0', 0),('S41', '4W', '4', '1', 0),('S42', '4W', '4', '2', 0),('S43', '4W', '4', '3', 0), ('S44', '4W', '4', '4', 0),('S45', '4W', '4', '5', 0), ('S46', '4W', '4', '6', 0),('S47', '4W', '4', '7', 0), ('S48', '4W', '4', '8', 0),('S49', '4W', '4', '9', 0),
            ('S50', '4W', '5', '0', 0),('S51', '4W', '5', '1', 0),('S52', '4W', '5', '2', 0),('S53', '4W', '5', '3', 0), ('S54', '4W', '5', '4', 0),('S55', '4W', '5', '5', 0), ('S56', '4W', '5', '6', 0),('S57', '4W', '5', '7', 0), ('S58', '4W', '5', '8', 0),('S59', '4W', '5', '9', 0),
            ('S60', '4W', '6', '0', 0),('S61', '4W', '6', '1', 0),('S62', '4W', '6', '2', 0),('S63', '4W', '6', '3', 0), ('S64', '4W', '6', '4', 0),('S65', '4W', '6', '5', 0), ('S66', '4W', '6', '6', 0),('S67', '4W', '6', '7', 0), ('S68', '4W', '6', '8', 0),('S69', '4W', '6', '9', 0),
            ('S70', '4W', '7', '0', 0),('S71', '4W', '7', '1', 0),('S72', '4W', '7', '2', 0),('S73', '4W', '7', '3', 0), ('S74', '4W', '7', '4', 0),('S75', '4W', '7', '5', 0), ('S76', '4W', '7', '6', 0),('S77', '4W', '7', '7', 0), ('S78', '4W', '7', '8', 0),('S79', '4W', '7', '9', 0),
            ('S80', '4W', '8', '0', 0),('S81', '4W', '8', '1', 0),('S82', '4W', '8', '2', 0),('S83', '4W', '8', '3', 0), ('S84', '4W', '8', '4', 0),('S85', '4W', '8', '5', 0), ('S86', '4W', '8', '6', 0),('S87', '4W', '8', '7', 0), ('S88', '4W', '8', '8', 0),('S89', '4W', '8', '9', 0),
            ('S90', '4W', '9', '0', 0),('S91', '4W', '9', '1', 0),('S92', '4W', '9', '2', 0),('S93', '4W', '9', '3', 0), ('S94', '4W', '9', '4', 0),('S95', '4W', '9', '5', 0), ('S96', '4W', '9', '6', 0),('S97', '4W', '9', '7', 0), ('S98', '4W', '9', '8', 0),('S99', '4W', '9', '9', 0)]
    cur.executemany("INSERT INTO parkings (name, type, lat, lon, is_active) VALUES (?,?,?,?,?)", parking_dataset)
    # save data to database
    conn.commit() 

def insert_record(pid, uid):
    conn, cur = create_con()
    #check if exists..
    sql = "SELECT * FROM bookings where pid = %d and is_active = 1" % (pid)
    cur.execute(sql)
    if (cur.fetchone()):
        return "Slot already booked."
    else:
        sql = "INSERT INTO bookings (pid, uid, charge, is_active, create_date) VALUES (%d, %d, 10.00, 1, '31-Jan-2019')" % (pid, uid)
        cur.execute(sql)
        sql = "UPDATE parkings SET is_active = %d WHERE id = %d" % (uid, pid)
        cur.execute(sql)
        conn.commit()
        return "Booking successful"

def update_record(pid, uid):
    conn, cur = create_con()
    sql = "SELECT * FROM bookings where pid = %d and uid = %d and is_active = 1" % (pid, uid)
    cur.execute(sql)
    if (cur.fetchone()):
        sql = "UPDATE bookings SET is_active = 0 WHERE pid = %d and uid = %d" % (pid, uid)
        cur.execute(sql)
        sql = "UPDATE parkings SET is_active = 0 WHERE id = %d" % (pid)
        cur.execute(sql)
        conn.commit()
        return "Booking Cancelled"
    else:
        return "No booking exists in your name"

def update_parkings(pid, status):
    conn, cur = create_con()
    sql = "UPDATE parkings SET is_active = %d WHERE id = %d" % (status, pid)
    cur.execute(sql)
    conn.commit()
    return 0 
    

def delete_tables(): 
    conn, cur = create_con()
    sql = """ DROP TABLE parkings"""
    cur.execute(sql)
    sql = """ DROP TABLE users"""
    cur.execute(sql)
    sql = """ DROP TABLE bookings"""
    cur.execute(sql)
 
def delete_record(bid):
    conn, cur = create_con()
    sql = "DELETE FROM bookings WHERE id = %d" % (bid)
    cur.execute(sql)
    conn.commit()

def get_records(uid, status):
    conn, cur = create_con()
    sql = "SELECT * FROM bookings where uid = %d and is_active=1" % (uid)
    cur.execute(sql)
    return (cur.fetchall())
 
def get_all_parkings():
    conn, cur = create_con()
    print ("\nListing all the parkings:\n")
    sql = "SELECT lat, lon, is_active FROM parkings"
    cur.execute(sql)
    return (cur.fetchall())


def vanilla():
    delete_tables()
    create_tables()

def parse_get_records():
    print(x)

def list_parkload():
    vanilla()
    insert_record(2,2)
    insert_record(3,2)
    insert_record(4,2)
    m = get_records(2,2)
    print (m)
    p = get_all_parkings()
    #print(p)
    slots = pd.DataFrame()
    for i in p:
        slots.set_value(i[0],i[1],i[2])
    print("Parkings Loaded and ready")
    print(slots)

#vanilla()
#list_parkload()
#parse_get_records()
