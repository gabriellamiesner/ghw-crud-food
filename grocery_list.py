import sqlite3

class Recipe:
  def __init__(self, name, ingredients, instructions, ) -> None:
    self.name = name
    self.ingredients = ingredients
    self.instructions = instructions

recipe_book = []
recipe_book.append(Recipe("New York Style Bagels", 
                   {'barley malt syrup': 1, "packet active dry yeast": 1, 'bread flour': 1, 'Diamond Crystal kosher salt': 1, 'baking soda':1, 'everything bagel seasoning': 2}, 
                   'https://cooking.nytimes.com/guides/81-how-to-make-bagels'))

groceries = sorted(groceries)

connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()

cursor.execute("create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(groceries)):
  cursor.execute("insert into groceries (name) values (?)",[groceries[i]])
  print("added ", groceries[i])

connection.commit()
connection.close()