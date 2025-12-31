class Mobile:
    def __init__(self, model, ram, rom):
        self.model = model
        self.ram = ram
        self.model = model


class Iphone(Mobile):
    type = "Iphone"

    def __init__(self, model, ram, rom, os):
        super().__init__(model, ram, rom)
        self.os = os

    def __str__(self):
        return f"This is an Iphone model {self.model}"


class Android(Mobile):
    type = "Android"

    def __init__(self, model, ram, rom, os):
        super().__init__(model, ram, rom)
        self.os = os

    def __str__(self):
        return f"This is an Android model {self.model}"


Redmi_9 = Android("Redmi 9",8,128,"Android")
print(Redmi_9.__str__())
Iphone16pro = Iphone("16 pro",18,1,"IOS")
print(Iphone16pro.__str__())
