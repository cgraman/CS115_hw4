#Prolog
#Author: Colin Graman
#Email: cagr259@uky.edu
#Section: 001
#Date: 2/3/2023

'''
Purpose:  offer the user a choice of food items, calculate total bill
Pre-conditions:  user enters 5 or 6 y's or n's depending on desired items (strings)
Post-conditions:  prompts for choices, total bill before (float) and after 20% tip, (float)
    and parting message.
'''
def (main):

# name of food vendor
    print("Welcome to Chuys")
# give user instructions of expected inputs
    print('Please answer each question with y or n')
    print()
# initialize total bill to zero
    total_bill = 0
# ask first choice
    chicka_boom = str(input("Would you like to try our Chicka-Chicka Boom-Boom?"))
# if the user desired the item, 
    if chicka_boom == 'y':
        total_bill += 14.09
#add price to total bill
#complete the design for the rest of the menu
    chick_fluatas = str(input("Can I get you some Chicken Fluatas?"))
    if chick_fluatas == 'y':
        total_bill += 11.86
    
    tacos = str(input("How about Crispy Tacos?"))   
    if tacos == 'y':
        total_bill += 11.44
        
    quesadilla = str(input("Can I interest you in some Quesadillas?"))        
    if quesadilla == 'y':
        guac_quesadilla = str(input("Would you like to add a scoop of guac?"))
        if guac_quesadilla == 'y':
            total_bill = 10.93
        else:
            total_bill = 8.49
        
    tres_leches = str(input("would you like to try our Tres Leches?"))        
    if tres_leches == 'y':
        total_bill += 9.00


    total_bill_tip = total_bill * 1.2

# output blank line
    print()
# output total bill before 20% tip 
    print("The total for you food is $", end='')
    print(f'{total_bill:.2f}')
    print("Your total with 20% tip is $", end='')
    print(f'{total_bill_tip:.2f}')
    print("Thanks for choosing to eat with us today!")
#complete rest of design
main()

'''
Individual Problem #1
A.$11.86,$14.23
B.$8.49,$10.19
C.$37.39,$44.87
D.$0.00,$0.00
E.$57.32,$68.78
'''