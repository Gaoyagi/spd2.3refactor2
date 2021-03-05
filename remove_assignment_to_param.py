# By Kami Bigdely
# Remove assignment to method parameter.
class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value
class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
def calculate_kinetic_energy(mass, distance, time):
    kmDist = None
    if distance.unit != 'km':
        if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit        
            in_km = distance.value * 9.461e12
            kmDist = Distance(in_km, "km") 
        else:
            print ("unit is Unknown")
            return
    else:
        kmDist = distance
        
    speed = kmDist.value/time # [km per sec]

    solarMass = None
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            value = mass.value * 1.98892e30 # [kg]
            solarMass = Mass(value, 'kg')
        else:
            print ("unit is Unknown")
            return  
    else:
        solarMass = mass  

    kinetic_energy = 0.5 * solarMass.value * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))