Volt = float(input('Enter the Voltage of power supply (Volt): '))
R1 = float(input('Enter the resistance of the 1st resistor (Ohm) : '))
R2 = float(input('Enter the resistance of the 2st resistor (Ohm) : '))
R3 = float(input('Enter the resistance of the 3st resistor (Ohm) : '))


resistor = R1 + R2 + R3
Amp = Volt / resistor
R1 *= Amp
R2 *= Amp
R3 *= Amp

print()
print("Electric current charge =", Amp, "Amp.")
print("The voltage across the 1st resistor =", round(R1, 3) ,"Ohm.")
print("The voltage across the 2st resistor =", round(R2, 3) ,"Ohm.")
print("The voltage across the 3st resistor =", round(R3, 3) ,"Ohm.")
