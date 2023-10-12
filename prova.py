import math

AU = 149597870707
G = 6.67430e-11
mass_sun = 1.989e30
mass_earth = 5.972e24
distance_earth_sun = 1.496e11

ang = 0
dist_to_sun = 1 * AU


sun_pos = [0, 0]
earth_pos = [100, 0]
r_x = earth_pos[0] - sun_pos[0]
r_y = earth_pos[1] - sun_pos[1]
r = math.sqrt(r_x**2 + r_y**2)


def get_force(m1, m2, r):
    F = (G * m1 * m2) / (r**2)
    alpha = math.atan2(r_y, r_y)
    F_x = math.cos(alpha) * F
    F_y = math.sin(alpha) * F
    return F_x, F_y


while True:
    F_x, F_y = get_force(mass_sun, mass_earth, r)

    earth_pos[0] += F_x / mass_earth
    earth_pos[1] += F_y / mass_earth

    print(earth_pos)
