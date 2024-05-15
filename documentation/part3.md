## part 2 recap 
- finished tutorial 
- create sql schemas for meal_plan + schedule_plan 
- successfully connected schedule plan data to flask app 
- almost able to connect meal_plan to flask app (errors pending)
    - fixed the errors by actually calling the right db, deleting all the db files, allowing sqlite3 to regenerate everything

## part 3
to do: 
- create update function + route for groceries ✅ 
- add CRUD operations for our schedule + meal plans 
- connect logic to return grocery list based off schedule + meal plan ✅ 
    - add a data variable in our meal_plan schema that shows us how many servings a recipe makes ✅ 
    - find how many meals we need to cook/are eating [at home] (assume that we are only cooking for 1 person) ✅ 
    - figure out how many recipes we need to be cooking  ✅ 
    - once we have selected our recipes, combine all the cooking_ingredients into a list ✅ 
    - push that list to our grocery_list ✅ 
- add web styling via css templating 
    - drop down grouping for calendar/schedule 
    - color differences for not at home v at home 
    

## future stretches 
- deploy to heroku 
- creating collections of different meal plans (high protein/gluten free/vegetarian/halal/kosher)
- integrating google calendar/calendar of your choice 