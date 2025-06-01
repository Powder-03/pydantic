from pydantic import BaseModel, Field , EmailStr , AnyUrl
from typing import Optional , Dict ,List , Annotated

class Patient(BaseModel):
    name: Annotated[
        str,
        Field(min_length=1, max_length=100, title='Name of the patient', description="Name must be between 1 and 100 characters")
    ]
    email: Annotated[
        EmailStr,
        Field(description="Valid email address of the patient")
    ]
    linked_in: Annotated[
        Optional[AnyUrl],
        Field(default=None, description="LinkedIn profile URL")
    ]
    age: Annotated[
        int,
        Field(ge=0, description="Age must be a non-negative integer")
    ]
    weight: Annotated[
        float,
        Field(gt=0, description="Weight must be a positive float", strict=True)
    ]
    married: Annotated[
        Optional[bool],
        Field(default=None, description="Marital status of the patient")
    ]
    allergies: Annotated[
        Optional[List[str]],
        Field(default=None, max_length=5, description="List of allergies (max 5)")
    ]
    contact_details: Annotated[
        Dict[str, str],
        Field(description="Contact details as a dictionary")
    ]
    # All fields now use Annotated for type and validation/metadata. 'weight' uses strict=True.
    
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


# Strict=True in Field ensures that the value must be exactly of the specified type (float in this case), not just a subtype or convertible type.
# This is particularly useful for numeric types where you want to enforce strict type checking.




