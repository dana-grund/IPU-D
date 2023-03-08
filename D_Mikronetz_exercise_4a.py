# --------------------------------------------------
# Script: IP Umweltbeobachtung Versuch D - Mikronetz 
# Kapitel 4, Aufgabe 1.a)
# Usage: python D_Mikronetz_exercise_solution.py
# --------------------------------------------------
import numpy as np

# constants
L = 1.5 #1.3 # Hebung in kg
P = 0.9 #Payload in kg
R = L-P
Cd = 0.25 #Reibungskoeffizient
rhoAir = 1.205 #kgm^-3
rhoHe = 0.166 #kgm^-3
g = 9.81 #m/s^2

# calculation
V = L/(rhoAir-rhoHe) #Volume
r = (V*3/(np.pi*4))**(1/3) #Radius
A = math.pi*r**2
v = (R*g/(0.5*Cd*A*rhoAir))**(1/2)

# display results
print("Volumen (V): ",V)
print("Radius (r): ",r)
print("Netto Hebung (R): ",R)
print("Flaeche (A): ",A)
print("Aufstiegsgeschwindigkeit (v): ",v)



