I = 0.005
B = 0.5
D = 1e-4
#MAC = 0.0156811

MAC1 = 15.6811
MAC2 = -15.6292
MAC1M = 15.8382
MAC2M = -15.7882
AB = -0.0033221
q = 1.602e-19
HallCo = -3.1570e-03
#Ns = (I * B) / (q * MAC)
#print(Ns)
Nb = 1 / (q * HallCo)
print(Nb)
Ns = Nb * D
print(Ns)
VH = (I * B)/(q * Nb * D)
print(VH)

ACHallCo = (MAC1 - MAC2 + MAC2M - MAC1M) * D / (B * I)
print ("AC-HallCoeffecient:", ACHallCo)