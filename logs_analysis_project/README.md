# Logs Analysis Project

### Modules
The modules included in this project are:
* log_analysis.py

### Description:
This project was developed in Python 3.  It is a server log analysis tool that connects to
a PostgreSQL database and executes three queries. The query results are written to a plain text file called 'output.txt'.  Queries can be added or modified in the project using Python code.  The project
is provided as part of the Udacity Full Stack Developer Nanodegree.

* The project sets up a mock PostgreSQL database for a fictional news website.  The Python script uses
psycopg2 to query the database and generate output that answers the following three questions.
  1.  What is the most popular article on the site?
  2.  Who are the most popular article authors?
  3.  On which days did more than 1% of the requests lead to errors?

### Requirements
In order to use this program, users will need to install a Linux VM with Vagrant:
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

### Running:
The code cannot be run without the associated database.
* Creating the database:
  * if you use the Vagrantfile supplied by Udacity, this step is automated, otherwise
  * manually create the news database using SQL.  The following link provides the SQL file needed to recreate the database.  [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).  To setup the news database you will need to unzip this file and follow the steps below.
  1.  from the command line, 'cd' into the vagrant directory.
  2.  run the 'psql' command
  *  `psql -d news -f newsdata.sql`
  this command will connect to your database server and create the tables and data.
  * To learn more about how to use the psql command line interface see the [Postgres Guide](http://postgresguide.com/utilities/psql.html).


### Author:
Jon Lunsford, March 18, 2018