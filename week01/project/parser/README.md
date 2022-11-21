# Evaluation Assignment

## Basic Overview

Upload a locally stored excel file to a flask webserver using http, and subsequently parse it
using a set of rules. The output of the parser should be stored in a mysql database.
Implement logging on the flask server, and also run basic SQL commands using a mysql client to explore the data you stored in the database. Requirements listed below.

## Solution

My data parsing logic is processed through 4 python modules: 

1. file_handler
    a. check_file - there are 3 quick checks in this file. 
        - checks that extension is .xlsx because openpyxl will not open excel files with other/older extensions. 
        - checks that name is at least 12 characters (3 for month, 4 for year, and 4 for extension)
        - checks that 
    b. read_file - reads excel file and raises an exception when teh workbook could not be loaded.
    c. archive_file - moves file to archived folder.
    d. error_file - moves file to the error folder. 
2. name_parser
    a. check_year - searches for a 4 digit number and retunrs the last 2 digits.
    b. check_month - searches for each 3 letter code within the file name and returns it if found.
    c. get_date - invokes the check_year and check_month methods and returns a list with year at index 0 and 3 letter month code at index 1.
3. worksheet_search
    a. find_row - parses search term in a row and returns row coordinate if found.
    b. find_column - parses search term in a column and returns column coordinate if found. 
4. record_parser
    a. summary_data - finds Summary worksheet and parses records for Summary Report.
    b. voc_data - parses voc_data and parses records for VOC Report.
    c. check_score - compares value foudn in Promoters, Passives, and Dectractors
        and returns whether the score is determined to be 'good' or 'bad'.

Other moduls:
1. app.py - routing logic for web pages
2. logging_handler - creates log file and stores all logging messages to desired format. 

I ran out of time before implemnting the database and batching a client folder. I mocked some code/pseudocode in the following modules for those requirements. 

3. client.py - draft logic for batching a client folder
4. models.py - database schema

## Optimizations

There are some fields I would have liked to use a config file for: file paths, environment variables, etc. I also wanted to do a similar thing with fixtures in my test code. I opted to spend more time increasing coverage.

There are many restrictions placed on data to be considered acceptable. There are some ways to allow for more types of files and data to be parsed. 

Next Steps:
    1. Refactoring, especially in test methods, i.e., add fixtures in conftest. 
    2. Create validation models to use pydantic and enforce class attribute datatypes.
    3. Use validation models to create dbModels (which inherits from the BaseModel class). Validator class methods helps validate the data. 
    4. Write the data to the database
    5. Implement a way for the user to fetch reports from the database (currently shows on web page at uplaod).
    6. Client folder batching (see client.py). 

## Requirements

### Flask Server

- [x] Firstly, to save an uploaded excel file to a designated upload folder in a file system accessible to the webserver.
- [x] Secondly, to parse the file, and generate output. The parse logic is described below.
- [ ] Thirdly to store the output in a table in sqlite.

For any of the above processing:

- [x]  log the normal status or an error message if an error occurs, using a logger to a log file
- [x]  the flask webserver will log any such messages to a logfile on the server side
- [x]  move the file to a designated "error" folder if an error occurs, or move it to a designated "archive" folder if processing succeeds
- [x]  return an appropriate http code to the client that reflects the success/failure

### Specific Excel File Parser

- [X] 1. Please import csv (or) openpyxl & Logging packages for this parsing problem.
- [X] 2. The parser should attempt to parse the file that was just uploaded.
- [X] 3. Write code to infer the month and year from the file name. For eg if the file name is expedia_report_monthly_january_2018.xlsx, then the month is "january" and the year is "2018". Feel free to use any fuzzy logic, as the naming conventions are intentionally inconsistent.
- [X] 4. Based on the month and year inferred above, the parser generates output in a specific format outlined below after it parses the data in the first and second tab of the excel sheet.

### Output 1

For instance, in the above scenario, based on the data in the first tab of the above file, the output for "january 2018" needs to look like the following:

```
Calls Offered : 16,915
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

- [ ] You will need to look at the output logged in the above section, to design your own custom database schema to store the output in a specific schema corresponding to the file you parsed. Be prepared to run a few SQL queries to read the data from the database, so you can verify that the data stored in the database is as you expect.

### Work Item Processing Job Status
- [ ] Client folder: For this assignment, there are two files that are included in your client folder that a browser can access, but there could be numerous:

```
 expedia_report_monthly_january_2018.xlsx
 expedia_report_monthly_march_2018.xlsx
```

- [x] Server folder: A file list should be created, which keeps track of all the filenames which have been processed. This file list should be persisted in a file called processed.lst in a filesystem accessible to the flask webserver.
- [x] Files which are processed, should not be processed again even if the user attempts to upload them.
- [x] You can assume that files with the same name on the client will not be updated locally once they are created with initial content.
- [x] Newly uploaded files are not saved by flask to the file system.
- [x] Files once processed in the upload directory should be moved to an archive directory once they are successfully processed.
- [x] Error checks on the file:
- [x] In case if the file name appears invalid (or the month and year cannot be inferred easily from the file name), the file needs to be moved to a designated "error" folder, and you need to log an appropriate message in the log file, using the python logger.
- [x] If any of the spreadsheet tabs are missing, then the file is invalid and should be moved to the "error" folder.