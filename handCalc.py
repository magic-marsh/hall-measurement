#parameter
I = 0.005
B = 0.5
D = 0.000005
AB = -22.7475
ABm = 22.5675
BC = -7.7614
BCm = 7.7097
CD = -22.5549
CDm = 22.7607
DA = -7.6959
DAm = 7.7711
MAC11 = -15.5882
MAC12 = 15.3537
MAC21 = -14.4794
MAC22 = 14.2572
MBD11 = -14.2976
MBD12 = 14.4251
MBD21 = -15.4021
MBD22 = 15.5302
q = 1.602e-19

# Concentration
HallCo = -3.1570e-03
#Ns = (I * B) / (q * MAC)
#print(Ns)
Nb = 1 / (q * HallCo)
#print(Nb)
Ns = Nb * D
#print(Ns)
VH = (I * B)/(q * Nb * D)
#print(VH)

# Hall Coefficient
BDAC = D * (MBD12 - MBD11 + MBD21 - MBD22) / (B * I)
print("BD Hall Coefficent:", BDAC) #unmatch

# Mobility
resistivity = 6.2744e-03
hall_coefficient = -1.1037e+00
mobility = hall_coefficient / resistivity
print("Mobility:", mobility)  #checked