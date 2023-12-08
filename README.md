# Information retrieval

## Starting the application

### First time setup

Before starting the application we advise the creation of a python virtual env, done with the following command
``` bash
python3 -m venv venv
```
This will create a virtual environment called venv in which we are going to install all the required modules with the command.

``` bash
source venv/bin/activate
pip install -r requirements.in
```

This is the setup needed for the backend. In another terminal we are going to setup the frontend. This is done in the following way.
``` bash
cd web-app/src
npm install
```
This will install all of the node.js module needed for our project.

### After first setup start

To start the application we are going to need two terminals the first for the backend must run 
``` bash
source venv/bin/activate
python3 main.py
```
The frontend must run:
``` bash
cd web-app/src
npm run dev
```
This will boot the application and make it available in local
