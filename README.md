# Requirements

To run this application, you'll need to have the following software installed on your system:

    Python 3.8 or later
    pip

# Installation

To install the dependencies for this application, follow these steps:

 1. Clone this repository to your local system
   ```
    git clone https://github.com/infnetdanpro/ChatGPT-flask-application
   ```
 2. Change into the directory of the cloned repository
    ```
    cd ChatGPT-flask-application
    ```
 3. Install the dependencies using pip
    ```
    pip install -r requirements.txt
    ```

# Running the Application
To run the application, use the following command:

```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
This will start the Flask development server, and you should be able to access the application in your web browser at http://localhost:5000.

# Running the Tests

To run the tests for this application, use the following command:

```
python -m unittest discover
```

This will run all the tests defined in the tests directory.
