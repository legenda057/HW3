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
        if self.powder >= 100:
            return f"Вы можете положить только 100gram порошка:"
        else:
            self.powder -= 20
        if self.powder < 20:
            return f"Не хватает порошка"
        self.is_work = True
        return f"Ваша машина работает - {self.is_work}"

    def refuel(self):
        if self.powder > 100:
            return f"Вы можете положить только 100gram порошка:"
        self.powder += 100
        return f"Машинка заправлена"
            
              

    def finish(self):
        self.is_work = False
        return f"Стиральная машина отключена - {self.is_work}"
    
    def main(self):
        while True:
            commands = input("1 - Информация, 2 - Начало стирки, 3 - Заправка порошка, 4 - Финиш :")
            if commands == "1":
                print(washer)
            elif commands == "2":
                print(washer.start())
            elif commands == "3":
                print(washer.refuel())
            elif commands == "4":
                print(washer.finish())
                break
        return f"До свидания!"        
            


washer = Washer('AEG', 'Black')
print(washer.main())
