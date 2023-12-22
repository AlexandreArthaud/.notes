# Python

```aln
# Syntax
## Lists
Syntax to get a subset of a "list" or string, up to the "x"th element : list[:x]
Syntax for a try catch block in Python, capturing a generic "exception" and logging it : try: ... except Exception as exception: print(exception)

# Standard Library
## Functions
Standard Library Function to print any "expression" to the console : print(expression)
Standard Library Function to get a [type] which corresponds to the type of an "expression" (usually there is no need to store the returned value, just to display it to check out which type the expression is) : type(expression)
Standrd Library Function to return the [int] count the number of elements in a "list" or string (counting letters, not bytes, so a Chinese character is just one letter) : len(list)
## Modules
Standard Library Python module that provides high-level interface to display web-based documents : webbrowser
  "webbrowser" module function to display a [string] "url" using the system default web browser : webbrowser.open(url) 

# Third Party Modules
Python module to send HTTP requests (can be installed with pip) : requests
  <requests> function to send a HTTP request to a [string]url and get a [requests.models.Response]response : response = requests.get(url)
    [requests.model.Response]response attribute which contains the [int] status code of the response : response.status_code
    [requests.model.Response]response attribute which contains the [string] text response of the request : response.text
    [requests.model.Response]response method which raises an exception if the request failed (often used in try block before continuing working on response) : response.raise_for_status()
    [INT] from <requests> corresponding to the 'ok' status code for a request (usually 200), often used to compare with a response status code : requests.codes.ok
```