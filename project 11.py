import math

class Sphere:
    def __init__(self,radius):
        self.radius = radius
        self.area = 0
        self.volumeResult = 0

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        r = self.radius         
        self.area = 4 * math.pi * (r * r)            
        return self.area

    def volume(self):
        r = self.radius         
        
        self.volumeResult = (4/3) * math.pi * (r * r * r)
        return self.volumeResult

def main():
    r = input("enter radius of circle:")
    r = int(r)
    radius = Sphere(r)
    v = radius.volume()
    a = radius.surfaceArea()

    print(v)
    print(a)

main()
