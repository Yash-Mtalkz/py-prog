import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://yash-mtalkz:12345@cluster0.xhm9l9v.mongodb.net/?retryWrites=true&w=majority")
project = client["StockWatcher"]
mycol = project["Stocks"]
mydoc = [{
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
x = mycol.insert_many(mydoc)
