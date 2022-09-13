import matplotlib.pyplot as plt

exhaust_vel = 5000000 # m s-1
mass_flow = 10 # kg s-1
thrust = mass_flow * exhaust_vel # N

dt = 0.0001 # s

def calc_final_speed_no_drop(mass_ship, mass_drop, prop_ship, prop_drop):

    vel = 0

    while prop_ship > 0:

        if prop_ship < 0:
            prop_ship = 0

        if prop_drop < 0:
            prop_drop = 0
            
        total_mass = mass_ship + mass_drop + prop_ship + prop_drop
        accel = thrust/total_mass

        vel += accel * dt
        
        if prop_drop > 0:
            prop_drop -= mass_flow * dt
        else:
            prop_ship -= mass_flow * dt

    return vel

def calc_final_speed_w_drop(mass_ship, mass_drop, prop_ship, prop_drop):

    vel = 0

    while prop_ship > 0:

        if prop_ship < 0:
            prop_ship = 0

        if prop_drop < 0:
            prop_drop = 0

        if prop_drop > 0:
            total_mass = mass_ship + mass_drop + prop_ship + prop_drop
        else:
            total_mass = mass_ship + prop_ship
            
        accel = thrust/total_mass

        vel += accel * dt
        
        if prop_drop > 0:
            prop_drop -= mass_flow * dt
        else:
            prop_ship -= mass_flow * dt

    return vel

no_drops_list = []
yes_drops_list = []
ratios_list = []
mass_ratios_list = []
for i in range(10):
    mass_ship = 400 # kg
    mass_drop = 50 + i*10 # kg
    prop_ship = 750 # kg
    prop_drop = 200 # kg

    no_drop = calc_final_speed_no_drop(mass_ship, mass_drop, prop_ship, prop_drop)
    with_drop = calc_final_speed_w_drop(mass_ship, mass_drop, prop_ship, prop_drop)

    no_drops_list.append(no_drop)
    yes_drops_list.append(with_drop)

    mass_ratios_list.append(mass_drop/mass_ship)
    ratios_list.append(with_drop/no_drop)

plt.plot(no_drops_list)
plt.plot(yes_drops_list)
plt.ylabel("Final velocity")
plt.legend(["no drop", "with drop"])
plt.show()

plt.plot(mass_ratios_list, ratios_list)
plt.xlabel("Mass ratio (drop tank dry mass/ship dry mass)")
plt.ylabel("Final velocity ratio (tank dropped/tank kept attached)")
plt.show()
