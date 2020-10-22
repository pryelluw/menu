class Meal


class Menu:
    def __init__(self):
        pass


    def load_meals(self):
        with open('data/meals.toml', 'r') as f:
            meals = toml.loads(f.read())
            return meals
