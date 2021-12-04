from Datakit import convert, count, convert_to_tfrecord, visualizer, create_labels

"""
Test Code when using Tensorflow SSD models
"""

"""
#Parse XML Annotations and convert to CVS table
parsed_train_xml= convert.Converter(data_rel_directory='data\\Val', data_set='Val.csv', all_gen_dir='all_generated')
parsed_train_xml.xml_write_to_csv()
"""

#count = count.Counter(base_directory='/home/clark/Documents/Object Detectn', csv_filename='Train_labels.csv', txt_filename='labelmap.txt',pbtxt_filename='labelmap.pbtxt')
#count.unique_n()

#count.write_labelmap_txt()
#count.write_labelmap_pbtxt()


"""Test Visualizer
vis = visualizer.Visualizer(csv_file="Train_vs_Val.csv", train_csv="all_generated\\Train.csv", val_csv="all_generated\\Val.csv", 
                            save_as_png = "Train_vs_Val.png",
                            html_file='Train.html')
vis.graph()
"""

"""Create labels
labels = create_labels.Labels(labels_fname='symptoms', train_vs_val_csv='Train_vs_Val.csv')
#labels.create_pbtxt()
labels.create_txt()
"""

"""Create TFRecord

"""
tfr = convert_to_tfrecord.shardTFRecord(csv_file_input='all_generated\\Val.csv', pbtxt_labels='all_generated\\symptoms.pbtxt', data_type='Val', num_of_shards=1)
tfr.convert()