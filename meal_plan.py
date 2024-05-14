import sqlite3

class Recipe:
  def __init__(self, name, instructions, grocery_items) -> None:
    self.name = name
    self.instructions = instructions
    self.grocery_items = grocery_items


salmon_teriyaki = Recipe("salmon teriyaki", "https://cooking.nytimes.com/recipes/1024206-salmon-teriyaki", "1 teriyaki sauce\n1 salmon")
quinoa_salad = Recipe("quinoa salad", "https://cooking.nytimes.com/recipes/1024829-quinoa-salad", "1 quinoa\n4 bell pepper\n1 olives\nlemon pepper dressing\n3 cucumber")
chicken_burgers = Recipe("smashed avocado chicken burgers", "https://cooking.nytimes.com/recipes/1023132-smashed-avocado-chicken-burgers", "1 ground chicken\n3 avocado\nginger\ngarlic\ncilantro\nscallions")
bagels = Recipe("New York Style Bagels", 'https://cooking.nytimes.com/guides/81-how-to-make-bagels', "barley malt syrup\npacket active dry yeast\nbread flour\nDiamond Crystal kosher salt\nbaking soda\neverything bagel seasoning") 
recipe_book = [salmon_teriyaki, quinoa_salad, chicken_burgers, bagels]

connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()

cursor.execute("drop table if exists recipes")
cursor.execute("create table recipes (name TEXT, instructions TEXT, grocery_items TEXT)")
for i in range(len(recipe_book)):
  cursor.execute("insert into recipes (name, instructions, grocery_items) values (?, ?, ?)",(recipe_book[i].name, recipe_book[i].instructions, recipe_book[i].grocery_items))
  print("added ", recipe_book[i].name)

connection.commit()
connection.close()