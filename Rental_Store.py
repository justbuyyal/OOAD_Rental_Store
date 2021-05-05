# Rental Store has 20 videos, 5 categories(New Release, Drama, Comedy, Romance, Horror)
# New Release is the most expensive, Comedy is the cheapest
# 10 Customers, 3 types(Breezy, Hoarder, Regular)
import random
import time
from collections import Counter

# Get fixed amount of videos and random choice
#random.seed(7414)

# Global variables
video_category = ['New Release', 'Drama', 'Comedy', 'Romance', 'Horror']
customer_category = ['Breezy', 'Hoarder', 'Regular']

class Videos:
    def __init__(self, id, category):
        __prices = [10, 7, 3, 5, 4]
        self.v_id = id
        self.v_category = category
        self.price = __prices[self.v_category]
    def Get_price(self):
        # New Release(0): $10 per night, Drama(1): $7 per night, Comedy(2): $3 per night, 
        # Romance(3): $5 per night, Horror(4): $4 per night
        return self.price
    def info(self):
        return print('Video No.' + str(self.v_id) + ' Category: ' + video_category[self.v_category] + ' at price : ' + str(self.price))

class Customers:
    def __init__(self, id, category):
        self.c_id = id
        self.c_type = category # Breezy(0), Hoarder(1), Regular(2)
        self.rent_videos = []
        self.rentals = []
    def Check_illegal(self):
        pass
    def Rent_video(self, store_videos):
        pass
    def Return_video(self, day):
        return_list = []
        for i in self.rentals:
            if(i.Check_return(day)):
                return_list.append(i)
        if(len(return_list)):
            for i in return_list:
                for j in i.r_videos:
                    if(j in self.rent_videos):
                        del self.rent_videos[self.rent_videos.index(j)]
                if(i in self.rentals):
                    del self.rentals[self.rentals.index(i)]
        return return_list
    def info(self):
        return print(self.c_id, self.c_type)

class Breezy(Customers):
    def __init__(self, id, category):
        super().__init__(id, category)
    def Check_illegal(self):
        return True if len(self.rent_videos) < 3 else False
    def Rent_video(self, store_videos):
        v_to_rent = 0
        n_to_rent = 0
        v_type = Counter()
        if(self.Check_illegal()): # Breezy(Rent 1 or 2 videos for 1 or 2 nights)
            s_type = []
            for i in store_videos:
                s_type.append(i.v_category)
            v_to_rent = random.randint(1, 3 - len(self.rent_videos))
            n_to_rent = random.randint(1, 2)
            if(len(store_videos) >= v_to_rent):
                v_type = Counter(random.choices(s_type, k = v_to_rent)) # Customers choose video category
                return v_to_rent, n_to_rent, v_type
            else: return 0,0, Counter()
        else: return 0, 0, Counter()

class Hoarder(Customers):
    def __init__(self, id, category):
        super().__init__(id, category)
    def Check_illegal(self):
        return True if len(self.rent_videos) == 0 else False
    def Rent_video(self, store_videos):
        v_to_rent = 0
        n_to_rent = 0
        v_type = Counter()
        if(self.Check_illegal()): # Hoarder(Always rent 3 videos for 7 nights)
            s_type = []
            for i in store_videos:
                s_type.append(i.v_category)
            v_to_rent = 3
            n_to_rent = 7
            if(len(store_videos) >= v_to_rent):
                v_type = Counter(random.choices(s_type, k = v_to_rent)) # Customers choose video category
                return v_to_rent, n_to_rent, v_type
            else: return 0,0, Counter()
        else: return 0, 0, Counter()

class Regular(Customers):
    def __init__(self, id, category):
        super().__init__(id, category)
    def Check_illegal(self):
        return True if len(self.rent_videos) < 3 else False
    def Rent_video(self, store_videos):
        v_to_rent = 0
        n_to_rent = 0
        v_type = Counter()
        if(self.Check_illegal()): # Regular(Rent 1 - 3 videos for 3 - 5 nights)
            s_type = []
            for i in store_videos:
                s_type.append(i)
            v_to_rent = random.randint(1, 3 - len(self.rent_videos))
            n_to_rent = random.randint(3, 5)
            if(len(store_videos) >= v_to_rent):
                v_type = Counter(random.choices(s_type, k = v_to_rent)) # Customers choose video category
                return v_to_rent, n_to_rent, v_type
            else: return 0,0, Counter()
        else: return 0, 0, Counter()

