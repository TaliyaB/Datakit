import os
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_file, ColumnDataSource
from bokeh.models import HoverTool
import pandas_bokeh
from bokeh.io import curdoc


class Visualizer:
    def __init__(self,
                base_directory = os.getcwd(),
                train_csv =None,
                val_csv = None,
                csv_file=None,
                html_file = None):

        self.base_directory = base_directory
        self.csv_file = csv_file
        self.html_file = html_file
        self.train_csv = train_csv
        self.val_csv = val_csv

        self.data = pd.read_csv(self.csv_file)
        self.df_train = pd.read_csv(self.train_csv)
        self.df_val = pd.read_csv(self.val_csv)
        self.df_train_vs_val = None

    def count_instances(self):
        symptom_freq=self.data['class'].value_counts().index.tolist()
        count_freq=self.data['class'].value_counts().values.tolist()

        #dataframe: Creates dataframe with columns=['Symptoms', 'Frequency']
        #symptom_freq=df['class'].value_counts().index.tolist()
        #count_freq=df['class'].value_counts().values.tolist()

        index= [i for i in range(len(symptom_freq))]
        zipped = list(zip(symptom_freq,count_freq))
        df_xy = pd.DataFrame(index=index, data=zipped, columns=['Symptoms', 'Frequency'])

        #train
        train_symptoms = self.df_train['class'].value_counts().index.tolist()
        train_symptoms_freq = self.df_train['class'].value_counts().values.tolist()
        train_zipped = list(zip(train_symptoms, train_symptoms_freq))
        train_index = [i for i in range(len(train_symptoms))]
        train_df = pd.DataFrame(index=train_index, data= train_zipped, columns=['Symptoms', 'Frequency'])

        #val
        val_symptoms = self.df_val['class'].value_counts().index.tolist()
        val_symptoms_freq = self.df_val['class'].value_counts().values.tolist()
        val_zipped = list(zip(val_symptoms, val_symptoms_freq))
        val_index = [j for j in range(len(val_symptoms))]
        val_df = pd.DataFrame(index=val_index, data=val_zipped, columns=['Symptoms', 'Frequency'])
        return  train_df, val_df

    def compare_data(self):
        #count instances of symptoms in train and val
        train_df , val_df = self.count_instances()

        #combine symptoms
        all_symptoms=train_df['Symptoms'].values.tolist() + val_df['Symptoms'].values.tolist()
        all_symptoms= set(all_symptoms)
        print(all_symptoms, len(all_symptoms))
        return

    def graph(self):
        """
        #Visualizer graph
        path = os.path.join(self.base_directory, 'all_generated' ,self.html_file)
        output_file(path)
        curdoc().theme =  'dark_minimal'
        src = ColumnDataSource(self.count_instances())
        p = figure()
        p.circle(x='index', y='Frequency',
                 source=src, size=6, legend='Train')
        p.title.text = 'Annotation Frequency of Abaca Viral Disease Symptoms'
        p.xaxis.axis_label = 'index'
        p.yaxis.axis_label = 'Frequency'
        p.xaxis.major_label_orientation = "vertical"
        hover = HoverTool()
        hover.tooltips = [
            ('Frequency', '@Frequency'),
            ('Symptom', '@Symptoms')
        ]
        p.add_tools(hover)

        show(p)

        :return:
        """

        #count_instances(train)
        #count_instances(val)
        #create dummy df(Symptoms, Train, Val)
        #make set of symptoms in count_instances(train)  and count_instances(val)
        #supply frequency
        #show graph
        #show table