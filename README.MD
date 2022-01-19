## Introduction To Flask

**Flask** is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. **Flask** supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.

**Applications** that use the Flask framework are pinterest and LinkedIn. 

## Features of Flask Web Framework:

1. Development server and debugger.
2. Integrated support of unit testing.
3. RESTful Api.
4. Secure cookies.
5. Unicode-based.

## Example

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
	return "Hello World"

if __name__ == "__main__":
	app.run(debug=False)
```



## Start Learning Flask

1. Setup and workflow.
2. Get a basic app running.
3. Templates and static content.
4. Setting up and using Database.
5. Create a basic CRUD Application.
6. Deploy to Heroku.

### Setup And Workflow

**Installing Python and Visual Studio Code**

to begin with **flask,** We need few things to be installed on the computer. Firstly we python 3.8.x to be installed on the system and to do code we need a code editor  VS Code.

Follow this link to install Python : [https://www.tutorialspoint.com/how-to-install-python-in-windows](https://www.tutorialspoint.com/how-to-install-python-in-windows)

Follow this link to install VS Code : [https://code.visualstudio.com/download](https://code.visualstudio.com/download) and [https://code.visualstudio.com/learn/get-started/basics](https://code.visualstudio.com/learn/get-started/basics)~