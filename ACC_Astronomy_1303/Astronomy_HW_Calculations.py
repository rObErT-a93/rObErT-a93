import math

mass_kg = 4e30
radius_m = 6.95e7

volume_m3 = (4/3) * math.pi * radius_m**3
density_kg_per_m3 = mass_kg / volume_m3

density_g_per_cm3 = density_kg_per_m3 * 0.001

print("Density of the red giant:" , density_g_per_cm3, "g/cm3")