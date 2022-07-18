#parameter
I = 5.00E-03
B = 0.5
D = 0.000005
D = 5
AB = -7.78E+00
ABm = 7.82E+00
BC = -2.28E+01
BCm = 2.28E+01
CD = -7.78E+00
CDm = 7.81E+00
DA = -2.28E+01
DAm = 2.28E+01
MAC11 = 1.44E+01
MAC12 = -1.44E+01
MAC21 = 1.55E+01
MAC22 = -1.55E+01
MBD11 = 1.56E+01
MBD12 = -1.55E+01
MBD21 = 1.44E+01
MBD22 = -1.44E+01

q = 1.602E-19

# expected value
bulk_concentration = -5.56E+18
sheet_concentration = -2.78E+15
sheet_resistivity = 1.26E+01
resistivity = 6.32E-03
conductivity = 1.58E+02
magneto_ratio = 1.12E-01
mobility = 1.78E+02
average_hall_coeffecient = -1.12E+00
AC_hall_coeffecient = -1.12E+00
BD_hall_coeffecient = -1.12E+00
ratio_vh = 3.42E-01
"""
# calculate
bc = 1/(q*average_hall_coeffecient)
rh = 1/(q*bc)
vh = rh*(I*B)/D
ns1 = (I*B)/(q*vh)
ns2 = bc * D
print(ns1,ns2)
print(bc,rh,vh)
print(resistivity/D)
"""

# Hall Coefficient
BDHC = D * (MBD12 - MBD11 + MBD21 - MBD22) / (B * I)
print("BD Hall Coefficent:", BDHC, "expected:",BD_hall_coeffecient) #unmatch
print(D/(I*B)*MBD11)
vh = BD_hall_coeffecient*(I*B)/D
print("VH:",vh)
