user_choice = -1

tasks = []
tasks.append("wyniesc smieci")
tasks.append("posprzatac biurko")
tasks.append("umyc samochod")

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1

def add_task():
    task = input("Wpisz tresc zadania")
    tasks.append(task)
    print(Dodano zadanie!)

def delete_task():
    task_index = int(input("Podaj indeks zadania do usuniecia)"))

    if task_index < 0 or task_index > len(tasks) - 1
        print("Zadanie o tym indeksie nie istnieje ")
        return
    tasks.pop(task_index)
    print(Usunięto zadanie)

def save_tasks_to_file():
     file = open("tasks.txt","w")
     for task in tasks:
         file.write(task+"\n")
     file.close()

while user_choice != 5:
    if user_choice == 1:
        show_task()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()

    if user_choice ==4:
        save_tasks_to_file()

        print( )
        print ("1. Pokaz zadania")
        print ("2. Dodaj zadanie")
        print ("3. Usun zadanie")
        print ("4. Zapisz zmiany w pliku")
        print ("5. Wyjdz")

    user_choice = int(input("Wybierz liczbe "))
    print()
