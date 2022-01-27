from datetime import datetime

user_input = input("enter your goal with deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
# calculation how many days from now till deadline
time_till = deadline_date - today_date

print(f"Dear user! Time remaining for you goal: {goal} is {int(time_till.days)} days")


