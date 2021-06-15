from flask import Flask,render_template,request  
import pandas as pd
import csv
from flask_pymongo import PyMongo



app = Flask(__name__) 
# mongoDB configuration
app.config["MONGO_URI"]="mongodb+srv://1234567890:KayaL28401**@miniproject.frhdr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo =PyMongo(app) 
db=mongo.db
fileData =db.fileData
@app.route('/')  
def upload():  
    return render_template("index.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        csvfile = open(f.filename)
        reader = csv.DictReader( csvfile )
        reader=list(reader)
        header= reader[0]
        for each in reader:
            row={}
            for field in header:
                row[field]=each[field]
            insert =fileData.insert_one(row)
    return render_template("success.html") 
        
    
  
if __name__ == '__main__':  
    app.run(debug = True)  


