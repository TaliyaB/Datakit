USING DATAKIT (Draft)
=======
_Currently programmed for TensorFlow Object Detection API and the Abaca Disease Detection App._

##**Setup**
***
- Clone Datakit from github : `git clone "https://github.com/TaliyaB/Datakit.git"`
- Navigate to Datakit and you will find `setup.py` .
- The project structure looks like this : <br>
![structure](https://github.com/TaliyaB/Datakit/blob/master/screenshots/structure.png?raw=true) 
- Do `pip install .` in the directory where `setup.py` is located.
![install]() <br>
- Create a folder named `all_generated` in your base directory. Every generated file will be saved here. Sample:<br>
![all_gen]()<br>
##**Usage**
***
- Import :`from Datakit import convert, count, convert_to_tfrecord, visualizer, create_labels`
- Steps:
1. **Convert XML to CSV.** This codes iterate over the XML annotations and save it into CSV file. 
   - Sample output:<br>
   ![csvToxml]()
   - Sample:<br>
```
parsed_train_xml= convert.Converter(data_rel_directory='data\\Val', data_set='dumVal.csv', all_gen_dir='all_generated')
parsed_train_xml.xml_write_to_csv()
```
1. **Create visualizer.** This creates an HTML Visualizer and CSV file that contains the count per class. 
   - Sample:<br>
```
vis = visualizer.Visualizer(csv_file="Train_vs_Val.csv", train_csv="all_generated\\Train.csv", val_csv="all_generated\\Val.csv",
                            save_as_png = "Train_vs_Val.png",
                            html_file='Train.html')
vis.graph()
```
2. **Create Labels.**
3. **Create TFRecord.**