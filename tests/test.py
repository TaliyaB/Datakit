from Datakit import convert, count, convert_to_tfrecord

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

tfr = convert_to_tfrecord.shardTFRecord(base_directory='/home/clark/Documents/Object Detectn', csv_file_input='Train_labels.csv', pbtxt_labels='labelmap.pbtxt', data_type='train', num_of_shards=3)
tfr.convert()