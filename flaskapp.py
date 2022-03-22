from asyncio import tasks
from email import message
from flask import Flask,jsonify,request
from pandas import concat
app=Flask(__name__)
list=[
    {
        'id':1,
        'name':u'raju',
        'contack':u'1234567890',
        'done':False
    },
    {
        
        'id':2,
        'name':u'rahul',
        'contack':u'1324567890',
        'done':False
    },
]
@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'providedata'
        },400)
    
    contact={
          'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contack':request.json.get('contact',''),
        'done':False

    }
    list.append(contact)
    return jsonify({
            'status':'success',
            'message':'contactadded'
        })

@app.route('/get-data')
def get_task():
    return jsonify({
        'data':list
    })
if(__name__=='__main__'):
    app.run()
