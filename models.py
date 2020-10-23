import os
from datetime import datetime
from random import choice
from dataclasses import dataclass


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@dataclass
class Meal:
    name: str
    

class Menu:
    meals = []
    
    def load_meals(self):
        filepath = os.path.join(BASE_DIR, "data", "meals.txt")
        with open(filepath, 'r') as f:
            data = f.readlines()
            for meal in data:
                self.meals.append(Meal(meal))

    def generate(self):
        menu = []
        # meals for 7 days
        for number in range(7):
            menu.append([choice(self.meals), choice(self.meals)])
        return menu
        
    def write(self, menu):
        filepath = os.path.join(BASE_DIR, 'menu.txt')
        with open(filepath, 'w') as f:
            f.write(f'{datetime.now().strftime("%c")} \n')
            for meal in menu:
                f.write(f'Lunch: {meal[0].name.rstrip()}, Dinner: {meal[1].name}')
        