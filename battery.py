class Battery:
    def __init__(self):
        pass

    def batterystatus(time, capacity, Ibat):



        SoC = 1 - Ibat * time * capacity * 3600 #State of charge of the battery
        

        return SoC
    
