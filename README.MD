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