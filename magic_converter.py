import csv
import sys
import xml.etree.cElementTree as ET
	
def main():
	if len(sys.argv) <= 1:
		print("Provide a file")
		input()
		sys.exit(-1)
		
	file_name = sys.argv[1]

	if not check_file(file_name):
		print("Not a valid file")
		input()
		sys.exit(-1)
		
	print(file_name)
	convert_file(file_name)	
		
def check_file(file_name):
	extension = file_name.rsplit(".", 1)[-1]
	
	if extension == "csv":
		return True

	return False
	
def convert_file(file_name):
	root = ET.Element("cards")
	ET.SubElement(root, "name")
	ET.SubElement(root, "key")
	ET.SubElement(root, "comment")
	ET.SubElement(root, "type")
	doc = ET.SubElement(root, "list")

	with open(file_name, newline='') as csvfile:
		card_reader = csv.DictReader(csvfile, delimiter=',', quotechar="\"")
		next(card_reader) #skip header
		
		for row in card_reader:
			write_node(doc, row)
			
	tree = ET.ElementTree(root)
	tree.write("collection.xml")
			
def write_node(doc, row):
	mcp = ET.SubElement(doc, "mcp")
	card = ET.SubElement(mcp, "card")
	ET.SubElement(card, "name").text = row['Card']
	ET.SubElement(card, "edition").text = row['Set']
	ET.SubElement(mcp, "count").text = row['Total Qty']
	ET.SubElement(mcp, "ownership").text = "true"

if __name__ == '__main__':
	main()