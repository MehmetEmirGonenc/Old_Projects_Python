class Car:
    def __init__(self,name,engine,hp,price):
        self.name=name
        self.engine = engine
        self.hp = hp
        self.price = price
    def ShowDetail(self,number):
        print(f'Car-{number} >>> Name : {self.name}  |  Engine : {self.engine}  |  HP : {self.hp}  |  Price : {self.price}')


