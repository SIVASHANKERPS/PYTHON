import json
import csv
with open('data.json') as json_file:
    data = json.load(json_file)
 
student_data = data['stud_detail']
 
data_file = open('data_file.csv', 'w')

csv_writer = csv.writer(data_file)
 
count = 0
 
for stud in student_data:
    if count == 0:
        header = stud.keys()
        csv_writer.writerow(header)
        count += 1
        
    csv_writer.writerow(stud.values())
 
data_file.close()