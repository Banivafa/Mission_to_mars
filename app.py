from flask import Flask, render_template, redirect
import scrape_mars
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import os


# Create an instance of Flask
#sys.setrecursionlimit(2000)
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
#conn = 'mongodb://localhost:27017'
#client = PyMongo.MongoClient(conn)
#db = client.mars_db
#collection = db.mars_facts

    # Route to render index.html template using data from Mongo
@app.route("/") 
def home():

    # Find one record of data from the mongo database
    mars_data= mongo.db.mars_info.find_one()
    #mars = list(db.mars_facts.find())
    #print(mars_info)
    # Return template and data
    return render_template("index.html", mars_info = mars_data)
    #mars_info.update({}, mars_data, upsert =True)
    


from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_data)
    
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)