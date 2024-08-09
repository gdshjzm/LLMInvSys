# LLMInvSys
## Usage
This document includes a calculator interface that interacts with a Large Language Model (LLM) through a backend server to generate URLs. Users can input their requests into the prompt, which is then passed to the LLM. The LLM outputs a URL, which the user can then enter into a browser to view the results.

Part of this is related to Project 9, and the calculator's web interface is also associated with it.

## File Structure
```plaintext
/api-main
    /node_modules           -> Required libraries
        /express            
        /CORS
    /API_Documentation.md   -> API documentation (markdown version)
    /calculatorWeb.html     -> Calculator interface
    /package.json           -> Base package information
    /package-lock.json
    /Prompts.txt            -> Prompts for the LLM to generate URLs
    /readme.md              -> Readme file
    /script.js              -> Script connecting the frontend and backend
    /server.js              -> Backend server
```

## Installation
### Install node.js
You can go to the ![Nodejs](https://nodejs.org/en/) to install Node.js.
### Install Ollama (Optional, if you want automation)
You can go to ![Ollama](https://ollama.com) to install ollama.
#### Install llama3.1
After you installed the ollama, you're recommended to install llama3.1.
```bash
ollama run llama3.1
```
**Notice:** You need to make sure that you have the enough space for llama3.1--4.4GB.
### Install express
The server needs express.js to support the server running.
```bash
npm install express
```
### Run the code.
Keep your server listening on the port 7000.
```bash
node server.js
```
## Automation
to run the python scripts, ypu need to install such libraries.
```bash
pip install langchain
pip install langchain_community
pip install langchain_core
pip install requests
pip install webbrowser
```
Then you need to keep llama3.1 open in the backend
```bash
ollama run llama3.1
```
And just input your query to get answers!
