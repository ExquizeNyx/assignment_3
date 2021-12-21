#!/usr/bin/env python3

#How to run:

###modules###
import csv

####Main##################################################

#read file line-for line and stores content in empty list readcounts
readcounts = []
headers = None
with open ("white_readcounts.txt", "r") as fh:
    fh_reader = csv.reader(fh, delimiter ='\t')
    
    headers = next(fh_reader)
    for line in fh_reader:
        readcounts.append(line)
headers.insert(1,'Name')

#read file line-for-line and stores content in empty list report
report = []
with open ("MGIBatchReport_20211217_155157.txt", "r") as fh:
    fh_reader = csv.reader(fh, delimiter ='\t')
    next(fh_reader)
    for line in fh_reader:
        report.append(line)

#for rep in report:
#    print(str(rep))


#create empty list reformattedread that will hold the new/cleaned/reformatted data

reformatted_read = []

for gene_data in readcounts:
    new_data = gene_data    
    for gene_info in report:        
        if gene_data[0] == gene_info[0]:            
            new_data.insert(1, gene_info[3])
            break
    reformatted_read.append(new_data)

with open('combined_file.csv', 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(headers)
    for output in reformatted_read:
        writer.writerow(output)
        



