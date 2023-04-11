
def fer_to_cel():
        conv_dict = {
                "Farenheit_Celcius":"C",
                "Celcius_Farenheit": "F"
        }
        print(conv_dict.items())
        print()

        choice = input("press corresponding letter to go through: ")

        if choice.lower() == "c":
                while True:
                        temp_f = input("Enter temp in farenheit exit[x]: ")
                        res = (float(temp_f) - 32)/1.8
                        print(f"Temperature in Celcius is: {res}C")
                        if temp_f == 'x':
                                break

        elif choice.lower() == "f":
                while True:
                        temp_c = input("Enter temp in Celcius, exit[x]: ")
                        res = (float(temp_c)*1.8) + 32                                  
                        print(f"Temperature in Farenheit is :{res}F")
                        if temp_c == 'x':
                                break
        else :
                print("Only enter the valid key")
                        
# fer_to_cel()

def cel_to_kel():
        key = ["Kelvin_Celcius","Celcius_Kelvin"]
        val = ["C","K"]
        comb = list(zip(key,val))
        for i in comb:
                print(i)

        choice = input("Chose the corresponding  key to go through,exit[x]: ")

        if choice.lower() == "k":
                while True:
                        temp_c = input("Celcius to Kelvin exit[x]: ")
                        res = float(temp_c) + 273.15
                        print()
                        print(f"temperature in Kelvin is :{res}K")
                        if temp_c == "x":
                                break

        elif choice.lower() == "c":
                while True:
                        temp_k = input("kelvin to celcius,exit[x]: ")
                        res = float(temp_k) - 273.15
                        print(f"Temperature in celcius is {res}C")
        else:
                print("Only enter the valid key")
# cel_to_kel()

def fer_to_kel():
        temp_list = ["Farenheit_to_Kelvin","Kelvin_to_Farenheit"]
        for i in enumerate(temp_list):
                print(i)
        choice = int(input("Enter the corresponding number to go through: "))
        if choice == 0:
                while True:
                        temp_fk = input("Farenheit to Kelvin,exit[x]: ")
                        res = float(temp_fk) * 1.8+32
                        reslt = res + 273.15
                        print(f"Temperature in Kelvin is {reslt}K")
                        if temp_fk.lower() == "x":
                                break        
        elif choice == 1:
                while True:
                        temp_kf = input("Kelvin To Farenheit,exit[x]: ")
                        res = float(temp_kf)-273.15
                        reslt = res*1.8 + 32
                        print(f"Temperature in farenheit is {reslt}F")
                        if temp_kf.lower() == "x":
                                break
        else:
                print("Enterthe valid key")
                        

fer_to_kel()