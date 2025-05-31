#type hinting of python is not that strong.

def insert_patient_data(name:str , age:int):
    
    if type(name ==str and type(age) == int):
        print(name)
        print(age)
        
    else:
        raise TypeError("Name must be a string and age must be an integer")
    
insert_patient_data("Rishabh", 21)
    
    
 # this is a way to enforce type checking in python but it is not a scalable method.
# Pydantic is a library that provides data validation and settings management using Python type annotations.

def update_patient_data(name:str , age:int):
    
    
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age cannot be negative")
        print(name)
        print(age)
        
    else:
        raise TypeError("Name must be a string and age must be an integer")
    
update_patient_data("Rishabh", 22)   

# there in no data validation in python by default so to achieve this we can use pydantic library.
# Pydantic allows you to define data models with type annotations and automatically validates the data against these models.
# It also provides features like serialization, deserialization, and data parsing. like giving negative values for age. but it will be managed by pydantic