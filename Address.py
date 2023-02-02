class Address:
    def __init__(self, index, city, street, home, flat):
        self.index=index
        self.city=city
        self.street=street
        self.home=home
        self.flat=flat
        self.whithout_index=city+', '+street+', '+str(home)+"-"+str(flat)
    def my_return(self):
        return self.whithout_index
        

class Mailing:
    def __init__(self, to, frome, cost, track):
        self.to=to
        self.frome=frome
        self.cost=cost
        self.track=track
    def my_print(self):
        print('Отправление',self.track, 'из', self.frome, 'в', self.to+'. ', 'Стоимость', self.cost, 'рублей.')