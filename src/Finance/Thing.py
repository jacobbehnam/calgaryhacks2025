class Thing:
    GROCERY = 0
    INCOME = 1
    RENT = 2
    FOOD = 3
    SAVINGS = 4
    LEISURE = 5
    INVESTMENT = 6
    EMERGENCY_FUND = 7
    TRANSPORTATION = 8
    ESSENTIAL = {GROCERY, RENT, FOOD, SAVINGS, INVESTMENT, EMERGENCY_FUND, TRANSPORTATION}
    OPTIONS = [GROCERY, INCOME, RENT, FOOD, SAVINGS, LEISURE, INVESTMENT, EMERGENCY_FUND, TRANSPORTATION]
    OPTIONS_STR = ["Grocery", "Income", "Rent", "Food", "Savings", "Leisure", "Investment", "Emergency Fund", "Transportation"]
    EXPENSES = {GROCERY, RENT, FOOD, LEISURE, INVESTMENT, TRANSPORTATION}
    def __init__(self, name, amount,type):
        self.name = name
        self.amount = amount
        self.type = type
        
    def getAmount(self):
        return self.amount
    
    def isEssential(self) -> bool:
        return self.type in self.ESSENTIAL
    
    def isExpenses(self) -> bool:
        return self.type in self.EXPENSES    
