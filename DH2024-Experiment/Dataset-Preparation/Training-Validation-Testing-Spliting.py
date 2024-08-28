import argparse
import codecs
import jsonlines


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Prepare file in CONLL BIO format")
	parser.add_argument("--inputFile", help="The name of the file to process")
	parser.add_argument("--outputFileTraining", help="The name of the file to store the extracted data for training")
	parser.add_argument("--outputFileValidation", help="The name of the file to store the extracted data for validation")
	parser.add_argument("--outputFileTesting", help="The name of the file to store the extracted data for validation")
	args = parser.parse_args()
	
	output_file_training = codecs.open(args.outputFileTraining,encoding='utf-8',mode="w+")
	output_file_validation = codecs.open(args.outputFileValidation,encoding='utf-8',mode="w+")
	output_file_testing = codecs.open(args.outputFileTesting,encoding='utf-8',mode="w+")
	
	total_number_of_charters = 0
	with jsonlines.open(args.inputFile) as reader:
		for obj in reader:
			total_number_of_charters = total_number_of_charters + 1
	
	
	training_charters_nbr = int((total_number_of_charters*70)/100)
	
	validation_charters_nbr = int((total_number_of_charters*15)/100)
	
	testing_charters_nbr = int((total_number_of_charters*15)/100)
	
	
	if(training_charters_nbr+validation_charters_nbr+testing_charters_nbr < total_number_of_charters):
		validation_charters_nbr = total_number_of_charters - training_charters_nbr - testing_charters_nbr
	
	
	
	with jsonlines.open(args.inputFile) as reader:
		for idx, obj in enumerate(reader):
			if idx <= training_charters_nbr+1:
				token_text=[]
				token_label=[]

			
				for i in range(len(obj['tokens'])):
					token_text.append(obj['tokens'][i]['text'])
					token_label.append("O")
				
			
				if 'spans' in obj:
					for i in range(len(obj['tokens'])):
						for j in obj['spans']:
							if obj['tokens'][i]['start'] == j['start']:
								token_label[i] = "B-"+j['label']
						
								if obj['tokens'][i]['end'] == j['end']:
									break
								else:
									for k in range(i+1,len(obj['tokens'])):
										if(obj['tokens'][k]['end'] <= j['end']):
											token_label[k] = "I-"+j['label']
										else:
											break

						
				for i in range(len(token_text)):
					output_file_training.write(token_text[i]+"\t"+token_label[i]+"\n")
				output_file_training.write("\n")
			
			
			
			if idx > training_charters_nbr+1 and idx <= training_charters_nbr+1+validation_charters_nbr+1:
				token_text=[]
				token_label=[]

			
				for i in range(len(obj['tokens'])):
					token_text.append(obj['tokens'][i]['text'])
					token_label.append("O")
				
			
				if 'spans' in obj:
					for i in range(len(obj['tokens'])):
						for j in obj['spans']:
							if obj['tokens'][i]['start'] == j['start']:
								token_label[i] = "B-"+j['label']
						
								if obj['tokens'][i]['end'] == j['end']:
									break
								else:
									for k in range(i+1,len(obj['tokens'])):
										if(obj['tokens'][k]['end'] <= j['end']):
											token_label[k] = "I-"+j['label']
										else:
											break

						
				for i in range(len(token_text)):
					output_file_validation.write(token_text[i]+"\t"+token_label[i]+"\n")
				output_file_validation.write("\n")
			
			
			
			if idx > training_charters_nbr+1+validation_charters_nbr+1:
				token_text=[]
				token_label=[]

			
				for i in range(len(obj['tokens'])):
					token_text.append(obj['tokens'][i]['text'])
					token_label.append("O")
				
			
				if 'spans' in obj:
					for i in range(len(obj['tokens'])):
						for j in obj['spans']:
							if obj['tokens'][i]['start'] == j['start']:
								token_label[i] = "B-"+j['label']
						
								if obj['tokens'][i]['end'] == j['end']:
									break
								else:
									for k in range(i+1,len(obj['tokens'])):
										if(obj['tokens'][k]['end'] <= j['end']):
											token_label[k] = "I-"+j['label']
										else:
											break

						
				for i in range(len(token_text)):
					output_file_testing.write(token_text[i]+"\t"+token_label[i]+"\n")
				output_file_testing.write("\n")
