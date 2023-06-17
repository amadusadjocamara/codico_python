import datetime


currentday = datetime.date.today()
userinpt = input ("what is your brithday? ")

birt = datetime.datetime.strptime(userinpt, '%m/%d/%Y').date()

#why did we list datetime twice
#because we are calling the strptime function 
#which is part of the datetime class
#which is in the datetime module
#print("Your birth month is " + birthdate.strtime("%B"))

print(birt)

dd = birt - currentday
print (dd.days)