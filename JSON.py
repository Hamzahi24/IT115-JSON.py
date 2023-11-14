#Import the class library Json
import json


#Create the data dictionary.

data = {
    
    'name':'Hamzah',
    'age':30,
    'city':'Washington,WA',
    'interests':['basketbal','Gym','Gaming'],
    'is_student':True

}
#Use the with statement to open data.jason as a json_file
with open('data.json', 'w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')


#Use the with statement to open data.jason as a json_file
with open('data.json','r') as json_file:
    
    loaded_data = json.load(json_file)
    
print('Sucessfully able to read data.json')
print(loaded_data)

#Modify the loaded_data in json file
loaded_data['age'] = 34 
loaded_data['interests'].append('Sports')

#Modify the json file
with open('data.json', 'w') as json_file:

    json.dump(loaded_data, json_file, indent=4)

print('Modified data written to data.json')
