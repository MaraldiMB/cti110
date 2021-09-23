# Calculate bill payments monthly and annually
# 9/22/2021
# CTI-110 P1HW2 - Basic Math
# Mary Beth Maraldi
#

# Gather needed inputs
expense = input('Enter name of expense: ')      
charge = float(input('Enter monthly charge: '))

# Set varriables and equations
tax = .06 * charge  # This equation will change if the tax percent changes. 
total = charge + tax
annual = total * 12


print()

# display Bill name and amount before tax
print('Bill:', expense, '--------- Before Tax:', '${:.2f}'.format(charge))

# dispaly amount of tax charged a month if tax is 6%
print('Monthly tax:       ', '${:.2f}'.format(tax))

# display total amount to be paid monthly
print('Monthly charge:    ', '${:.2f}'.format(total))

# display total amount to be paid annualy--- *changed format style for readability*
print('Annual charge:     ', '${:,.2f}'.format(annual))

