# Dynamo-Calculator
A simple industrial application to calculate the output of an engine using tkinter and pyodbc.

Calculates the output of an engine in "Horsepower(approximately 745.7 watts)" along with the correction factor, corrected-horsepower, top-speed, and power/weight-ratio.

The interface is designed using tkinter library for python while the connection to a simple Microsoft Access database is established using pyodbc.

Correction-factor is calculated using the SAE(Society of Automotive Engineers) and includes frictional loss using the formula:

![images](https://user-images.githubusercontent.com/112173249/186931113-14855aef-a69c-477c-b988-346596f02cbd.png)

## Interface:
![Screenshot](https://user-images.githubusercontent.com/112173249/186932190-d54cc001-c2b3-4f78-b7c2-916c0ed0e4d8.jpg)


## Dependencies:
1. tkinter (interface)
2. pyodbc (database connection and CRUD operations)
3. math (calculations)

## Instructions:
1. Unzip files to specific folder
2. Run the python file by double clicking or using your python editor

Note: The project expects the "images" and "Database1" file in "D:" address on lines(31,41,50,69). You can specify your custom paths using a python editor tool.
