# Pydantic Examples and Concepts

This repository demonstrates various features and best practices of the Pydantic library in Python, including field validation, model validation, computed fields, serialization, and more. Each file focuses on a specific concept with clear code and comments.

## Files Overview

- **pydantic_2.py**
  - Shows how to define a Pydantic model using `Annotated` for type hints and field validation/metadata.
  - Demonstrates strict type enforcement, optional fields, and custom validation rules.

- **field_validator.py**
  - Demonstrates the use of `@field_validator` to add custom validation logic for individual fields.
  - Includes examples of domain-specific email validation, name transformation, and age range enforcement.

- **model_validator.py**
  - Shows how to use `@model_validator` for cross-field or model-level validation.
  - Example: Ensures an emergency contact is present for patients above 60 years old.

- **computed_field.py**
  - Explains and demonstrates computed fields using the `@computed_field` decorator.
  - Example: Calculates BMI dynamically from other model fields.

- **serialization.py**
  - Provides an overview and examples of serializing Pydantic models to dictionaries and JSON.
  - Shows how to deserialize data back into Pydantic models.

- **nested_models.py**
  - (If present) Demonstrates how to use nested Pydantic models for complex data structures.

## Requirements

- Python 3.8+
- Pydantic v2+

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage

Each file can be run independently to see the concept in action:
```bash
python <filename>.py
```

## References
- [Pydantic Documentation](https://docs.pydantic.dev/)

---
Feel free to explore each file for detailed code examples and comments explaining the concepts!
