weeklyAllowance = int(input("Enter your weekly allowance: "))
weeklyGoals = {}

def goal_setting(goals):
    print("Let's set some goals for the week")
    while True:
        category = input("Name a category to spend in: ")
        amount = int(input(f"How much do you want to spend in {category}: "))
        goals[category] = amount
        done = input("Is that all your goals? (Yes/No): ")
        if done.lower() == "yes":
            break

goal_setting(weeklyGoals)

weeklyExpenditure = {}
totalSpent = 0

while True:
    day = input("Enter the day of the week: ")
    if day not in weeklyExpenditure:
        weeklyExpenditure[day] = {}

    while True:
        category = input("Enter a category you spent money in: ")
        amount = int(input("Enter the amount spent in that category: "))
        totalSpent += amount

        if category in weeklyExpenditure[day]:
            weeklyExpenditure[day][category] += amount
        else:
            weeklyExpenditure[day][category] = amount

        more = input("Any more spending for today? (Yes/No): ")
        if more.lower() == "no":
            break

    done = input("Is that all your spending for the week? (Yes/No): ")
    if done.lower() == "yes":
        break

# Calculate total spent per category
totalPerCategory = {}
for day in weeklyExpenditure:
    for category in weeklyExpenditure[day]:
        if category in totalPerCategory:
            totalPerCategory[category] += weeklyExpenditure[day][category]
        else:
            totalPerCategory[category] = weeklyExpenditure[day][category]

print("\nSummary of Spending Compared to Goals:")
for category in weeklyGoals:
    spent = totalPerCategory.get(category, 0)
    goal = weeklyGoals[category]
    if spent > goal:
        print(f"You are ${spent - goal} over your goal in {category}.")
    else:
        print(f"You are on track in '{category}'. You are ${goal - spent} under your goal.")

print(f"\nYou have spent ${totalSpent}. You currently have saved ${weeklyAllowance - totalSpent}.")
print("Weekly Expenditure Breakdown:", weeklyExpenditure)
