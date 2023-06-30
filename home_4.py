class Washer:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.powder = 0
        self.is_work = False

    def  __str__(self):
        return f'{self.brand} {self.color} {self.powder} {self.is_work}'

    def info(self):
        return f"Ваш бренд - {self.brand}\nЦвет - {self.color}"
    
    def start(self):
        self.is_work = True
        self.powder -= 20
        if self.powder < 20:
            print("Не хватает порошка")
        else:
            print(f"Ваша машина работает - {self.is_work}")

    def refuel(self, gram):
        self.powder = gram
        if gram > 100:
            print("Вы можете положить только 100gram порошка:")
        elif gram < 0:
            print("вы не пополнели")
        elif gram > 0 and gram < 10:
            print("Вы пополнили слишком мало:")
        else:
            return f"{self.start()}"

    def finish(self):
        self.is_work = False
        return f"Стиральная машина отключена - {self.is_work}"
            


washer = Washer('AEG', 'Black')
print(washer)
print(washer.info())
washer.refuel(100)
print(washer.finish())
