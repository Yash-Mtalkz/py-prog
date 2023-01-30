import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://yash-mtalkz:12345@cluster0.xhm9l9v.mongodb.net/?retryWrites=true&w=majority")
project = client["StockWatcher"]
mycol = project["Stocks"]
# code for manual addition of fields
'''mydoc = [{
    'name': 'Prashant',
    'Project': 'Admin Page',
    'Coworker': 5,
    'Deadline in days': '7 days'
},
    {
    'name': 'Arpit',
    'Project': 'Front end',
    'Coworker': 7,
    'Deadline in days': '5 days'
},
    {
    'name': 'Ajay',
    'Project': 'Front end',
    'Coworker': 7,
    'Deadline in days': '5 days',
    'Cohead': 'manas'
}]
x = mycol.insert_many(mydoc)'''

# code for taking fields as input from the user
'''mymultpledoc = []
n = int(input())

for i in range(n):
    mydoc = {}

    category1 = "Name"
    Name = input("Enter name of person : ")
    mydoc[category1] = Name

    category2 = "Project : "
    Project = input("Enter the project allocated : ")
    mydoc[category2] = Project

    category3 = "Coworker : "
    Coworker = input("Enter the Coworker in number working along with : ")
    mydoc[category3] = Coworker

    category4 = "Deadline in days : "
    deadline = input("Enter deadline in days : ")
    mydoc[category4] = deadline

    mymultpledoc.append(mydoc)

x = mycol.insert_many(mymultpledoc)'''

'''query = {"name": "Prashant"}
print(mycol.find_one(query))  # single query
query = {"Coworker": "7"}
print(mycol.find(query))  # multiple queries'''
query = {"name": "Prashant"}
# Updates the db  mycol.find_one_and_update((query), {'$set': {"name": "gautam"}})
mycol.delete_one(query)
