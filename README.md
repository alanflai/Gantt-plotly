# Gannt chart with plotly
## Reference
This example is derived by the code from the following URL:

https://pythonandvba.com/blog/how-to-create-an-interactive-gantt-diagram-in-python-using-plotly-excel/

## Description

The data is coming directly from an Excel file. You can do all the changes in the excel file and after running the code again you will have your updated Gantt Diagram. The Gantt Chart is interactive and will be saved as an HTML file.


## How to package the project in a single executable file

Install the module pysinstaller to package the application into a single executable file with all its dependecies (python interpreter and python libraries listed in requirements.txt file).

`$ pip install pyinstaller` 

The command to builde the application's single executable file is

`$ pyinstaller --onefile -F .\gantt.py`

## Info and documentation Reference 

During the development of this project I have read and used informationa from the following
Internet blogs/site.

(1) Figure reference
URL: https://plotly.com/python/reference/index/

(2) Reference plotly.explore.scatter
URL: https://plotly.com/python/reference/scatter/

It contains ifnormation usefull fot scatter graph configurations as the marker formatting.

(3) Scatter markers configuration example
URL: https://plotly.com/python/marker-style/

(4) Text annotation
URL: https://plotly.com/python/text-and-annotations/

(5) Python command line example
URL: https://www.tutorialspoint.com/python/python_command_line_arguments.htm

(6) 10 minutes to pandas
URL: https://pandas.pydata.org/docs/user_guide/10min.html

## Points of attentions

1. Workraround for adding text annotation to a vertical line
   - convert the x value in milliseconds how described in this post 
     https://github.com/plotly/plotly.py/issues/3065

2. Date management
   
   - Assigned date as a string converterd in milliseconds
  
      - `date = datetime.datetime.strptime("2022-06-03", "%Y-%m-%d").timestamp() * 1000` 

   - Today date and time in milliseconds
  
      - `date = int(round(time.time()*1000))` 





