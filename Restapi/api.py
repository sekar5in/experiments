from flask import Flask
from flask_restful import Api, Resource
from json import dumps
import sqlite3


app = Flask(__name__)
api = Api(app)

# Initiating the Database connection to exisiting sqlite3 database.

#conn = sqlite3.connect('salaries.sqlite')
#c = conn.cursor()

class Departments(Resource):
	
	def get(self):
		conn = sqlite3.connect('salaries.sqlite')
		c = conn.cursor()
		query = c.execute("SELECT col_1,col_2,col_3,col_4 FROM employee_chicago WHERE col_3='POLICE'")
		return {'departments' : [i for i in query.fetchall()]}


class Departments_salary(Resource):
	def get(self):
		conn = sqlite3.connect('salaries.sqlite')
		c = conn.cursor()
		query = c.execute("SELECT col_1,col_3,col_4 FROM employee_chicago")
		return {'departments': [i for i in query.fetchall()]}


api.add_resource(Departments,'/departments')
api.add_resource(Departments_salary, '/salary')

if __name__ == '__main__':
	app.run(debug=True)

