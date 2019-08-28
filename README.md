# MetaSearchEngine
This Meta Search Engine is a demonstrator which scrapes information from the [Expertenservice of the University of Hamburg](https://www.uni-hamburg.de/newsroom/presse/expertenservice.html) using the following tech stack: 

- Python, an interpreted, high-level, general-purpose programming language
- Python virtual environments
- Selenium, a webtesting framework
- Flask, a micro webframework written in Python 
- Bootstrap, a CSS framework 

## Executing this project 

1. Clone this repository 
2. Install required environment
3. Run virtual environement 
4. Run application with `flask run`
5. Navigate to `localhost:5000` in the browser

### Setting up the virtual environment 

If you are using Python 3, virtual environment support is included. So in your application repository, run the command: 
```
$ python3 -m venv venv
```
In some operating systems you may need to use `python` instead of `python3`. 
With this command, Python runs the venv package, which creates a virtual environement named venv. The first venv is the name of the Python package, the second is the name that you are using for this particular environment.  

> If you are using any version of Python older than 3.4, virtual environments are not supported natively. Update your python version or use [Virtualenv](https://virtualenv.pypa.io/en/latest/) instead.

To activate your virtual environment, use the following commands
```
$ source venv/bin/activate
```` 
On Windows it looks like this: 
```
$ source venv\Scripts\activate
```

### Installing Flask and further packages

Python comes with a tool called `pip` which enables you to install packages from the Python Package Index (PyPI). 
> In Python 2.7 pip does not come bundled with Python and needs to be installed separately.

Install all packages by running the command: 

```
(venv) $ pip install requirements.txt
```

To seperately install the packages in the requirements.txt, run `pip install <packagename>`

For example, install flask by running the command: 

```
(venv) $ pip install flask
```

To see if Flask is installed either run the command `pip list` to see which packages have been installed or start the Python interpreter with `python` and importing flask by running `import flask`. If this does not provide you with an error, your flask installation was successful. 