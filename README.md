# Gannt chart with plotly
## Reference
This example is derived by the code from the following URL:

https://pythonandvba.com/blog/how-to-create-an-interactive-gantt-diagram-in-python-using-plotly-excel/

## Description

The data is coming directly from an Excel file. You can do all the changes in the excel file and after running the code again you will have your updated Gantt Diagram. The Gantt Chart is interactive and will be saved as an HTML file.

## Points of attentions

1. Workraround for adding text annotation to a vertical line
   - convert the x value in milliseconds how described in this post 
     https://github.com/plotly/plotly.py/issues/3065

2. Date management
   
   - Assigned date as a string converterd in milliseconds
  
      - `date = datetime.datetime.strptime("2022-06-03", "%Y-%m-%d").timestamp() * 1000` 

   - Today date and time in milliseconds
  
      - `date = int(round(time.time()*1000))` 





