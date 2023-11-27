# Python

## Virtual Environment

You can create a virtual environment with `python -m venv /path/to/virtual/environment`.

Then you have to enable the virtual environment. On Debian systems, you have to run
`source /virtual_environment_folder/bin/activate`.

## Requirements File

You can create a `requirements.txt` file in a Python project to list its dependencies. Each line
contains a dependency using the `package==version` format.

Once your file is ready, you can use `pip install -r requirements.txt` to install these dependencies
(preferably in a virtual environment).