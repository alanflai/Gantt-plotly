
import plotly.express as px
import plotly
import pandas as pd
import datetime, time
import sys, getopt, os

#import plotly.figure_factory as ff

INPUT_FILE = "plan0.xlsx"
OUTPUT_FILE = "gantt-plan0.html"
PRJ_NAME = "Gantt chart of XXX project"
TEXT_FONT_SIZE = 12

# Tool Function: Convert RGB to int
def rgb2int(rgb_tuple):
        val = rgb_tuple[0] << 16 | rgb_tuple[1] << 8 | rgb_tuple[2] 
        return val
# Tool Function: Get file name without extension from a path
def get_filename_only(arg):
       if type(arg) != str:
               return "output"
       return os.path.splitext(os.path.basename(arg))[0]


def create_gantt(prj_name,df, output_file):

        # Create the status column as a result of 'Complete in %' values range
        df.loc[df['Complete in %'] == 100, 'Status'] = 'Completed'
        df.loc[df['Complete in %'].between(1,99), 'Status'] = 'Working'
        df.loc[df['Complete in %'] == 0, 'Status'] =  'Planned'

        # Milestone series
        ml_completed = df.loc[(df['Duration'] == 0) & (df['Status']=='Completed') ] 
        ml_working = df.loc[(df['Duration'] == 0) & (df['Status']=='Working') ]
        ml_planned = df.loc[(df['Duration'] == 0) & (df['Status']=='Planned') ]  

        # Task completed
        task_completed = df.loc[(df['Duration'] > 0) & (df['Status']=='Completed') ] 

        # Associate colors to status values
        color_discrete_map = {'Completed': 'rgb(0,255,0)', 'Working': 'rgb(0,0,128)', 'Planned': 'rgb(0,0,220)'} 


        # Create Gantt Chart
        fig = px.timeline(df, 
                  x_start='Start Date', 
                  x_end='End Date', 
                  y='Id', 
                  # color='Status', 
                  color_discrete_map = color_discrete_map,
                  text='Task Name', 
                  title=prj_name,
                  template="plotly"
        )


        # Draw the today vertical line in red
        date = int(round(time.time()*1000))  # Today date and time in milliseconds
        today =datetime.datetime.today().strftime("%d/%m/%Y") # Today date conversion to string

        fig.add_vline(x=date, 
              line_width=3, 
              line_dash="dash", 
              annotation_text="Today! (" + today +")", 
              annotation_position="top right", 
              line_color="red")

        fig2 = px.scatter(ml_completed, x='Start Date', 
                  y='Id',
                  color= 'Status',
                  color_discrete_map = color_discrete_map,
                  text=ml_completed['Id'] + " - " + ml_completed['Task Name']
                ) 
        fig2.update_traces(name='Milestone Completed',
                   textposition='middle right', 
                   textfont=dict(size=TEXT_FONT_SIZE),
                   marker=dict(size=15,symbol='diamond'))

        fig3 = px.scatter(ml_working, x='Start Date', 
                  y='Id',
                  color= 'Status',
                  color_discrete_map = color_discrete_map,
                  text=ml_working['Id'] + " - " + ml_working['Task Name']
                ) 
        fig3.update_traces(name='Milestone Working',
                   textposition='middle right', 
                   textfont=dict(size=TEXT_FONT_SIZE),
                   marker=dict(size=15,symbol='diamond'))

        fig4 = px.scatter(ml_planned, x='Start Date', 
                  y='Id',
                  color= 'Status',
                  color_discrete_map = color_discrete_map,
                  text=ml_planned['Id'] + " - " + ml_planned['Task Name']
                ) 
        fig4.update_traces(name='Milestone Planned',
                   textposition='middle right', 
                   textfont=dict(size=TEXT_FONT_SIZE),
                   marker=dict(size=15,symbol='diamond'))

        # Milestone visualization
        try:      
                fig.add_trace(fig2.data[0])
        except IndexError:
                print("Milestone Completed non presenti")
        try:
                fig.add_trace(fig3.data[0])
        except IndexError:
                print("Milestone Working non presenti")

        try:
                fig.add_trace(fig4.data[0])
        except IndexError:
                print("Milestone Planned non presenti")


        # Update/Change Layout

        fig.update_yaxes(autorange='reversed')
        fig.update_layout(
                title_font_size=42,
                font_size=18,
                title_font_family='Arial',
        )

        # Interactive Gantt
        #fig = ff.create_gantt(df)

        # Save Graph and Export to HTML
        plotly.offline.plot(fig, filename=output_file)
        
# Main function, where start the business logic 
# command line input parameter:
# $ gantt -i inputfile -p "project title"


def main(argv):
        
        input_file = INPUT_FILE
        prj_name = 'XXX'
        prj_title = 'Gantt del Progetto XXX'
        output_file = 'gantt-' + get_filename_only(INPUT_FILE) + '.html'
        
        try:
                opts,args =getopt.getopt(argv,"hi:p:",["ifile=","pname="])
        except getopt.GetoptError:
                print('gantt.py -i <inputfile> -p <projectname>')
                sys.exit(2)
        for opt, args in opts:
                if opt == '-h':
                        print('gantt.py -i <inputfile> -p <projectname>')
                        sys.exit()
                elif opt in ("-i","--ifile"):
                        input_file = args
                        namefile = get_filename_only(args)
                        output_file = 'gantt-' + namefile+ '.html'
                elif opt in ("-p","--pname"):
                        prj_name = args
                        prj_title = "Gantt del Progetto " + prj_name
        
        if os.path.isfile(input_file):              
                print("Input file is: ", input_file)
                print("Output file is: ", output_file)
                print("Project name is: ", prj_name)
                print("Project Title is: ", prj_title)
        else:
                print("Error!!!")
                print("The input file not exists!")
                print("The program aborted")
                sys.exit(2)
        
        # Read Dataframe from Excel file
        df = pd.read_excel(input_file,sheet_name="PERT")
        
        create_gantt(prj_title,df, output_file)
        return 1

# Application starting point
if __name__ == "__main__":
        main(sys.argv[1:])