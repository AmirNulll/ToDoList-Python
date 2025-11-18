import json
from datetime import datetime

def loadData():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []



def saveData(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def addEntry(task,category):
    data = loadData()
    entry = {
        'task': task,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'category': category

    }
    data.append(entry)
    saveData(data)
    print("✅ Task added successfully!")

def filterbydate(inputDate,):
    data = loadData()
    filteredData = []
    for entry in data:
        ts=datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S')
        if ts.strftime('%Y-%m-%d') == inputDate:
            filteredData.append(entry)
    if len(filteredData) > 0:
        for i, entry in enumerate(filteredData, 1):
            print(f"{i}. {entry['task']} ({entry['timestamp']})")
    else: print('No match Data found')



def filterbycategory(inputCategory):
    data = loadData()
    filteredCategories = []

    for cate in data:
        if cate['category'] == inputCategory:
            filteredCategories.append(cate)
    if len(filteredCategories) > 0:
            for i,entry in enumerate(filteredCategories, 1):
                print(f"{i}.{entry['task']} ({entry['timestamp']}) {entry['category']} ")
    else:
        print('No match Data found')


def deleteEntry():
    data = loadData()
    if not data:
        print("No tasks to delete!")
        return

    showEntry()
    try:
        choice = int(input("Enter the number of the task to delete: "))
        if 1 <= choice <= len(data):
            removed = data.pop(choice - 1)
            saveData(data)
            print(f"✅ Task '{removed['task']}' deleted successfully!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

def stats():
    data = loadData()
    total = len(data)
    print(f"Total tasks: {total}")

def showEntry():
    data = loadData()
    if not data :
        print('i dont have data yet')
        return
    for i , entry in enumerate(data,1):
        print(f"{i}. {entry['task']} ({entry['timestamp']}) - {entry['category']}")

def editTasks():
    data = loadData()
    if not data:
        print("No tasks to Edit!")
        return
    showEntry()
    try:
        choice = int(input("Enter the number of the task to Edit: "))
        if 1 <= choice <= len(data):
            changed = data[choice - 1]
            EditText=input("Enter the new text: ")
            old=changed['task']
            changed['task'] = EditText

            saveData(data)
            print(f"Task updated: '{old}' → '{EditText}'")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

while True:
    print("\n1. Add new task")
    print("2. Show all tasks")
    print("3. Edit tasks")
    print("4. Delete a task")
    print("5. Show stats")
    print("6. Filter ")
    print("7. Exit")

    choice = input("Choose an option: ")




    if choice == "1":
        task = input("Enter your task: ")
        category = input("Enter your category: ")
        addEntry(task,category)
    elif choice == "2":
        showEntry()
    elif choice == "3":
        editTasks()
    elif choice == "4":
        deleteEntry()
    elif choice == "5":
        stats()
    elif choice == "6":
        print("\n1. Filter by date")
        print("2. Filter by category")
        select=input('Choose your type of filter: ')


        if select=='1':
            inputDate = input("Enter the date of your task: ")
            filterbydate(inputDate)
        elif select=='2':
            inputCategory = input("Enter the category of your task: ")
            filterbycategory(inputCategory)


    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")

