import os
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_file, ColumnDataSource
from bokeh.models import HoverTool
import pandas_bokeh

class Visualizer:
    def __init__(self,
                base_directory = os.getcwd(),
                csv_file=None,
                html_file = None):

        self.base_directory = base_directory
        self.csv_file = csv_file
        self.html_file = html_file

        self.data = pd.read_csv(self.csv_file)
        self.df_xy = None

    def count_instances(self):
        symptom_freq=self.data['class'].value_counts().index.tolist()
        count_freq=self.data['class'].value_counts().values.tolist()
        index= [i for i in range(len(symptom_freq))]
        zipped = list(zip(symptom_freq,count_freq))
        df_xy = pd.DataFrame(index=index, data=zipped, columns=['Symptoms', 'Frequency'])
        return df_xy

    def graph(self):
        #Visualizer graph
        path = os.path.join(self.base_directory, 'all_generated' ,self.html_file)
        print(self.base_directory)
        print(path)
        output_file(path)
        src = ColumnDataSource(self.count_instances())
        p = figure()
        p.circle(x='index', y='Frequency',
                 source=src,
                 size=10, color='blue')
        p.title.text = 'Annotation Frequency of Abaca Viral Disease Symptoms'
        p.xaxis.axis_label = 'index'
        p.yaxis.axis_label = 'Frequency'
        hover = HoverTool()
        hover.tooltips = [
            ('Frequency', '@Frequency'),
            ('Symptom', '@Symptoms')
        ]
        p.add_tools(hover)

        show(p)
