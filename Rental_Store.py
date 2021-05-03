# Rental Store has 20 videos, 5 categories(New Release, Drama, Comedy, Romance, Horror)
# New Release is the most expensive, Comedy is the cheapest
# 10 Customers, 3 types(Breezy, Hoarder, Regular)
import random

class Videos:
    def __init__(self, id, category):
        self.v_id = id
        self.v_category = category
        self.price = 0
    def set_price(self):
        # New Release(0): $10 per night, Drama(1): $7 per night, Comedy(2): $3 per night, 
        # Romance(3): $5 per night, Horror(4): $4 per night
        prices = [10, 7, 3, 5, 4]
        self.price = prices[self.v_category]
    def info(self):
        return print(self.v_id, self.v_category, self.price)

class Customers:
    def __init__(self, id, category):
        self.c_id = id
        self.c_type = category
        self.rent_videos = []

class Rental_Store:
    def __init__(self):
        self.videos = []
        # Build videos
        for i in range(20):
            v = Videos(i, random.randint(0, 4)) # 5 categories
            v.set_price()
            v.info()
            self.videos.append(v)
        # Build customers
        for i in range(10):
            c = Customers(i, random.randint(0, 2)) # 3 types

# class Rental:
#     def __init__(self, name, night, category):
#         self.c_name = name
#         self.r_night = night
#         self.v_category = category
#     def set_price(self):
#         return 0

# Testing
store = Rental_Store()
#

# def renting():
#     # Build Rental Store
    
#     # 35 days and 34 nights
#     for i in range(35):


# if __name__ : '__main__':