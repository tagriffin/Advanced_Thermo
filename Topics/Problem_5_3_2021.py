from Tools import IG_EQ_ed8 as EQ
import matplotlib.pyplot as plt
import numpy as np

CH4_ox = EQ.IG_Reaction('CH4_Ox',['CH4', 'O2','CO2','H2O'], [-1, -2, 1, 2])
print(CH4_ox.DeltaH_Rxn(298.15))
#print(CH4_ox.DeltaG_Rxn(298.15))
print(CH4_ox.DeltaH_Rxn(2000))

C2H6_ox = EQ.IG_Reaction('C2H6_Ox',['C2H6', 'O2','CO2','H2O'], [-1, -3.5, 2, 3])
print(C2H6_ox.DeltaH_Rxn(298.15))
#print(C2H6_ox.DeltaG_Rxn(298.15))
print(C2H6_ox.DeltaH_Rxn(2000))
