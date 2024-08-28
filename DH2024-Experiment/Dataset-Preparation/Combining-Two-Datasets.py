import argparse
import codecs

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Combining the content of 2 files")
	parser.add_argument("--FirstFile", help="The name of the first file to get content from")
	parser.add_argument("--SecondFile", help="The name of the second file to get content from")
	parser.add_argument("--OutputFile", help="The name of the file to store the content of the first file followed by the content of the second file")
	
	
	args = parser.parse_args()
	first_file = codecs.open(args.FirstFile, encoding='utf-8')
	second_file = codecs.open(args.SecondFile, encoding='utf-8')
	output_file = codecs.open(args.OutputFile,encoding='utf-8',mode="w+")

	
	for line in first_file:
		output_file.write(line)
		
	for line in second_file:
		output_file.write(line)
