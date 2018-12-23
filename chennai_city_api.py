from flask import Flask, request
from flask_restful import Resource,Api
from sqlalchemy import create_engine



db=create_engine('sqlite:///Databases/chennai_city.db')
app=Flask(__name__)
api=Api(app)

class info(Resource):
    def get(self):
        conn = db
        query = conn.execute("select * from city_info") 
        #return {'info': [i[0:] for i in query.fetchall()]} 
        return{'data': [dict(zip(tuple(query.keys()) ,i)) for i in query]}
class city_number(Resource):
    def get(self,city_number):
        conn=db
        query=conn.execute("select * from city_info where si_no="+str(city_number))
        return {'data': [dict(zip(tuple(query.keys()) ,i)) for i in query]}

class  city_name(Resource):
    def get(self,city_name):
        conn=db
        query=conn.execute("select * from city_info where area_name like '%s'" % city_name)
        return {'data': [dict(zip(tuple(query.keys()) ,i)) for i in query]}
api.add_resource(info,'/')
api.add_resource(city_number,'/si_no/<city_number>')
api.add_resource(city_name,'/city_name/<city_name>')


app.run(port='5002')