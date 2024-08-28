#pip install scikit-learn
#python3 -m spacy download de_core_news_lg

import argparse
import sys
import codecs
import spacy
from sklearn.metrics import f1_score, classification_report


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Testing performance of model on ground-truth data")
	parser.add_argument("--inputFile", help="The name of the file containing the testing partion of the ground-truth data")
	parser.add_argument("--testedLabel", help="The name of the named entity category to process: either PERS ; LOC ; or ORG")
	parser.add_argument("--testedModel", help="An entry referring to the model to test")
	args = parser.parse_args()
	
	
	
	if args.testedModel == 'spacy-standard-german':
		nlp = spacy.load("de_core_news_lg")
	else:
		if args.testedModel == 'my-model':
			nlp = spacy.load(args.testedLabel+"-Model"+"/model-best")
		else:
			print("please enter a valid model name")
			sys.exit(0)
	
	
	
	input_file = codecs.open(args.inputFile, encoding='utf-8')
	
	
	true_tokens = []
	true_labels = []
	
	
	for line in input_file:
		word_text, BIO_tag = line.split("\t", 2)
		true_tokens.append(word_text)
		
		refined_BIO_tag = ''
		for i in range(len(BIO_tag)-1):
			refined_BIO_tag = refined_BIO_tag + BIO_tag[i]
	
		
		true_labels.append(refined_BIO_tag)
		
	
	input_text = ' '.join(true_tokens)
	
		
	doc = nlp(input_text)
	
	
	pred_tokens = []
	pred_labels = []
	
	
	for token in doc:
		pred_tokens.append(token.text)
		
		
		if((token.ent_type_ == args.testedLabel) or (token.ent_type_ == args.testedLabel+'S') or (token.ent_type_+'S' == args.testedLabel)):
			if token.ent_type_ == 'PER':
				pred_labels.append(token.ent_iob_+"-"+token.ent_type_+'S')
			else:
				pred_labels.append(token.ent_iob_+"-"+token.ent_type_)
				
		else:
			pred_labels.append("O")
			
	
	print(classification_report(true_labels, pred_labels))
