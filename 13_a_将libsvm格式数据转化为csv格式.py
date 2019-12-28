# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:51:46 2019

@author: Administrator
"""

#!/usr/bin/env python

"""
convert libsvm file to csv'
libsvm2csv.py <input file> <output file> <X dimensionality>
"""

import sys
import csv

###命令行方式
#input_file = sys.argv[1]
#output_file = sys.argv[2]
#d = int( sys.argv[3] ) #必须要设定维数

###直接在程序中设定
##input_file = 'G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random.scaled.txt'
##output_file = 'G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random.scaled.csv'
#input_file = 'G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random_test.scaled.txt'
#output_file = 'G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random_test.scaled.csv'
#d = 27

def fromLibSvmToCSV(input_file,output_file,d):
	assert ( d > 0 )
	
	reader = csv.reader( open( input_file ), delimiter = " " )
	myfile=open( output_file, 'w',newline='' )
	writer = csv.writer(myfile)
	index=0
	for line in reader:
		label = line.pop( 0 )
		if line[-1].strip() == '':
			line.pop( -1 )
			
		# print line
		
		line = map( lambda x: tuple( x.split( ":" )), line )
		#print line
		# ('1', '0.194035105364'), ('2', '0.186042408882'), ('3', '-0.148706067206'), ...
		
		new_line = [ label ] + [ 0 ] * d
		for i, v in line:
			i = int( i )
			if i <= d:
				new_line[i] = v
	
	
			
		writer.writerow( new_line )
		index=index+1
	myfile.flush()
	print (index)
if __name__ == "__main__":
	####处理tc特征
#	files_list_input=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random.scaled.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random_test.scaled.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_complete.scaled.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_5000_1_4_train_random.scaled.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_5000_1_4_train_random_test.scaled.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_complete.scaled.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_5000_1_4_train_random.scaled.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_5000_1_4_train_random_test.scaled.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_complete.scaled.txt']
#	files_list_output=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random_test.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_complete.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_5000_1_4_train_random.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_5000_1_4_train_random_test.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_complete.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_5000_1_4_train_random.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_5000_1_4_train_random_test.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_complete.scaled.csv']
#	input_output=zip(files_list_input, files_list_output)
#	for input_file,output_file in input_output:
#		fromLibSvmToCSV(input_file,output_file,27)
	
	####处理dtc特征 #即包含doc2vec的。这个时候，就要注意了，是28维度
	files_list_input=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_5000_1_4_train_random.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_5000_1_4_train_random_test.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_complete.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_5000_1_4_train_random.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_5000_1_4_train_random_test.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_complete.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_5000_1_4_train_random.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_5000_1_4_train_random_test.txt','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_complete.txt']
	files_list_output=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_5000_1_4_train_random.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_5000_1_4_train_random_test.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_5000_1_4_train_random.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_5000_1_4_train_random_test.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_5000_1_4_train_random.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_5000_1_4_train_random_test.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_complete.csv']
	input_output=zip(files_list_input, files_list_output)
	for input_file,output_file in input_output:
		fromLibSvmToCSV(input_file,output_file,28)
	
	