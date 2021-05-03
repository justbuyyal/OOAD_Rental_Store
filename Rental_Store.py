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
        __prices = [10, 7, 3, 5, 4]
        self.v_id = id
        self.v_category = category
        self.price = prices[self.v_category]
    def Get_price(self):
        # New Release(0): $10 per night, Drama(1): $7 per night, Comedy(2): $3 per night, 
        # Romance(3): $5 per night, Horror(4): $4 per night
        return self.price
    def info(self):
        return print('Video No.' + str(self.v_id) + ' Category: ' + video_category[self.v_category] + ' at price : ' + str(self.price))

class Customers:
    def __init__(self, id, category):
        self.c_id = id # Breezy(0), Hoarder(1), Regular(2)
        self.c_type = category
        self.rent_videos = []
        self.rentals = []
    def Check_illegal(self):
        pass
    def Rent_video(self):
        pass
    def info(self):
        return print(self.c_id, self.c_type)

class Breezy(Customers):
    def __init__(self, id, category):
        super().__init__(id, category)
    def Check_illegal(self):
        return True if len(self.rent_videos) < 3 else False
    def Rent_video(self):
        v_to_rent, n_to_rent = 0
        v_type = Counter()
        if(self.Check_illegal()): # Breezy(Rent 1 or 2 videos for 1 or 2 nights)
            v_to_rent = random.randint(1, 3 - len(self.rent_videos))
            n_to_rent = random.randint(1, 2)
            v_type = Counter([random.choices(range(0, 4), k = v_to_rent)]) # Customers choose video category
            return v_to_rent, n_to_rent, v_type
        else: return 0, 0, Counter()

class Hoarder(Customers):
    def __init__(self, id, category):
        super().__init__(id, category)
    def Check_illegal(self):
        return True if len(self.rent_videos) == 0 else False
    def Rent_video(self):
        v_to_rent, n_to_rent = 0
        v_type = Counter()
        if(self.Check_illegal()): # Hoarder(Always rent 3 videos for 7 nights)
            v_to_rent = 3
            n_to_rent = 7
            v_type = Counter([random.choices(range(0, 4), k = v_to_rent)]) # Customers choose video category
            return v_to_rent, n_to_rent, v_type
        else: return 0, 0, Counter()

class Regular(Customers):
    def __init__(self, id, category):
        super().__init__(id, category)
    def Check_illegal(self):
        return True if len(self.rent_videos) < 3 else False
    def Rent_video():
        v_to_rent, n_to_rent = 0
        v_type = Counter()
        if(self.Check_illegal()): # Regular(Rent 1 - 3 videos for 3 - 5 nights)
            v_to_rent = random.randint(1, 3 - len(self.rent_videos))
            n_to_rent = random.randint(3, 5)
            v_type = Counter([random.choices(range(0, 4), k = v_to_rent)]) # Customers choose video category
            return v_to_rent, n_to_rent, v_type
        else: return 0, 0, Counter()

class Rental():
    def __init__(self, c_id, c_type, night, videos):
        self.c_name = c_id
        self.c_type = c_type
        self.r_night = night
        self.r_videos = videos
    def info(self):
        print('Customer ' + str(self.c_name) + ' rent: ')
        for i in self.r_videos:
            i.info()

class Rental_Store:
    def __init__(self):
        self.videos = []
        self.rentals = []
        self.complete_rental = []
        self.total_amount = 0
        # Build videos
        for i in range(20):
            self.videos.append(Videos(i, random.randint(0, 4))) # 5 categories
    def Check_inventory(self):
        return len(self.videos)
    def Customer_rent(self, customer, v_to_rent, n_to_rent, v_type):
        # Check inventory
        if(self.Check_inventory() >= v_to_rent):
            valid_list = [] # Save current valid video_id to rent
            for k, v in v_type.items():
                videos_list = []
                if([x for x in self.videos if x.v_category == k].count() >= v): # Store has enough inventory
                    videos_list.append(random.sample([x for x in self.videos if x.v_category == k], k = v))
                    valid_list.append(videos_list)
            if(len(valid_list) == len(v_type)): # Check all videos that customer rents is available
                # Build Rental
                rent_out = []
                for v_list in valid_list:
                    for j in v_list:
                        rent_out.append(j)
                # Remove rented videos from store
                for i in rent_out:
                    self.total_amount += (i.price * n_to_rent) # Record for Store total amount
                    del self.videos[self.videos.index(i)]
                c_rental = Rental(customer.c_id, customer.c_type, n_to_rent, rent_out)
                self.rentals.append(c_rental)
                customer.rentals.append(c_rental)
                customer.rent_videos.append([x for x in rent_out])
                return True
            else:
                return False
        else:
            return False
    def Current_info(self, day):
        # show every information per day
        print('Day: ', day)
        print('Videos: ')
        if(self.check_inventory()):
            for i in range(5):
                print(video_category[i] + ' has ' + str(Counter(self.videos.values())[i]))
        else: print('There is no inventory in store today !')
        print('Today Complete Rental: ')
        for i in self.complete_rental:
            i.info()
        self.complete_rental.clear()

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

        # Rental Store open, and customers come to rent videos
        if(store.Check_inventory()):
            # inventory > 0, customers wil come
            print('TO Do')
        # End of day, show today's current store infomations
        store.current_info(i)

if __name__ == '__main__':
    renting()