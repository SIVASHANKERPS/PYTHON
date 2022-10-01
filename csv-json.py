import csv  
import json  
gvn_csvfile = 'data_file.csv'  
gvn_jsonfile = 'data.json'  
json_dictionary = {}  
with open(gvn_csvfile) as gvn_csvfile:
  csvfiledata = csv.DictReader(gvn_csvfile)
  json_dictionary["data"]=[]
  for row_data in csvfiledata:  
    print(row_data)
    json_dictionary["data"].append(row_data)  
with open(gvn_jsonfile, 'w') as gvn_jsonfile:  
  gvn_jsonfile.write(json.dumps(json_dictionary, indent = 4))  