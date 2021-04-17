
class Budget:
    def ___init___(self, food, entertainment, healthcare, clothing):
        self.food = food
        self.entertainment= entertainment
        self.healthcare= healthcare
        self.clothing= clothing

food = Budget()
food.deposit = 50000
food.withdraw = 5000
food.balance = food.deposit - food.withdraw 

entertainment = Budget()
entertainment.deposit = 45000
entertainment.withdraw = 30000
entertainment.balance = entertainment.deposit - food.withdraw

healthcare = Budget()
healthcare.deposit = 1000000
healthcare.withdraw = 500000
healthcare.balance = healthcare.deposit - healthcare.withdraw

clothing = Budget
clothing.deposit = 200000
clothing.withdraw = 50000
clothing.balance = clothing.deposit - clothing.withdraw 