from pydantic import BaseModel , Field
from typing import Literal

class Customer_Data(BaseModel):
    CustomerId: int = Field(..., description="Unique identifier for each customer.")
    Surname: str = Field(..., description="Customer's surname.")
    CreditScore: int = Field(..., description="Credit score of the customer.", ge=0, le=1000)
    Geography: Literal['France', 'Spain', 'Germany'] = Field(..., description="Country of residence.")
    Gender: Literal['Male', 'Female'] = Field(..., description="Gender of the customer.")
    Age: int = Field(..., description="Age of the customer.", ge=0)
    Balance: float = Field(..., description="Account balance of the customer.", ge=0.0)
    NumOfProducts: int = Field(..., description="Number of products the customer has with the bank.", ge=0)
    IsActiveMember: Literal[0, 1] = Field(..., description="Indicates if the customer is an active member (1 = Yes, 0 = No).")
    Exited: Literal[0, 1] = Field(..., description="Indicates if the customer has churned (1 = Yes, 0 = No).")