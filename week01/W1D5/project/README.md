# Evaluation Assignment

## Basic Overview

Upload a locally stored excel file to a flask webserver using http, and subsequently parse it
using a set of rules specified below. The output of the parser should be stored in a mysql database.
Implement logging on the flask server, and also run basic SQL commands using a mysql client to explore
the data you stored in the database.

## Flask Client

Write a browser based client that allows a user to upload .xlsx files to a flask webserver.

## Flask Webserver

Write a python program to spin up a flask webserver. The flask webserver should implement at least one
http method (using a decorator) 

- Firstly, to save an uploaded excel file to a designated upload folder in a file system accessible to the webserver.
- Secondly, to parse the file, and generate output. The parse logic is described below.
- Thirdly to store the output in a table in mysql.

For any of the above processing:

- log the normal status or an error message if an error occurs, using a logger to a log file
- the flask webserver will log any such messages to a logfile on the server side
- move the file to a designated "error" folder if an error occurs, or move it to a designated "archive" folder if processing succeeds
- return an appropriate http code to the client that reflects the success/failure

There are more details specified in the work item processing job status section below in this document.


## Specific Excel File Parser

As mentioned above, the http method you implement in the flask webserver, will attempt to parse the excel file after it saves it to a folder on the server side. Here are some details on how you need to implement this parser:

1. Please import csv (or) openpyxl & Logging packages for this parsing problem.
2. The parser should attempt to parse the file that was just uploaded.
3. Write code to infer the month and year from the file name. For eg if the file name is expedia_report_monthly_january_2018.xlsx, then the month is "january" and the year is "2018". Feel free to use any fuzzy logic, as the naming conventions are intentionally inconsistent.
4. Based on the month and year inferred above, the parser generates output in a specific format outlined below after it parses the data in the first and second tab of the excel sheet.

### Output 1
For instance, in the above scenario, based on the data in the first tab of the above file, the output for "january 2018" needs to look like the following:

```
Calls Offered: 16,915
Abandon after 30s : 2.32%
FCR : 86.50%
DSAT :  14.20%
CSAT : 78.30%
```

### Possible Output 2

The second tab which is "VOC Rolling MoM" you need to grab all the values related to Jan-18 in the "Net Promoter Score" column of the sheet, and print "good" or "bad" depending upon the below specified rules:

```
Promoters > 200 : good              Promoters <200 : bad
Passives > 100 : good               Passives <100 : bad
Dectractors > 100 : good            Dectractors <100 : bad
```

A typical output can look like below:

```
Promoters: good
Passives: bad
Dectractors: good
```

The above values are not necessarily correct and simply provided as an example, and you will need to apply the rules mentioned above in order to determine the correct output.


## Database Schema Design

You will need to look at the output logged in the above section, to design your own custom database schema to store the output in a specific schema corresponding to the file you parsed. Be prepared to run a few SQL queries to read the data from the database, so you can verify that the data stored in the database is as you expect.

## Work Item Processing Job Status

Client folder: For this assignment, there are two files that are included in your client folder that a browser can access, but there could be numerous:

```
 expedia_report_monthly_january_2018.xlsx
 expedia_report_monthly_march_2018.xlsx
```

There are no sub-folders and the files are not recursively stored.

Server folder: A file list should be created, which keeps track of all the filenames which have been processed. This file list should be persisted in a file called processed.lst in a filesystem accessible to the flask webserver.

- Files which are processed, should not be processed again even if the user attempts to upload them.
- You can assume that files with the same name on the client will not be updated locally once they are created with initial content.
- Newly uploaded files are not saved by flask to the file system.
- Files once processed in the upload directory should be moved to an archive directory once they are successfully processed.
- Error checks on the file:


```
In case if the file name appears invalid (or the month and year cannot be inferred easily from the file name), the file needs to be moved to a designated "error" folder, and you need to log an appropriate message in the log file, using the python logger.

If any of the spreadsheet tabs are missing, then the file is invalid and should be moved to the "error" folder.
```

## Installation

Set up environment

```
source venv/bin/activate or .
\venv\Scripts\activate

pip install -r requirements.txt

python run.py
```

## Usage


## Support

lynda.foster@smoothstack.com

## Optimizations

## Contributing

This repo is not open to contributions
