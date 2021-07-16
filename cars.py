class Cars(object):
    def __init__(self, model, company, color, speed_limit):
        self.model = model
        self.company = company
        self.color = color
        self.speed_limit = speed_limit
    
    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating")

    def changeGear(self, gearType):
        print("gear changed")



audi = Cars("A6", "audi", "black", 80)
print(audi.stop())


