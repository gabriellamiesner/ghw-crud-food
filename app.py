import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "select_a_COMPLEX_secret_key_please"
app.config["SESSION_COOKIE_NAME"] = 'global_hack_week' 

@app.route("/", methods = ["POST", "GET"])
def index():
    session["all_items"], session["shopping_items"], session["schedule_items"] = get_db()
    return render_template("index.html", all_items = session["all_items"], shopping_items = session["shopping_items"],  schedule_items = session['schedule_items'])

@app.route("/add_items", methods = ["POST"])
def add_items():
    session["shopping_items"].append(request.form["select_items"])
    session.modified = True
    return render_template("index.html", all_items = session["all_items"], shopping_items = session["shopping_items"])

@app.route("/remove_items", methods = ["POST"])
def remove_items():
    checked_boxes = request.form.getlist("check")
    
    for item in checked_boxes: 
        if item in session["shopping_items"]:
            idx = session["shopping_items"].index(item)
            session["shopping_items"].pop(idx)
            
            session.modified = True

    return render_template("index.html", all_items = session["all_items"], shopping_items = session["shopping_items"])

@app.route("/update_item", methods=["POST"])
def update_item():
    pass

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        grocery_list = g._database = sqlite3.connect('db/grocery_list/grocery_list.db')
        cursor = grocery_list.cursor()
        cursor.execute('select name from groceries')
        all_data = cursor.fetchall()
        # all_data = [item for item in g]
        all_data = [str(val[0]) for val in all_data]
        shopping_list = all_data.copy()
        random.shuffle(shopping_list)
        shopping_list = shopping_list[:5]
        grocery_list.close()

        meal_plan = g._database = sqlite3.connect('db/meal_plan/meal_plan.db')
        recipe_cursor = meal_plan.cursor()
        recipe_cursor.execute('select * from recipes')
        recipe_names = recipe_cursor.fetchall()
        print(recipe_names)
        meal_plan.close()
        

        schedule_plan = g._database = sqlite3.connect('db/schedule_plan/schedule_plan.db')
        schedule_cursor = schedule_plan.cursor()
        schedule_cursor.execute('select * from plans')
        schedule_items = schedule_cursor.fetchall()
        schedule_plan.close()

        
        
    return all_data, shopping_list, recipe_names, schedule_items

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()