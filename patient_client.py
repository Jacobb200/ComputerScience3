from Patient import Patient


def main():
    name = str(input("Please input your name: "))
    temp = float(input("Please input your temperature in Fahrenheit: "))
    print(f"Patient Name: {name}, Patient Temperature: {temp}\n")

    patient1 = Patient()
    try:
        patient1.name = name
    except ValueError:
        print("Invalid Name, must be 2-40 characters long")
    try:
        patient1.temp = temp
    except ValueError:
        print("Invalid temp, must be 88° to 111° Fahrenheit")
    patient1.display()

    name2 = str(input("PLease input your name: "))
    temp2 = float(input(f"Please input your temperature in Fahrenheit: "))
    print(f"Patient Name: {name2}, Patient Temperature: {temp2}\n")

    patient2 = Patient()
    try:
        patient2.name = name2
    except ValueError:
        print("Invalid Name, must be 2-40 characters long")
    try:
        patient2.temp = temp2
    except ValueError:
        print("Invalid temp, must be 88° to 111° Fahrenheit")
    print(patient2)

    print(Patient.sicker_patient(patient1, patient2))


main()

"""
Please input your name: j
Please input your temperature in Fahrenheit: 1
Patient Name: j, Patient Temperature: 1.0

Invalid Name, must be 2-40 characters long
Invalid temp, must be 88° to 111° Fahrenheit
Name: No Name; ID: 1; Temp: 0°

PLease input your name: jacob
Please input your temperature in Fahrenheit: 106
Patient Name: jacob, Patient Temperature: 106.0

*** urgent: attend immediately***
Patient name: jacob, ID: 2, Temperature: 106.0°

*** urgent: attend immediately***
Patient name: jacob, ID: 2, Temperature: 106.0°
, Patient name: No Name, ID: 1, Temperature: 0°
"""