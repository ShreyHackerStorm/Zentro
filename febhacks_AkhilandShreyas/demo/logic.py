weeklyAllowance=input("Enter your weekly allowance:")
weeklyAllowance=int(weeklyAllowance)
#For Every Day
end=True
while end:
    for i in range(0,7,1):
        day=input("Enter the day of the week")
        totalSpent=0
        weeklyExpenditure={}
        dailyExpenditure=[]
        category=input("Enter a category you spent money in:")
        amount=input("Enter the amount spent in that category:")
        amount=int(amount)
        totalSpent +=amount
        dailyExpenditure.append(category)
        dailyExpenditure.append(amount)
        weeklyExpenditure[day]=dailyExpenditure
        done=input("Is that all you spent today:")
        if done=="Yes":
            end=False 
print("You have spent ",totalSpent, "dollars. You currently have saved", weeklyAllowance-totalSpent,"Dollars")
print(weeklyExpenditure)

