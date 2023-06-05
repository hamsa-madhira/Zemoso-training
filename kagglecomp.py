import csv

training_terms_path = '/Users/hamsamadhira/Desktop/cafa-5-protein-function-prediction/Train/train_terms.tsv'
#how to make this a relative path?

# entry_ID, term, aspect
with open(training_terms_path) as file:
	train_file = csv.reader(file, delimiter="\t") #\t is the tab 
	# printing data line by line
	for line in train_file:
		print(line)


taxonomy_terms_path = '/Users/hamsamadhira/Desktop/cafa-5-protein-function-prediction/Train/train_taxonomy.tsv'
#how to make this a relative path?

# entry_ID, taxonomy
with open(taxonomy_terms_path) as file:
	tax_file = csv.reader(file, delimiter="\t") #\t is the tab 
	# printing data line by line
	for line in tax_file:
		print(line)

# steps to clean th