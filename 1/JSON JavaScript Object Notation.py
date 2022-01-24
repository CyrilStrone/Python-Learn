import json
a = {
"firstName": "Jane",
"lastName": "Doe",
"hobbies": ["running", "sky diving", "singing"],
"age": 35,
"children": [
{
"firstName": "Alice",
"age": 6
},
{
"firstName": "Bob",
"age": 8
}
]
}
with open("data_file.json", "w") as write_file:
    json.dump(a, write_file)
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)