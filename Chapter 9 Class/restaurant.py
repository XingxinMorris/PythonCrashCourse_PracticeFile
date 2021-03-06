class Restaurant():
    """make some change"""
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("Our restaurant is "+self.restaurant_name+".")
        print("We provide "+self.cuisine_type+" for you.")
    
    def open_restaurant(self):
        print("We are opening right now!")
    
    def show_customer(self):
        print("We have served "+str(self.number_served)+" customers.")
        
    def set_number_served(self,customer_num):
        self.number_served = customer_num
    
    def increment_number_served(self,increment_num):
        self.number_served += increment_num