from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # Model validator: Used to validate the entire model after all fields are populated and validated.
    # Here, it ensures that if the patient's age is above 60, an 'emergency' contact must be present in contact_details.
    # model_validator with mode='after' runs after all field validators and type coercion are complete.
    @model_validator(mode='after')
    def validate_emergency_contact(cls , model):
        if model.age >60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years of age')
        return model
    # Model validators are useful for cross-field validation and logic that depends on multiple fields.
    # The default mode is 'before', but 'after' is used here to access the fully constructed model instance.
    
    
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)



# field validators are used in two modes -- before and after
# before: used to validate and transform the value before it is assigned to the field
# after: used to validate the value after it has been assigned to the field
# mode='before' is the default mode