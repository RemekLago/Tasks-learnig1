from enum import IntEnum

Week_List = IntEnum("Week_List", "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday")

Prediction_Day = int(input("""Put day of the week and you will see your nearest future:
1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday
6. Saturday
7. Sunday
"""))

if Prediction_Day == Week_List.Monday:
    print("You will be working 5 days this week")

elif Prediction_Day == Week_List.Tuesday:
    print("You will be working 4 days this week")

elif Prediction_Day == Week_List.Wednesday:
    print("You will be working 3 days this week")

elif Prediction_Day == Week_List.Thursday:
    print("You will be working 2 days this week")

elif Prediction_Day == Week_List.Friday:
    print("You will be working 1 days this week")

elif Prediction_Day == Week_List.Saturday:
    print("You have 2 days off")

elif Prediction_Day == Week_List.Sunday:
    print("You have only 1 days off")

else:
    print("Chose day of the week")
