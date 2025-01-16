# AI Agent Task: Langgraph Personalized

This project implements an AI-powered computation agent using LangChain and Groq APIs. The agent is designed to handle mathematical operations like addition and multiplication, with a structured execution flow managed through state graphs.



## Overview
This project uses LangChain, Groq APIs, and LangGraph to create a computation agent that processes user queries to perform arithmetic operations. The agent executes tasks using tools and a state graph for seamless execution and response generation.

---

## Features
- **Tool Integration**: Supports tools for addition and multiplication.
- **LLM Integration**: Leverages the `ChatGroq` model for natural language understanding and generation.
- **State Graph**: Uses LangGraph to define the execution flow.
- **Dynamic Responses**: Provides warm, user-friendly responses with explanations of the computations.

---

## Requirements
- Python 3.8+
- Libraries:
  - `langchain_groq`
  - `langgraph`
  - `python-dotenv`
  - `langsmith`
  - `grandalf`
- API Credentials for Groq and LangChain

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ansumanbhujabal/Langgraph_Agent_Personalized.git
   cd 
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API credentials (see [API Credentials Setup](#api-credentials-setup)).

---

## Usage
1. Open the directory.
2. Set the user query in the `inputs` dictionary, for example in `app.py` :
   ```python
   inputs = {
       "messages": [HumanMessage(content="User name - Subho, Age- 21, Home- India. What is sum of 45 and 2")]
   }
   ```
3. Run the script to execute the agent and view the results.
   ```python
   python3 app.py
   ```
---

## API Credentials Setup

This project uses `.env` files for secure storage of API keys. Add the following variables to your `.env` file:

```env
GROQ_API_KEY=<your_groq_api_key>
LANGCHAIN_ENDPOINT=<your_langchain_endpoint>
LANGCHAIN_API_KEY=<your_langchain_api_key>
LANGCHAIN_PROJECT=<your_langchain_project>
```


## Tools
1. **Adder**: Adds two integers.
   - Input Schema: `AdderInput(a: int, b: int)`
   - Description: Adds two numbers.

2. **Multiplier**: Multiplies two integers.
   - Input Schema: `MultiplierInput(a: int, b: int)`
   - Description: Multiplies two numbers.

---

## Agent and Graph Setup

The agent uses `ChatGroq` as the LLM and LangGraph for defining the execution flow:

1. **Nodes**:
   - `agent`: Calls the model to interpret user input.
   - `action`: Executes tools based on user queries.

2. **Graph Flow**:
   - Starts at `agent`.
   - Proceeds to `action` if a function call is needed.
   - Ends if no further actions are required.

---

## Execution Flow
1. Parse user input via `HumanMessage`.
2. Process the input using the LLM (`ChatGroq`).
3. Dynamically select and execute tools (`Adder` or `Multiplier`).
4. Return a user-friendly response with an explanation.

## Visualize Graph 
![image](https://github.com/user-attachments/assets/8fa67aa0-ce0a-440a-8662-fdf428bcf882)

## Visualize Langsmith Tool calls
![Screenshot from 2025-01-16 12-08-59](https://github.com/user-attachments/assets/a0b924f1-442f-4da7-825d-f162b95a549b)

---

## Output
The agent outputs a structured response including:
- **Result**: The computed value.
- **Explanation**: A user-friendly message with computation details and personalized greetings.

Example Output:
```
Hello Subho! I see you are 21 years old from India. The sum of 45 and 2 is 47. I used an addition tool to calculate this result.
```

---

## Visualize Output 

![Screenshot from 2025-01-16 12-19-01](https://github.com/user-attachments/assets/3072a662-b055-440a-9ab3-81a9fbcfc85f)

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

