from art import title
import os
import time
from tabulate import tabulate

def menu():
    show_menu = True
    while show_menu:
        os.system("cls")
        print(title)
        print("\n" + "-" * 75 + "\n")
        print("[1] First half")
        print("[2] Second half")
        print("[3] Exit\n")
        option_selected = input("Please select an option: ")
        if option_selected == "1":
            first_half()
            break
        elif option_selected == "2":
            second_half()
            break
        elif option_selected == "3":
            exit()
        else:
            os.system("cls")
            print("Please select a valid option")
            time.sleep(2)
            os.system("cls")


def input_control(message, half):
    invalid_input = True
    while invalid_input:
        data_inputted = input(f"{message}")
        if data_inputted.lower() == "r":
            os.system("cls")
            print("Please input the correct value")
            time.sleep(2)
            if half == 1:
                first_half()
            elif half ==2:
                second_half()
        else:
            try:
                transformed_data = float(data_inputted)
                return transformed_data
            except ValueError:
                print("Please input a valid value")
                time.sleep(2)


def exit_program():
    show_question = True
    while show_question:
        start_over = input("\nDo you want to load another operation? (y/n): ")
        if start_over.lower() == "y":
            menu()
            break
        elif start_over.lower() == "n":
            exit()
        else:
            print("\nPlease select a valid option")       

def first_half():
    os.system("cls")
    print("Please complete the information requested")
    print("If you make a mistake input [R/r] in any field")
    print("-------------------------------------------")
    retention_rate = input_control("Retention rate(%): ", 1) / 100
    non_tax_minimun = input_control("Non taxable amount: ", 1)
    transferred_amount = input_control("Transferred amount: ", 1)
    total_bill = (transferred_amount - non_tax_minimun * retention_rate) / (1 - 1 / 1.21 * retention_rate)
    net_amount = total_bill / 1.21
    tax = net_amount * 0.21
    retention = - (net_amount - non_tax_minimun) * retention_rate
    data_table = [
        ["Net Amount", "Taxes", "Total", "Retention", "Transferred Amount"], 
        [net_amount, tax, total_bill, retention, transferred_amount]
    ]
    print("-------------------------------------------")
    print(tabulate(data_table, headers='firstrow', tablefmt='fancy_grid', floatfmt=".2f", stralign='center'))
    exit_program()


def second_half():
    os.system("cls")
    print("Please complete the information requested")
    print("If you make a mistake input [R/r] in any field")
    print("-------------------------------------------")
    previous_net_amount = input_control("Previous net amount: ", 2)
    previous_retention = input_control("Previous retention: ", 2)
    retention_rate = input_control("Retention rate(%): ", 2) / 100
    non_tax_minimun = input_control("Non taxable amount: ", 2)
    transferred_amount = input_control("Transferred amount: ", 2)
    total_bill = (transferred_amount + (previous_net_amount - non_tax_minimun) * retention_rate - previous_retention) / (1 - 1 / 1.21 * retention_rate)
    net_amount = total_bill / 1.21
    tax = net_amount * 0.21
    retention = - ((net_amount + previous_net_amount - non_tax_minimun) * retention_rate - previous_retention)
    data_table = [
        ["Net Amount", "Taxes", "Total", "Retention", "Transferred Amount"], 
        [net_amount, tax, total_bill, retention, transferred_amount]
    ]
    print("-------------------------------------------")
    print(tabulate(data_table, headers='firstrow', tablefmt='fancy_grid', floatfmt=".2f", stralign='center'))
    exit_program()

if __name__ == "__main__":
    menu()