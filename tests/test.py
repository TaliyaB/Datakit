from Datakit import convert, count, convert_to_tfrecord, visualizer

"""
Test Code when using Tensorflow SSD models
"""

"""
#Parse XML Annotations and convert to CVS table
parsed_train_xml= convert.Converter(data_rel_directory='data\\Train', data_set='Train.csv', all_gen_dir='all_generated')
parsed_train_xml.xml_write_to_csv()
"""
#count = count.Counter(base_directory='/home/clark/Documents/Object Detectn', csv_filename='Train_labels.csv', txt_filename='labelmap.txt',pbtxt_filename='labelmap.pbtxt')
#count.unique_n()

#count.write_labelmap_txt()
#count.write_labelmap_pbtxt()


"""Create TFRecord
tfr = convert_to_tfrecord.shardTFRecord(csv_file_input='all_generated\\Train.csv', pbtxt_labels='all_generated\\classes.pbtxt', data_type='Train', num_of_shards=3)
tfr.convert()
"""

"""Test Visualizer
"""
vis = visualizer.Visualizer(csv_file="all_generated\\Train.csv",
                            train_csv="all_generated\\Train.csv",
                            val_csv="all_generated\\Val.csv",
                            html_file='Train.html')
vis.graph()