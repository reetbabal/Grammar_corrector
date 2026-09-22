from pydantic import BaseModel,Field,field_validator

from typing import Annotated

class Data(BaseModel):
    text: Annotated[str,Field(...,description = 'enter the text which you want to be grammatically correct.')]

    @field_validator('text')
    @classmethod
    def valid(cls,value):
        value = value.strip()
        if len(value)>1000:
            raise ValueError('Please enter the text in small amount.Maximum allowed length of text is 1000. ')
        if len(value)<3:
            raise ValueError('Please enter a large sentence so that I can correct it grammatically.')
        has_alphabet = any(char.isalpha() for char in value)
        if not has_alphabet:
            raise ValueError('Please enter a sentence with enough content for grammar correction.')
            
        return value

