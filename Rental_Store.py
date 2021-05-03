# Rental Store has 20 videos, 5 categories(New Release, Drama, Comedy, Romance, Horror)
# New Release is the most expensive, Comedy is the cheapest
# 10 Customers, 3 types(Breezy, Hoarder, Regular)
import random
from collections import Counter

# Global variables
video_category = ['New Release', 'Drama', 'Comedy', 'Romance', 'Horror']
customer_category = ['Breezy', 'Hoarder', 'Regular']

class Videos:
    def __init__(self, id, category):
        self.v_id = id
        self.v_category = category
    def Get_price(self):
        # New Release(0): $10 per night, Drama(1): $7 per night, Comedy(2): $3 per night, 
        # Romance(3): $5 per night, Horror(4): $4 per night
        prices = [10, 7, 3, 5, 4]
        return prices[self.v_category]
    def info(self):
        return print(self.v_id, self.v_category, self.price)

class Customers:
    def __init__(self, id, category):
        self.c_id = id # Breezy(0), Hoarder(1), Regular(2)
        self.c_type = category
        self.rent_videos = dict()
    def Check_illegal(self):
        return True if len(self.rent_videos) < 3 else False
    def Rent_video(self):
        v_to_rent, n_to_rent = 0
        v_rent_type = Counter()
        if(self.Check_illegal()): # Customers are allowed to have at most 3 videos rented at any one time
            r_len = len(self.rent_videos)
            if(self.c_type == 0): # Breezy(Rent 1 or 2 videos for 1 or 2 nights)
                v_to_rent = random.randint(1, 3 - r_len)
                n_to_rent = random.randint(1, 2)
            elif(self.c_type == 1): # Hoarder(Always rent 3 videos for 7 nights)
                if(r_len == 0):
                    v_to_rent = 3
                    n_to_rent = 7
            else: # Regular(Rent 1 - 3 videos for 3 - 5 nights)
                v_to_rent = random.randint(1, 3 - r_len)
                n_to_rent = random.randint(3, 5)
            v_type = Counter(random.sample(range(0, 4), v_to_rent)) # Customers choose video category
        return(v_to_rent, n_to_rent, v_rent_type)
    def Checkout(videos, nights):
        sum = 0
        for v in videos:
            sum += (v.Get_price() * nights)
        return sum
    def info(self):
        return print(self.c_id, self.c_type)

class Rental:
    def __init__(self, name, night, videos):
        self.c_name = name
        self.r_night = night
        self.r_videos = videos

class Rental_Store:
    def __init__(self):
        self.videos = dict()
        self.rentals = dict()
        # Build videos
        for i in range(20):
            v = Videos(i, random.randint(0, 4)) # 5 categories
            self.videos[v.v_id] = v.v_category
    def Check_inventory(self):
        return len(self.videos)
    def Customer_rent(self, customers):
        for c in customers:
            v_rent, n_rent, v_type = c.Rent_video() # int, int, counter
            # Check inventory
            if(self.Check_inventory() >= v_rent):
                flag = False
                for k, v in v_type.items():
                   if(Counter(self.videos.values())[k] < v): # Found a category has insufficient inventory
                       flag = True
                if(flag): # There is no amount in some categories for customer
                    continue
                else:
                    # Make rent_videos list
                    rent_list = []
                    rent_videos = dict()
                    for k, v in v_type.items():
                        for i in self.videos.keys():
                            if(self.videos[i] == k):
                                rent_videos.append(i)
                    for i in rent_list:
                        rent_videos[i] = self.videos[i]
                        del self.videos[i]
                    # Build Rental
                    Rental(c.c_id, n_rent, rent_videos)
    def Current_info(self, day):
        print('Day: ', day)
        print('Videos: ')
        if(self.check_inventory()):
            for i in range(5):
                print(video_category[i] + ' has ' + str(Counter(self.videos.values())[i]))
        else: print('There is no inventory in store today !')

def renting():
    # Build Rental Store
    store = Rental_Store()
    # Build customers
    customers = []
    for i in range(10):
        c = Customers(i, random.randint(0, 2))
        customers.append(c)
    # 35 days and 34 nights
    for i in range(35):
        # Customer return videos before opening

        # Rental Store open, and customers come to rent videos
        if(store.Check_inventory()):
            # inventory > 0, customers wil come
            print('TO Do')
        # End of day, show today's current store infomations
        store.current_info(i)

# if __name__ : '__main__':