#import the datetime class
import datetime

currebtDate = datetime.date.today()

strDeadline = " "
totalNbrDays = 0 
nbweek = 0
nbrDays = 0 
strDeadline = input("Please enter the date of your deadline: ")

deadline = datetime.datetime.strptime(strDeadline,"%m/%d/%Y").date()

#calculate number of days between the teo dates
totalNbrDays = deadline - currebtDate


#extra credit
nbweek = totalNbrDays.days / 7


nbrDays = totalNbrDays.days%7


print("###### Today is #######")
print(currebtDate)
print()
print("###################################")

print("you have %d weeks " %nbweek + " and %d days " %nbrDays + " until your dealine." )