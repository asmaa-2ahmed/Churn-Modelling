from pydantic import BaseModel, Field
from typing import Literal

class CustomerData(BaseModel):
    CreditScore: int = Field(description="Credit score of the customer.", ge=0, le=1000)
    Geography: Literal['France', 'Spain', 'Germany'] = Field(description="Country of residence.")
    Gender: Literal['Male', 'Female'] = Field(description="Gender of the customer.")
    Age: int = Field(description="Age of the customer.", ge=18)
    Balance: float = Field(description="Account balance of the customer.", ge=500.0)
    NumOfProducts: int = Field(description="Number of products the customer has with the bank.", ge=0)
    IsActiveMember: Literal[0, 1] = Field(description="Indicates if the customer is an active member (1 = Yes, 0 = No).")
