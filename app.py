from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import os


app = Flask(__name__)
load_dotenv()
MongoAcess = os.getenv("MONGO_ACESS")
client = MongoClient(MongoAcess)

app.db = client.microblog


entries = []

class GalieanMoons:
  def __init__(self, first, second, third, fourth):
    self.first = first
    self.second = second
    self.third = third
    self.fourth = fourth 



def create_app():
  @app.route("/", methods=["GET", "POST"])
  def index():
    # print([e for e in app.db.entries.find({})])
    if request.method == "POST":
      entry_content = request.form.get("content")
      formatted_data = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
      entries.append((entry_content, formatted_data))
      app.db.entries.insert_one({"content":entry_content, "date":formatted_data})
    
    entries_with_date = [
      (
        entry["content"],
        entry["date"],
        datetime.datetime.strptime(entry["date"], "%Y-%m-%d %H:%M:%S").strftime("%b %d")
      )
      for entry in app.db.entries.find({})
    ]
    return render_template("home.html", entries = entries_with_date)
  return app 

# expressions/
@app.route("/expressions/")
def expressions():
  color = "brown"
  animal_one = "fox"
  animal_two ="dog"

  orange_amount = 10
  apple_amount = 20
  donate_amount = 15

  first_name = "Captain"
  last_name = "Marvel"

  kwargs = {
    "color":color, 
    "aniaml_one":animal_one, 
    "animal_two":animal_two,
    "orange_amount":orange_amount,
    "apple_amount":apple_amount, 
    "donate_amount":donate_amount, 
    "first_name":first_name, 
    "last_name":last_name
  }

  return render_template("expressions.html", **kwargs) 


@app.route('/data_structures/')
def data_structures():
  movies = [
    "Leon the Professional",
    "suspects",
    "mind" 
  ]
  car = {
    "brand":"tesla",
    "model":"roadster",
    "year":2020,
  }
  moons = GalieanMoons('io', "euproa", "Ganymede", "Callisto")
  kwargs = {
    "movies":movies, 
    "car":car,
    "moons":moons
  }
  return render_template("data_structures.html", **kwargs)

@app.route("/company/")
def hello_world_fancy():
  company = "Apple"
  return render_template("conditionals_basics.html", company=company)


@app.route("/user_os/")
def user_os():
  user_os = {
    "Bob":"Windows",
    "Li":"Linux",
    "Andy":"MacOS"
  }
  return render_template("for_loop.html", user_os=user_os)

