from pydantic import BaseModel, field_validator
import re


# Input schema for creating new user
class CreateUserSchema(BaseModel):
    name: str
    email: str
    password: str

    # Name validator
    @field_validator("name")
    def validate_name(cls, value):
        if value == "":
            raise ValueError("Name is required.")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        return value

    # Email validator
    @field_validator("email")
    def validate_email(cls, value):
        if value == "":
            raise ValueError("Email is required.")
        # Regex for validating email
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, value):
            raise ValueError("An email address must have an @-sign.")
        return value

    # Password validator
    @field_validator("password")
    def validate_password(cls, value):
        if value == "":
            raise ValueError("Password is required.")
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters.")
        return value


# Input schema for updating user
class UpdateUserSchema(BaseModel):
    name: str
    email: str

    # Name validator
    @field_validator("name")
    def validate_name(cls, value):
        if value == "":
            raise ValueError("Name is required.")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        return value

    # Email validator
    @field_validator("email")
    def validate_email(cls, value):
        if value == "":
            raise ValueError("Email is required.")
        # Regex for validating email
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, value):
            raise ValueError("An email address must have an @-sign.")
        return value


# Output schema for user
class ReadUserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
