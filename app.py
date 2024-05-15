import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "select_a_COMPLEX_secret_key_please"
app.config["SESSION_COOKIE_NAME"] = 'global_hack_week' 

@app.route("/", methods = ["POST", "GET"])
def index():
    session["all_items"], session["recipe_names"], session["schedule_items"], session["servings"] = get_db()
    session["num_meals_home"], session["week_servings"], session["week_recipe_book"] = generate_groceries()
    return render_template("index.html", all_items = session["all_items"],  schedule_items = session['schedule_items'], recipe_names = session['recipe_names'], servings = session["servings"], num_meals_home = session["num_meals_home"], week_servings = session["week_servings"], week_recipe_book = session["week_recipe_book"])

@app.route("/add_items", methods = ["POST"])
def add_items():
    session["all_items"].append(request.form["select_items"])
    session.modified = True
    return render_template("index.html", all_items = session["all_items"],  schedule_items = session['schedule_items'], recipe_names = session['recipe_names'])

@app.route("/remove_items", methods = ["POST"])
def remove_items():
    checked_boxes = request.form.getlist("check")
    
    for item in checked_boxes: 
        if item in session["all_items"]:
            idx = session["all_items"].index(item)
            session["all_items"].pop(idx)
            
            session.modified = True

    return render_template("index.html", all_items = session["all_items"],  schedule_items = session['schedule_items'], recipe_names = session['recipe_names'])


@app.route("/update_items", methods=["POST"])
def update_items():
    new_item = request.form["new_item"]
    old_item = request.form["old_item"]
    print(new_item, old_item)
    for item in session["all_items"]: 
        if item == old_item: 
            idx = session["all_items"].index(item)
            session["all_items"][idx] = new_item

            session.modified = True
    print(new_item, old_item)
    return render_template("index.html", all_items = session["all_items"],  schedule_items = session['schedule_items'], recipe_names = session['recipe_names'])

@app.route("/generate_groceries", methods=["POST"])
def generate_groceries():
    num_meals_home = 0 
    for i in session["schedule_items"]: 
        if i[3] == 'at home':
            num_meals_home += 1

    week_recipe_book = []
    week_servings = 0 
    db = sqlite3.connect('db/grocery_list/grocery_list.db')
    cursor = db.cursor()
    cursor.execute('delete from groceries')
    for i in session['recipe_names']: 
        if week_servings < num_meals_home:
            week_recipe_book.append(i[0])
            week_servings += i[3]
            placeholder = i[2].split('\n')
            for i in placeholder:
                cursor.execute('insert or ignore into groceries (name) values (?)', (i,))
        else: 
            break
       
    db.commit()
    db.close()
    
    return num_meals_home, week_servings, week_recipe_book

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        grocery_list = g._database = sqlite3.connect('db/grocery_list/grocery_list.db')
        cursor = grocery_list.cursor()
        cursor.execute('select name from groceries')
        all_data = cursor.fetchall()
        print(all_data)
        all_data = [str(val[0]) for val in all_data]
        print(all_data)
        shopping_list = all_data.copy()
        random.shuffle(shopping_list)
        grocery_list.close()

        meal_plan = g._database = sqlite3.connect('db/meal_plan/meal_plan.db')
        recipe_cursor = meal_plan.cursor()
        recipe_cursor.execute('select * from recipes')
        recipe_names = recipe_cursor.fetchall()
        random.shuffle(recipe_names)
        servings = recipe_names[3]
        meal_plan.close()
        

        schedule_plan = g._database = sqlite3.connect('db/schedule_plan/schedule_plan.db')
        schedule_cursor = schedule_plan.cursor()
        schedule_cursor.execute('select * from plans')
        schedule_items = schedule_cursor.fetchall()
        schedule_plan.close()

        
        
    return all_data, recipe_names, schedule_items, servings

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()