class Rental():
    def __init__(self, c_id, c_type, night, videos, day):
        self.c_name = c_id
        self.c_type = c_type
        self.r_night = night
        self.r_videos = videos
        self.r_day = day + night
        self.c_day = day
    def Check_return(self, day):
        return True if day == self.r_day else False
    def info(self):
        print('================================================================')
        print('Customer ' + str(self.c_name) + '(Customer_type: ' + customer_category[self.c_type] + ') ' + ' rent: ')
        for i in self.r_videos:
            i.info()
        print('for ' + str(self.r_night) + ' night at day ' + str(self.c_day))
        total_amount = 0
        for i in self.r_videos:
            total_amount += self.r_night * i.Get_price()
        print('At total amount : $' + str(total_amount))

class Rental_Store:
    def __init__(self):
        self.videos = []
        self.rentals = []
        self.complete_rental = []
        self.total_amount = 0
        # Build videos
        for i in range(20):
            self.videos.append(Videos(i, random.randint(0, 4))) # 5 categories
        print('Initial Inventory: ')
        self.Current_info(0)
    def Check_inventory(self):
        return len(self.videos)
    def Customer_rent(self, customer, v_to_rent, n_to_rent, v_type, day):
        # Check valid
        if(v_to_rent == 0 and n_to_rent == 0):
            return False
        # Check inventory
        if(self.Check_inventory() >= v_to_rent):
            valid_list = [] # Save current valid video_id to rent
            for k, v in v_type.items():
                if(len([x for x in self.videos if x.v_category == k]) >= v): # Store has enough inventory
                    valid_list.extend(random.sample([x for x in self.videos if x.v_category == k], k = v))
                else: return False
            if(len(valid_list) == v_to_rent): # Check all videos that customer rents is available
                # Build Rental for store and customer to trackback
                rent_out = valid_list.copy()
                # Remove rented videos from store
                for i in rent_out:
                    self.total_amount += (i.price * n_to_rent) # Record for Store total amount
                    del self.videos[self.videos.index(i)]
                c_rental = Rental(customer.c_id, customer.c_type, n_to_rent, rent_out, day)
                self.rentals.append(c_rental)
                customer.rentals.append(c_rental)
                customer.rent_videos.extend([x for x in rent_out])
                return True
            else: return False
        else: return False
    def Customer_return(self, rental_list):
        for i in rental_list:
            for j in i.r_videos:
                self.videos.append(j)
            self.complete_rental.append(i)
            del self.rentals[self.rentals.index(i)]
    def Current_info(self, day):
        # show every information per day
        print('================================================================')
        print('Day: ', day)
        print('Videos: ')
        if(self.Check_inventory()):
            for i in range(5):
                print(video_category[i] + ' has ' + str(len([x for x in self.videos if x.v_category == i])) + ' movies')
        else: print('There is no inventory in store today !')
    def info(self):
        # show all information
        print('================================================================')
        print('All Completed Rentals: ')
        for i in self.complete_rental:
            i.info()
        print('================================================================')
        print('Uncompleted Rentals: ')
        for i in self.rentals:
            i.info()
        print('================================================================')
        print('Total amount of money : ' + str(self.total_amount))

def renting():
    # Build Rental Store
    store = Rental_Store()
    # Build customers
    customers = []
    for i in range(10):
        c_type = random.randint(0, 2)
        if(c_type == 0):
            customers.append(Breezy(i, c_type))
        elif(c_type == 1):
            customers.append(Hoarder(i, c_type))
        else: customers.append(Regular(i, c_type))
    # 35 days and 34 nights
    for i in range(35):
        # Customer return videos before opening
        return_temp = []
        for c in customers:
            return_temp.extend(c.Return_video(i + 1))
        store.Customer_return(return_temp)
        # Rental Store open, and customers come to rent videos
        if(store.Check_inventory()):
            # inventory > 0, customers wil come
            # A random number of customers will come
            cus_flag = False
            condition_counter = 0
            while True:
                for j in random.sample(customers, k = random.randint(1, 10)):
                    if(j.Check_illegal()):
                        v, n, t = j.Rent_video(store.videos)
                        if(store.Customer_rent(j, v, n, t, i + 1)):
                            cus_flag = True
                    else:
                        continue
                if(cus_flag):
                    break
        # End of day, show today's current store infomations
        store.Current_info(i + 1)
        time.sleep(1)
    # End of 35th, show every information
    store.info()
    
if __name__ == '__main__':
    renting()