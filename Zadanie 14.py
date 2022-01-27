import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1
    return completedTaskFrequencyByUser

""" gotowy schemat
def get_keys_with_top_values(my_dictionary):
    return [
    for (key, value) in my_disctionary.items()
    if value = max(my_dictionary.values())
    ]
"""
def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if numberOfCompletedTask == maxAmountOfCompletedTask:
            usersIdWithMaxCompletedAmountOfTasks.append(userId)
    return usersIdWithMaxCompletedAmountOfTasks

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawy format pliku")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTaskFrequencyByUser)
    print("The winner is user/users with ID: ", usersWithTopCompletedTasks)

"""
# sposób 1
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()

for user in users:
    if (user["id"] in usersWithTopCompletedTasks):
        print("The winner is user/users with ID: ", user["name"])

# sposób 2
for userId in usersWithTopCompletedTasks:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/" + str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users/", params = "id="+str(userId))
    user = r.json()
    print("The winner is user/users with ID: ", user[0]["name"])
"""

# sposób 3

def change_list_into_conj_of_param(my_list):

    return
conj_param = change_list_into_conj_of_param(usersWithTopCompletedTasks)

r = requests.get("https://jsonplaceholder.typicode.com/users/", params = "conj_param")
users = r.json()
for user in users:
    print("The winner is user/users with ID: ", user["name"])
