from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import webbrowser
import requests

def open_url_in_edge(url):
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    webbrowser.get('edge').open(url)

prompt = ChatPromptTemplate.from_template(
    '''
    Now,you are an althmetic calculator, you need to use an API to call the althmetic calculator.The API Documentation goes as follows:
    <Documents>
    # Math Operations API
    ## Summary
    A simple API for basic arithmetic operations and factorials.
    ## Endpoints
    ### Addition
    - **Endpoint**: `/add/:num1/:num2`
    - **Method**: `GET`
    - **Description**: Returns the sum of `num1` and `num2`.
    ### Subtraction
    - **Endpoint**: `/subtract/:num1/:num2`
    - **Method**: `GET`
    - **Description**: Returns the difference of `num1` and `num2`.
    ### Multiplication
    - **Endpoint**: `/multiply/:num1/:num2`
    - **Method**: `GET`
    - **Description**: Returns the product of `num1` and `num2`.
    ### Division
    - **Endpoint**: `/divide/:num1/:num2`
    - **Method**: `GET`
    - **Description**: Returns the quotient of `num1` divided by `num2`. Returns error on division by zero.
    ### Factorial
    - **Endpoint**: `/factorial/:num`
    - **Method**: `GET`
    - **Description**: Returns the factorial of a non-negative `num`. Returns error for negative input.
    ## Usage
    Use `curl` to make GET requests to the specified endpoints, e.g.:
    ```bash
    curl http://localhost:7000/add/5/3
    ```
    </Documents>
    <Requirements>
    1. You need to listen and understand about the user's input, whether it is a calculation or a practical problem.
    2. Then **ONLY** output the URL without any other words.
    3. If there are many steps of calculating, you should output the calculating URL in each step, use 'result' to represent the former result, and write each step line by line.
    </Requirements>
    <Userexample>
        ---
        'user':'I want to calculate 23 + 35.',
        'AI response':'http://localhost:7000/add/23/35',
        ---
        'user':'There are 10 rabbits in the forests, and the wolf have eaten three rabbits, then how many rabbits remained?',
        'AI response':'http://localhost:7000/subtract/10/3'
        ---
        'user':'Calculate(20-30)/5+4'
        'AI response':'http://localhost:7000/subtract/20/30
                       http://localhost:7000/division/result/5
                       http://localhost:7000/add/result/4'
        ---
    </Userexample>
    <UserInput>
    {UserInput}
    </UserInput>
    '''
)
output_parser = StrOutputParser()
model = Ollama(model='llama3.1:latest')
chain = (
        {"UserInput": RunnablePassthrough()}
        | prompt
        | model
        | output_parser
)

query = input('User:')
print('Llama3.1 is thinking...')
output = chain.invoke(query)
print('Going to ' + output + ' ...')
open_url_in_edge(output)
response = requests.get(output)

if response.status_code == 200:
    print('Calculation result is:',response.text)
else:
    print("Request Error,status code:", response.status_code)
