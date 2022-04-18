from sqlite3 import Error

import sqlite3


class Database:
    """
    Creates a database to store sensor data
    """
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = self.create_connection()

        self.create_table(
            '''CREATE TABLE sensor_data(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time REAL,
            temp REAL,
            humidity REAL,
            thermister REAL,
            photoresistor REAL
            );'''
        )

        self.create_table(
            '''CREATE TABLE motor_parameters(
            id integer PRIMARY KEY AUTOINCREMENT,
            name TEXT, 
            voltage INTEGER, 
            min_rpm INTEGER,
            max_rpm
            );'''
        )

        self.create_table(
            '''CREATE TABLE motor_data(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            motor_parameter FORIEGN KEY, 
            time REAL,
            position REAL,
            velocity REAL,
            acceleration REAL,
            FOREIGN KEY(motor_parameter) REFERENCES motor_parameters(motor_parameters)
            );'''
        )

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            return sqlite3.connect(self.database_name)
        except Error as e:
            print(e)


    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def add_sensor_data(self, data):
        """
        Insert sensor data into sensor_data table
        """
        sql = ''' INSERT INTO sensor_data(time,temp,humidity,thermister,photoresistor)
                VALUES(?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()
        return cur.lastrowid


    def add_motor_parameters(self, data):
        """
        Create new motor parameter 
        name = "string"
        voltage = int
        min rpm = int
        max rpm = int
        """
        sql = ''' INSERT INTO motor_parameters(name, voltage, min_rpm, max_rpm)
                VALUES(?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()
        return cur.lastrowid


    def add_motor_data(self, data):
        """
        Add new motor data for a parameter 
        name = "string"
        voltage = int
        min rpm = int
        max rpm = int
        """
        sql = ''' INSERT INTO motor_data(motor_parameter, time, position, velocity, acceleration)
                VALUES(?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()
        return cur.lastrowid

    
    def show_motor_id_name(self, motor_id):
        """
        Returns specified motor_parameter id and name
        """
        sql = ('''
            SELECT id,name 
            FROM motor_parameters
            WHERE id = ?
            ''')
        cur = self.conn.cursor()
        cur.execute(sql, motor_id)
        return cur.fetchall()[0]

    def show_all_motor_if_data(self, motor_id):
        """
        Returns all data for motor id
        """
        sql = ('''
            SELECT * 
            FROM motor_data
            WHERE motor_parameter = ?
            ''')
        cur = self.conn.cursor()
        cur.execute(sql, motor_id)
        return cur.fetchall()


    def all_sensor_data(self):
        """
        Returns all data for a given sensor name
        """

        sql = ('''
            SELECT *
            FROM sensor_data
        ''')
        cur = self.conn.cursor()
        cur.execute(sql)
        return cur.fetchall()