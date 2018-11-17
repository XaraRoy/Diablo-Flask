import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template, url_for, request

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///monthyear.sqlite3?check_same_thread=False")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
forum = Base.classes.monthyearcompound
# Create our session (link) from Python to the DB
global session
session = Session(engine)




#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Ajax Resposnse
#################################################
@app.route("/update=<request>")
# request = 7
def slidecloud(request):
	# language = request.args.get('language')
	monthyear = session.query(forum).filter_by(level_0=request).first()
	cloud = f"{request}cloud.jpg"
	pos = monthyear.pos
	neg = monthyear.neg
	date = monthyear.index
	slider = request
	
	return render_template("index.html", pos=pos, neg=neg, cloud=cloud, date=date, slider=slider)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
	pos = 1
	slider = 1
	neg = 1
	cloud = "1cloud.jpg"
	date = "2011-07"
	return render_template("index.html", pos=pos, neg=neg, cloud=cloud, date=date, slider=slider)
 


if __name__ == '__main__':
    app.run(debug=True)
