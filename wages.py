# Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly
# If age does not fall in any range then display the following message:“Enter appropriate age”

age= int(input("enter age: "))
sex= input("enter M or F: ")
day= int(input("enter day: "))
if sex=="M" or sex=="m":
    if age>=18 and age<30:
        wages= day*700
        print("wages=",wages)
    elif age>=30 and age<=40:
        wages= day*800
        print("wages=",wages)
    else:
        print("enter appropriate age")
elif sex=="F" or sex=="f":
    if age>=18 and age<30:
        wages= day*750
        print("wages=",wages)
    elif age>=30 and age<40:
        wages= day*850
        print("wages=",wages)
    else:
        print("enter appropriate age")
else:
    print("enter appropriate age")