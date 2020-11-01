
thirty_months = ["09","04","06","11"]
thirty_one_months = ["01","03","05","07","08","10","12"]


print ("please enter a day")
dd = input()
print ("please enter a month")
mm = input()
print ("please enter a year")
yyyy = input()

for thirty in thirty_months:
    thirty = int(thirty)

if int(dd) > 31 and int(mm) > 12:
    print ("thats incorrect,that date dosent exist!")
    
elif int(dd) <= 31 and int(mm) <= 12:
    if int(dd) == 31 and int(mm) == thirty:
        print ("That month dosent have that many days!")
    elif int(yyyy) > 2020:
        print ("Woah you're from the future!")
    elif int(yyyy) == 2020:
        print ("thats correct, that day exists!")
    elif int(yyyy) < 2020:
        print ("Woah you're from the past!")



#print ("you have entered " + dd + "/" + mm + "/" + yyyy)


