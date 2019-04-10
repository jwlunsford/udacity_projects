# Tree Catalog
Welcome to the Github page for the Tree Catalog application.  This is a simple web application that demonstrates the power of Flask and it's associated libraries.  This application was created for learning purposes as a requirement for the **_Full Stack Nanodegree Course_** at Udacity.

## Requirements
The Tree Catalog Application was created using the most recent version of the libraries listed below.  These components should be installed on your system prior to running the web application.
* Python 3.x
* flask
* flask_bootstrap4
* flask_wtf
* sqlalchemy
* oauth2client
* httplib
* json
* requests

## Installation and Flask Startup
My recommendation is to install all of the required components within a Virtual Environment as described in [this article](https://docs.python-guide.org/dev/virtualenvs/).  This will keep all the required packages organized under the same environment, using a simple and easy format.

After the required dependencies are installed, run the web application using Flask.  The following steps will explain how to create a local copy of the code and run Flask.

1.  Download and unzip (or Clone) the contents of this repository using Github or Git commands from the Terminal or shell.
2.  Navigate to the root directory (item_catalog) where the files have been copied using a Terminal (i.e.; shell prompt).  The command `dir` on windows or `cd` on OSX and Linux, are used to navigate to the directory.  For example, using Mac OSX Terminal, you would type `cd /path/to/directory/here` to navigate to the local files.
3.  Run the Flask server by typing the following into the Terminal (i.e.; shell) window. `$ python main.py`
If everything was installed correctly, this will start the Flask Application running in the background on port 5000.

## Usage
* When the Flask Server is running in the background, open a Browser and type `localhost:5000` into the address bar and press Enter.   This should bring up Tree Catalog landing page in the Browser.   From the landing page, click the Navigation links to view trees by Category (Deciduous and Evergreen).
* Login is required to make changes to the underlying data (Create, Update or Delete Trees).  The Web Application uses a Google account to log users in.  Users without a Google account will need to create one to access this functionality in the application.
* NOTE:  Trees for each category may be viewed without logging in to the application.

## License Info
The Tree Catalog Application is provided under the [MIT License](https://choosealicense.com/licenses/mit/), which means it is provided "AS IS" and may be used for any purpose as long as attribution is given.

## Created By:
* Created By: Jon Lunsford
* Date: April 9, 2019
* License: MIT
