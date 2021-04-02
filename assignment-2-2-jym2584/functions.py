'''
Functions of age in months
'''

# Gathering inputs
def age_in_months():
    ''' Calculating age in months
    '''
    current_year = int(input("Current year: ")) # We want to get the current year
    current_month = int(input("Current month: ")) # We want to get the current month
    birth_year = int(input("Birth year: ")) # Birth year
    birth_month = int(input("Birth month: ")) # Birth month

    aim_calc(current_year, current_month, birth_year, birth_month) # Calculating age in months

def day_of_the_year():
    ''' Calculating day of the year
    '''
    month = int(input("Enter a month: ")) # We want to get a month
    day = int(input("Enter a day: ")) # Getting a day

    doty_calc(month, day) # Calculating day of the year


# Calculations
def aim_calc(current_year, current_month, birth_year, birth_month):
    ''' Calculates age in months
    '''
    print("Your age in months: ", (current_year - birth_year)*12 + (current_month-birth_month), # Prints age in months
    "\nAge in years!: ", ((current_year - birth_year)*12 + (current_month-birth_month))/12, sep="") # Divides formula by 12!

def doty_calc(month, day):
    ''' Math for day of the year
    '''
    print("The approximate day of the year is: ", ((month * 30.4) + (30.4-day)), " days!", sep="") # Prints day of the year!

# Executes code
def main():
    age_in_months()
    age_in_months()
    age_in_months() # ran this 3 times
    day_of_the_year()
    day_of_the_year()
    day_of_the_year() # Also ran this 3 times
main()