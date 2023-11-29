# displaycolor.py

This readme will guide you through running the attached displaycolor.py script. This guide assumes you understand the basics of Python and programming in general; otherwise, it's wise to ignore this section of the respository.

### 1. Install needed software
This project was made with [**Python 2.11.6**](https://www.python.org/downloads/) and [**VS Code**](https://code.visualstudio.com/). Python is *required* while VS Code is *optional*. For a gude on installing python, see the following;

- [Windows](https://learn.microsoft.com/en-us/windows/python/beginners)
- [Mac OS](https://docs.python.org/3/using/mac.html)
- [Linux (Ubuntu)](https://www.knowledgehut.com/blog/data-science/install-python-on-ubuntu)

### 2. Create a Virtual Environment
Open your command line interface (Terminal on macOS/Linux, Command Prompt or PowerShell on Windows).

- **Navigate to the project directory** and enter the colors folder.
    - `cd 'directory here'`
- Once in the project directory, **create a virtual environment**.

```bash
python -m venv env
```
### 3. Activate the virtual environment
Before you can actually use the virtual environment, it must first by activated.
- **On Windows** (Command Prompt): `env\Scripts\activate`
- **On Windows** (Powershell): `.\myenv\Scripts\Activate.ps1`
- **On macOS/Linux** (BASH): `source env/bin/activate` 

### 4. Install dependencies
This project has dependencies which are listed in [py-requirements.txt](./py-requirements.txt). 

You can install dependencies by running:
```py
pip install -r py-requirements.txt
```

### 5. Running the script

You can run the script by running:
```py
python displaycolor.py
```

Once you're done, you can deactivate the virtual environment by simply running:
```
deactivate
```