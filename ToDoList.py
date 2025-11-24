import json
from datetime import datetime

# CategoryList = ['anime', 'game', 'movie', 'work']


def loadData():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def categoryDataLoad():
    try:
        with open('Category.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def categoryDataSave(category):
    with open('Category.json', 'w', encoding='utf-8') as f:
        json.dump(category, f, ensure_ascii=False, indent=4)

def addCategory(categoryList):
    categoryData = categoryDataLoad()
    catEntry=categoryList
    categoryData.append(catEntry)
    categoryDataSave(categoryData)


def saveData(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def addEntry(task,Categoryselect):
    data = loadData()
    CategoryData = categoryDataLoad()
    entry = {
        'task': task,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'category': CategoryData[Categoryselect-1]

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

def showCategories():
    catData = categoryDataLoad()
    for i, c in enumerate(catData,1):
        print(f'{i}.{c}')


def editTasksAndCategory():
    data = loadData()
    catData = categoryDataLoad()
    if not data:
        print("No tasks to Edit!")
        return
    showEntry()
    try:
        choice = int(input("Enter the number of the task to Edit: "))
        if 1 <= choice <= len(data):
            changed = data[choice - 1]

            print('\n1.Cahnge the Task')
            print('2.Cange the Category')
            print('3.Add new Category')
            selectSection=input('What would you like to do?')


            if selectSection=='1':
                EditText=input("Enter the new text: ")
                old=changed['task']
                changed['task'] = EditText
                saveData(data)
                print(f"Task updated: '{old}' → '{EditText}'")
            elif selectSection=='2':
                showCategories()
                EditCategory=int(input("Enter the new number of category: "))
                old=changed['category']
                changed['category'] = catData[EditCategory-1]
                saveData(data)
                print(f'Category updated: {old} → {catData[EditCategory-1]}')
            elif selectSection=='3':
                # categoryData=categoryDataLoad()
                categoryList=input("Enter the new category: ")
                addCategory(categoryList)
                print('Category added successfully!')

        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")





while True:
    print("\n1. Add new task")
    print("2. Show all tasks")
    print("3. Edit task / category")
    print("4. Delete a task")
    print("5. Show stats")
    print("6. Filter ")
    print("7. Exit")

    choice = input("Choose an option: ")


    if choice == "1":
        task = input("Enter your task: ")
        categoryData = categoryDataLoad()


        showCategories()

        # categoryData=categoryDataLoad()

        while True:
            try:
                Categoryselect = int(input("Enter your number of category: "))
                if 1 <= Categoryselect <= len(categoryData):
                    break
                else:
                    print("❌ Invalid number, try again.")
            except ValueError:
                print("❌ Please enter a number!")

        addEntry(task, Categoryselect)


    elif choice == "2":
        showEntry()
    elif choice == "3":
        editTasksAndCategory()
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

