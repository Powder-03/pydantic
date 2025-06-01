# Serialization in Pydantic
# ------------------------
# Serialization is the process of converting a Pydantic model (or its data) into a format that can be easily stored or transmitted,
# such as a dictionary or JSON string. This is useful for saving data to files, sending data over a network, or interacting with APIs.
#
# Pydantic provides built-in methods for serialization:
#   - model.dict() or model.model_dump(): Converts the model to a Python dictionary.
#   - model.json() or model.model_dump_json(): Converts the model to a JSON string.
#
# Example:
# --------
# from pydantic import BaseModel
#
# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#
# user = User(id=1, name='Alice', email='alice@example.com')
#
# # Serialize to dict
# user_dict = user.model_dump()  # or user.dict() in Pydantic v1
# print(user_dict)
# # Output: {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'}
#
# # Serialize to JSON
# user_json = user.model_dump_json()  # or user.json() in Pydantic v1
# print(user_json)
# # Output: '{"id": 1, "name": "Alice", "email": "alice@example.com"}'
#
# You can also control which fields are included/excluded, handle aliases, and more using arguments to these methods.
#
# Deserialization is the reverse process: creating a Pydantic model from a dict or JSON string.
#
# Example:
# user2 = User.model_validate({'id': 2, 'name': 'Bob', 'email': 'bob@example.com'})
# print(user2)
# # Output: id=2 name='Bob' email='bob@example.com'


from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male' #default value
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True) #existing pydantic object ko python dict mein convert karna
# temp = patient1.model_dump_json(exclude_unset=True) #existing pydantic object ko json mein convert karna

print(temp)
print(type(temp))