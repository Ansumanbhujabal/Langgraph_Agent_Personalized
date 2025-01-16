from langgraph.prebuilt import ToolExecutor
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
import warnings
warnings.filterwarnings("ignore")

class MultiplierInput(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")


def multiply(a: int, b: int) -> int:
    return a * b


multiplier = StructuredTool.from_function(
    func=multiply,
    name="Multiplier",
    description="Multiply two numbers",
    args_schema=MultiplierInput,
    return_direct=False,
)

class AdderInput(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")


def add(a: int, b: int) -> int:
    return a + b


adder = StructuredTool.from_function(
    func=add,
    name="Adder",
    description="Add two numbers",
    args_schema=AdderInput,
    return_direct=False,
)

tools = [multiplier, adder]
tool_executor = ToolExecutor(tools)