import math
def volumespher(radius):
    V=(4*math.pi*(radius**3))/3
    return V
    
radius=float(input("Radius:"))
print(volumespher(radius))