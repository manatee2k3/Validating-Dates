thirty_months = ["09","04","06","11"]
thirty_one_months = ["01","03","05","07","08","10","12"]
# making two lists of the months, splitting them depending on if they have 30 days or 31

print ("please enter a day")
dd = int(input())  
print ("please enter a month")
mm = int(input())
print ("please enter a year")
yyyy = int(input())
#getting the input for the date, the int() changes the input from a string into an integer

def leap_year(x): #making a function that checks if the month is a leap year
    if x % 400 == 0: #a centurary leap year is divisible by 400 this %(modulo) checks if the year is divisible by 400
        print ('this is correct. and also a leap year')
    elif x % 4 == 0: #most leap years are divisible by 4 so this %(modulo) checks if its divisible by 4
        print ('this is correct. and also a leap year')
    else:
        print ('this dosent exist') #if the above find out that the year isnt divisible by 4 (not a leap year) it prints that it dosent exist
    
if dd > 31 or mm > 12: #this checks weather they put the date within 31 and the month within 12. 
    print ("Wow...were you even trying to write an accurate date?") #if it finds its true then it will print that its not an actual date 

elif dd <= 31 and mm <= 12: #this easily checks weather the input is within the basic parameters of what a date can be (between 31 for the date and 12 for the month)
    if dd == 31 and mm not in thirty_one_months : #checking if the month has 30 or 31 days by pulling from the list at the top.
        print ("That month dosent have that many days!")
        print ('Remember...30 days has September, April, June and November.')
    elif mm == 2 and dd > 29: #singling out february as it only has 28 or 29 days. 
        print ('February dosent have that many days.')
    elif mm == 2 and dd == 29: #checking if they posted the 29 which is only correct on a leap year
            leap_year(yyyy) #activates the leap year function.
    elif yyyy > 2020: #any date above 2020 is from the future.
        print ("Woah you're from the future!")
    elif yyyy == 2020: 
        print ("thats correct, that day exists!")
    elif yyyy < 2020: #any date below 2020 is in the past.
        print ("Woah you're from the past!")

        
    
    
