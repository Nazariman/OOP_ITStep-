'''
Створіть клас Recipe з атрибутами
     name – назва страви
     ingredients – список продуктів
     text – текст рецепту
     time – час приготування
методи:
     __str__(self) – повертає назву страви
     __contains__(self, item) – перевіряє чи є інгредієнт в
    рецепті
     __gt__(self, other) – перевіряє чи є час приготування self
    більшим за other
     display_info(self) – виводить всю інформацію про рецепт
'''

class Recipe():
    def __init__ (self, name, ingredients, text, time):
        self.name = name
        self.ingredients = ingredients
        self.text = text
        self.time = time
        
    def __str__ (self): 
        return self.name
    
    def __contains__ (self, item):
        return item.lower() in (ingredient.lower() for ingredient in self.ingredients)
    
    def __gt__ (self, other): 
        if not isinstance(other, Recipe):
            return NotImplemented
        return self.time > other.time
    
    def display_info(self): 
        print(f"Рецепт: {self.name}")
        print(f"Час приготування: {self.time} хв.")
        print("Інгредієнти:")
        for ingredient in self.ingredients:
            print(f"  - {ingredient}")
        print("\nОпис приготування:")
        print(self.text)
        print("-" * 40)
        