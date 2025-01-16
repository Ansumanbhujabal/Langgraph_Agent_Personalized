from pydantic import BaseModel, Field
import warnings
warnings.filterwarnings("ignore")

class Response(BaseModel):
    """Final answer to the user"""

    result: int = Field(description="the result of the computation")
    explanation: str = Field(
        description="Always start the answer with a warm greetings to the user mentioning all the details you have found about him from the auery .explanation of the steps taken to get the result"
    )
