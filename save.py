import os
import matplotlib.pyplot as plt
import subprocess
import math 

data_library = [
    "Plotting chart", 
    "Histogram",
    "Pie chart",
    "Matrix",
    "Scatter"
]

while True:
    object_data_p = []
    object_data_h = []
    object_data_calculate_sum = []
    object_data_calculate_substract = []
    object_data_calculate_times = []
    print("---------------------------------------------")
    print("-------------Data Analysis-------------------")
    print("---------------------------------------------")
    print("Analysis my data (press 1): ")
    print("More information about data analysis (press 2): ")
    print("Show data library (press 3): ")
    enter = str(input("Enter: "))
    os.system("cls")
    if enter == "1":
        data = str(input("What type of data would you like to analyze?"))
        os.system("cls")
        if data[0] == "P" or (data[0] == "p"):
            print("Press based on the number of data you want to continue")
            print("No.------ Data ------")
            print("1. ------ ",data_library[2], "------")
            print("2. ------ ",data_library[0], "------")
            enter_data_p = str(input("Enter: "))
            if enter_data_p == "1":
                number = int(input("Enter number of objects: "))
                for i in range(number):
                    user_input = input("Name your objects / object" + str(i) + ": ")
                    print("Please enter the data for each object below")
                    data = input("Data " + str(i) + ": ")
                    object_data_p.append((user_input, data))
                os.system("cls")
                labels, values = zip(*object_data_p)
                plt.pie(values, labels=labels, autopct='%1.1f%%')
                plt.axis('equal')
                plt.legend()
                plt.show()
                os.system("cls")
            elif enter_data_p == "2":
                M_script = r"C:/Users/PC18/Desktop/Data_analysis_project-main/library/plotting.py"
                subprocess.call(['python', M_script])
        elif data[0] == "H" or (data[0] == "h"):
            print("Press based on the number of data you want to continue")
            print("No.------ Data ------")
            print("1. ------", data_library[1], "------")
            enter_data_h = str(input("Enter: "))
            if enter_data_h == "1":
                number_h = int(input("Enter number of data needed: "))
                value = str(input("Please name a value"))
                frequency = str(input("Please name a frequency"))
                for i in range(number_h):
                    user_input_h = input("Please enter your data name" + str(i) + ": ")
                    data_h = input("Please enter your value for each data (integer)" + str(i) + ": ")
                    object_data_h.append((user_input_h, data_h))
                os.system("cls")
                plt.hist(object_data_h, bins=number_h, edgecolor='black')
                plt.xlabel(value)
                plt.ylabel(frequency)
                plt.legend()
                plt.show()
        elif data[0] == "M" or (data[0] == "m"):
            M_script = r"C:/Users/PC18/Desktop/Data_analysis_project-main/library/First_m.py"
            subprocess.call(['python', M_script])
        elif data[0] == "C" or (data[0] == "c"):
            print("No------ Data ------")
            print("1.------ Calculatpr ------")
            input_next = int(input("Enter the No. of data you want: "))
            if input_next == "1":
                print("Choose the categories of calculation: ")
                print("1. Sum (+)")
                print("2. Substract (-)")
                print("3. Times (X)")
                calculate = int(input("Enter the number based on what you would like to calculate: "))
                if calculate == "1":
                    print("How many variable would you like to calculate in format of integer?")
                    number = int(input("Enter: "))
                    for i in range(number):
                        print("Calculate variable" + str(i) + ": ")
                        summing = input(int("Enter: "))
                        os.system["cls"]
                        object_data_calculate_sum.append(summing)
                    total_sum = sum(object_data_calculate_sum)
                    print("You total sum is: ", total_sum)
                elif calculate == "2":
                    print("How many variable would you like to substract? ")
                    number_substract = int(input("Enter the number based on what you would like to calculate: "))
                    for i in range(number_substract):
                        print("Calculate variable" + str(i) + ": ")
                        substracting = input(int("Enter: "))
                        os.system["cls"]
                        total_substract = substracting[i] - substracting[i-i]
                        object_data_calculate_substract.append(total_substract)
                    print(object_data_calculate_substract)
                elif calculate == "3":
                    print("How many variable would you like to times? ")
                    number_times = int(input("Enter the number based on what you would like to calculate: "))
                    for i in range(number_times):
                        print("Calcute variable" + str(i) + ": ") 
                        times_all = input(int("Enter"))
                        os.system["cls"]
                        object_data_calculate_times.append(times_all)
                        total_times = math.prod(object_data_calculate_times)
                    print("The total result is: ", total_times)         


    elif enter == "2":
        print("Data analysis is the process of inspecting, cleansing, transforming, and modeling data with the goal of discovering useful information,")
        print("informing conclusions, and supporting decision-making.")
        print("Business intelligence: Simple and cost effective to run high-performance queries on petabytes of semi-structured and structured data so that you can build powerful reports and dashboards.")
    elif enter == "3":
        os.system("cls")
        print(data_library)