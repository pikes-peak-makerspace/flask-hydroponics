# How to run this program

Once you have the code in a folder, make sure to be in that folder and do the following:

## Create a virtual enviroment

```
$ python3 -m venv venv
```

## Activate the virtual enviroment

```
$ source venv/bin/activate
```

## Once activated, install the requirements.txt file

```
(venv) $ pip install -r requirements.txt
```

## Now, run flask

```
(venv) $ flask run
```

## Access flask from anywhere on network (default port is 5000)
Optionally set port as well.

```
(venv) $ flask run --host=0.0.0.0 --port=5001
```

## Stop the server with

ctrl + c

## Optionally, run flask in debug mode
Use 'set' not 'export' if on Windows.

```
(venv) $ export FLASK_DEBUG=1
```

