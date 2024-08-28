import argparse
import codecs
import re

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Prepare file in the right format for spacy training")
	parser.add_argument("--originalFile", help="The name of the file that need a change in format/content")
	parser.add_argument("--outputFile", help="The name of the file to store the relevant content")
	parser.add_argument("--entityType", help="The entity type which annotation to keep")
	
	args = parser.parse_args()
	original_file = codecs.open(args.originalFile, encoding='utf-8')
	output_file = codecs.open(args.outputFile,encoding='utf-8',mode="w+")
	
	for line in original_file:
		
		if len(line.strip()) == 0 :
			continue
		
		info_to_keep = []
		word_text, BIO_tag = line.split("\t", 2)
		
			
		if word_text == "$":
			continue
		
		
		if word_text == " ":
			continue
		
	
		if(args.entityType == "LOC"):
			if "LOC" in BIO_tag:
				info_to_keep.append(word_text.strip())
				info_to_keep.append(BIO_tag.strip())
			
			else:
				info_to_keep.append(word_text.strip())
				info_to_keep.append("O")
				
				
		if(args.entityType == "PERS"):
			if ('PER' in BIO_tag) and not('PERS' in BIO_tag):
				info_to_keep.append(word_text.strip())
				info_to_keep.append(BIO_tag.strip()+"S")		
			else:
				if "PERS" in BIO_tag:
					info_to_keep.append(word_text.strip())
					info_to_keep.append(BIO_tag.strip())
				else:
					info_to_keep.append(word_text.strip())
					info_to_keep.append("O")
		
		
		if(args.entityType == "ORG"):
			if "ORG" in BIO_tag:
				info_to_keep.append(word_text.strip())
				info_to_keep.append(BIO_tag.strip())
			
			else:
				info_to_keep.append(word_text.strip())
				info_to_keep.append("O")
				
		
		output_file.write("\t".join(info_to_keep) + "\n")
