class Smartphone:
    def __init__(self, name, model, number):
       self.phone_name = name
       self.phone_model = model
       self.phone_number = number
    def printer(self):
        print(str(self.phone_name)+' - '+str(self.phone_model)+'. '+str(self.phone_number))