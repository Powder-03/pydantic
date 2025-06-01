# Computed Field in Pydantic
# ---------------------------
# A computed field is a property or method on a Pydantic model that is not directly set by the user,
# but is instead calculated from other fields in the model. Computed fields are useful for:
#   - Deriving values based on other model data
#   - Providing read-only properties
#   - Adding dynamic information to serialized output
#
# In Pydantic v2+, you can use the @computed_field decorator to mark a method as a computed field.
# This makes the field appear in the model's dict(), json(), and schema outputs.
#
# Example:
# --------
# from pydantic import BaseModel, computed_field
#
# class Rectangle(BaseModel):
#     width: float
#     height: float
#
#     @computed_field
#     @property
#     def area(self) -> float:
#         return self.width * self.height
#
# rect = Rectangle(width=3, height=4)
# print(rect.area)         # Output: 12.0
# print(rect.model_dump()) # Output includes 'area' as a field
#
# Computed fields are read-only and cannot be set by the user. They are always derived from other data in the model.


from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'height': 1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)