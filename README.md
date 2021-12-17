USING DATAKIT (Draft)
=======
_Currently programmed for TensorFlow Object Detection API and the Abaca Disease Detection App._

## **Setup**
***
- Clone Datakit from github : `git clone "https://github.com/TaliyaB/Datakit.git"`
- Navigate to Datakit and you will find `setup.py` .
- The project structure looks like this : <br>
![structure](https://github.com/TaliyaB/Datakit/blob/master/screenshots/structure.png?raw=true) 
- Do `pip install .` in the directory where `setup.py` is located.
![install](https://github.com/TaliyaB/Datakit/blob/master/screenshots/install.png?raw=true) <br>
- Create a folder named `all_generated` in your base directory. Every generated file will be saved here. Sample:<br>
![allgen](https://github.com/TaliyaB/Datakit/blob/master/screenshots/all_gen.png?raw=true)<br>

## **Usage**
***
- Import :`from Datakit import convert, count, convert_to_tfrecord, visualizer, create_labels`
- Steps:
1. **Convert XML to CSV.** This codes iterate over the XML annotations and save it into CSV file. 
   - Sample output:<br>
   ![csvToxml](https://github.com/TaliyaB/Datakit/blob/master/screenshots/1.png?raw=true)
   - Sample:<br>
```
parsed_train_xml= convert.Converter(data_rel_directory='data\\Val', data_set='dumVal.csv', all_gen_dir='all_generated')
parsed_train_xml.xml_write_to_csv()
```
2. **Create visualizer.** This creates an HTML Visualizer and CSV file that contains the count per class. 
   - Sample output:<br>
   - ![visual]()
   - ![csv_all_class]()
   - Sample:<br>
```
vis = visualizer.Visualizer(csv_file="Train_vs_Val.csv", train_csv="all_generated\\Train.csv", val_csv="all_generated\\Val.csv",
                            save_as_png = "Train_vs_Val.png",
                            html_file='Train.html')
vis.graph()
```
3. **Create Labels.** Creates pbtxt and txt labels.
   - Sample:<br>
```
vis = visualizer.Visualizer(csv_file="Train_vs_Val.csv", train_csv="all_generated\\Train.csv", val_csv="all_generated\\Val.csv",
                            save_as_png = "Train_vs_Val.png",
                            html_file='Train.html')
vis.graph()
```
4. **Create TFRecord.** TFREcord is a serialized data format required in training SSD TensorFlow models.
```
tfr = convert_to_tfrecord.shardTFRecord(csv_file_input='all_generated\\Val.csv', pbtxt_labels='all_generated\\symptoms.pbtxt', data_type='Val', num_of_shards=1)
tfr.convert()
```