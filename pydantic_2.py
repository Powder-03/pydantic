from pydantic import BaseModel, Field , EmailStr , AnyUrl
from typing import Optional , Dict ,List , Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(min_length=1, max_length=100, title = 'Name of the patient' , description="Name must be between 1 and 100 characters")]
    email :EmailStr  # EmailStr is a Pydantic type that validates email addresses.
    linked_in : Optional[AnyUrl] = None  # AnyUrl is a Pydantic type that validates URLs. Optional allows the field to be omitted.
    age : int = Field(..., ge=0, description="Age must be a non-negative integer")
    weight: float = Field(..., gt=0, description="Weight must be a positive float")
    married: Annotated[bool , field(default = None)] # Default value is False, indicating the patient is not married.
    allergies:Annotated[Optional[List[str]] , Field(default=None , max_length=5)] # Optional allows the field to be omitted, and None is the default value.
    
    # we need to give default field value for optional fields.
    contact_details : Dict[str , str]
    
    # The Field function allows you to add metadata to the field, such as validation rules and descriptions.
    
    
def insert_patient_data(patient:Patient):
    
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    # Here, we are using the Pydantic model to validate and insert patient data.
    
    print("Patient data inserted successfully.")
    
    

    
    
patient_info = {
    "name": "Rishabh",
    "email": "abc@gmail.com",
    "linked_in": "https://www.linkedin.com/in/rishabh",
    "age": 21 , 
    "weight": 70.5,
    "allergies": ["penicillin", "nuts"],
    "contact_details": {
        "email": "abc@gmail.com",
        "phone": "123-456-7890"
        }
    
    # If we try to pass a negative age or a non-integer value, Pydantic will raise a validation error.
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# Pydantic will automatically validate the data types and raise errors if they do not match the expected types.
# if we give age as a string or negative value, it will raise a validation error.

#Field provides two things ---custom validation and and option to attach metadata.
# Annotated is used to add metadata to the field, such as validation rules and descriptions.
# Annotated is the new, recommended way (especially in Pydantic v2+) to attach extra metadata (like Field) to a type hint.
#It separates the type (str) from the metadata (Field(...)), making type hints clearer and more compatible with static type checkers and other tools.
#It allows you to attach multiple pieces of metadata to a single type.




