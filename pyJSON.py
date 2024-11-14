#imports the JSON library to work with JSON data formats
import json

#creating a json dictionary
data = {
    "name": "Varvara",
    "age": 30,
    "city": "Seattle, WA",
    "interests": ["Traveling", "Football", "Cooking", "History"],
    "is_student": True
}

#creating a file to store our data
with open("data.json", "w") as json_file:
    # Import that data dictionary into a new file
    json.dump(data, json_file, indent=4)

print("You have successfully written to data.json")



#opens data.json in read mode
with open("data.json", "r") as json_file:  
    #loads JSON data from file into a Python dictionary
    loaded_data = json.load(json_file)  

print("Sucessfully able to read data.json:")
#outputs the contents of loaded_data to verify the contents of data.json
print(loaded_data)


#modifies a data in an array
loaded_data["age"]=11
loaded_data["interests"].append("Jumping")
loaded_data["interests"].append("New")



#creating a file to store our data
with open("data.json", "w") as json_file:
    #import that data dictionary into a new file
    json.dump(loaded_data, json_file, indent=4)
print("You have successfully modified a data.json:")   
print(loaded_data)