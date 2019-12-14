def obrits_from_COM(orbits, solar_system, planet):
    while(planet != 'COM'):
        for p in solar_system:
            if ')' + planet in p:
                orbits[0] += 1
                planet = p.split(')')[0]
    return orbits

# recursion limit reached for this function
# def calcOrbits1(orbits, solar_system = [], unique_planets = [], visited = [], curr_planet = 'COM'):
#     if curr_planet not in visited:
#         visited.append(curr_planet)
#         orbits = obrits_from_COM(orbits, solar_system, curr_planet)
#         for p in solar_system:
#             if ')' + curr_planet in p:
#                 recursive_planet = p.split(')')[0]
#                 orbits = calcOrbits(orbits, solar_system, unique_planets, visited, recursive_planet)
#     for recursive_planet in unique_planets:
#         if recursive_planet not in visited:
#             orbits = calcOrbits(orbits, solar_system, unique_planets, visited, recursive_planet)
#     return orbits

def calcOrbits(orbits, solar_system = []):
    visited = []

    unique_planets = []
    for p in solar_system:
        split = p.split(')')
        if split[0] not in unique_planets:
            unique_planets.append(split[0])
        if split[1] not in unique_planets:
            unique_planets.append(split[1])

    for p in unique_planets:
        curr_planet = p.split(')')[0]
        if curr_planet not in visited:
            visited.append(curr_planet)
            obrits_from_COM(orbits, solar_system, curr_planet)
    return

if __name__ == '__main__':

    f = open("solar_system.txt", "r")
    solar_system = f.read()
    solar_system = solar_system.split('\n')
    for i in range(len(solar_system) - 1, 0, -1):
        if not solar_system[-1]:
            solar_system = solar_system[:-1]

    orbits = [0]
    calcOrbits(orbits, solar_system)
    print(orbits[0])
