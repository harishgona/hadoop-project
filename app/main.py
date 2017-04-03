from flask import Flask, jsonify, request, abort, send_file
from flask_restful import Api, Resource
import json, csv
from dateutil.relativedelta import relativedelta 

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)


f=open("daily.csv")
reader=csv.reader(f)
data=list(reader)
head=data[0]
data=data[1:]

@app.route("/")
def main():
    return "hello"

@app.route("/forecast/")
def forecast():
    return send_file('./static/index.html')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response
def options (self):
    return {'Allow' : 'PUT' }, 200, \
    { 'Access-Control-Allow-Origin': '*', \
      'Access-Control-Allow-Methods' : 'PUT,GET' }

class datesAPI(Resource):
    def get(self):
        result = [dict(zip({head[0]}, {data[i][0]}))for i in range(len(data))]
        return jsonify(result)
    def post(self):
        json_data=request.get_json(force=True)
        Date=json_data['DATE']
        Tmax=json_data['TMAX']
        Tmin=json_data['TMIN']
        flag=False
        for i in range(len(data)-1):
            if (Date==data[i][0]):
                flag= True

        if(flag!=True):
            data.append([Date,Tmax,Tmin])
            result=dict(zip({"DATE"},{Date}))
            return result,201
        else:
            return abort(409,'data is already recorded')

    


class part_dateAPI(Resource):
    def get(self,date):
        flag = False
        for d in data:
            if (d[0]==date):
                flag=True
                d[1]=float(d[1])
                d[2]=float(d[2])
                result = dict(zip(head, d))
        if flag==True:
            return jsonify(result)
        else:
            abort(404,'404 error:no record found')
    def delete(self,date):
        for i in data:
            if(i[0]==date):
                data.remove(i)
                return "record deleted"

class forecastAPI(Resource):
    def  get(self, date):
        f=open("daily.csv")
        reader=csv.reader(f)
        data=list(reader)
        head=data[0]
        data=data[1:]
        flag=False
        true_date=date
        while(flag==False):
            for i in range(0,len(data)):
                if(data[i][0]==date):
                    flag=True
                    result=[]
                    for j in range(7):
                        data[i+j][0]=str(int(true_date)+j)
                        data[i+j][1]=float(data[i+j][1])
                        data[i+j][2]=float(data[i+j][2])
                        result1=dict(zip(head, data[i+j]))
                        result.append(result1)
                    return jsonify(result)
         
            date=str((int(date)-10000))  
api.add_resource(datesAPI, '/historical/')
api.add_resource(part_dateAPI, '/historical/<string:date>')
api.add_resource(forecastAPI, '/forecast/<string:date>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
