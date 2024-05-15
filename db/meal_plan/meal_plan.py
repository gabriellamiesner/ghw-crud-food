import sqlite3

class Recipe:
  def __init__(self, name, instructions, grocery_items, servings) -> None:
    self.name = name
    self.instructions = instructions
    self.grocery_items = grocery_items
    self.servings = servings


salmon_teriyaki = Recipe("salmon teriyaki", "https://cooking.nytimes.com/recipes/1024206-salmon-teriyaki", "teriyaki sauce\nsalmon", 4)
quinoa_salad = Recipe("quinoa salad", "https://cooking.nytimes.com/recipes/1024829-quinoa-salad", "quinoa\nbell pepper\nolives\nlemon pepper dressing\ncucumber", 5)
chicken_burgers = Recipe("smashed avocado chicken burgers", "https://cooking.nytimes.com/recipes/1023132-smashed-avocado-chicken-burgers", "ground chicken\navocado\nginger\ngarlic\ncilantro\nscallions", 7)
bagels = Recipe("New York Style Bagels", 'https://cooking.nytimes.com/guides/81-how-to-make-bagels', "barley malt syrup\npacket active dry yeast\nbread flour\nDiamond Crystal kosher salt\nbaking soda\neverything bagel seasoning", 6) 
recipe_book = [salmon_teriyaki, quinoa_salad, chicken_burgers, bagels]

# connection = sqlite3.connect("grocery_list.db") this was the mistake; forgot to change the db connection 🤦‍♀️
connection = sqlite3.connect("meal_plan.db")
cursor = connection.cursor()

cursor.execute('drop table if exists recipes')
cursor.execute("create table recipes (name TEXT, instructions TEXT, grocery_items TEXT, servings INT)")
for i in recipe_book:
  cursor.execute("insert into recipes (name, instructions, grocery_items, servings) values (?, ?, ?, ?)", (i.name, i.instructions, i.grocery_items, i.servings))
  print("added ", i.name)

connection.commit()
connection.close()