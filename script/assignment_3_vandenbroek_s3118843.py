#!/usr/bin/env python3

#How to run:

#
def calculateSum (readcounts, col):
    totalsum = 0
    for read in readcounts:
        totalsum = totalsum + int(read[col])
    return totalsum

####Main##################################################

#read file line-for line and stores content in empty list readcounts
readcounts = []
with open ("white_readcounts.txt", "r") as fh:
    next(fh)
    for line in fh:
        readcounts.append(line.strip().split('\t'))

#read file line-for-line and stores content in empty list report
report_unfiltered = []
with open ("MGIBatchReport_20211217_155157.txt", "r") as fh:
    next(fh)
    for line in fh:
        report_unfiltered.append(line.strip().split('\t'))

#
print("The amount of reads in the library of sample SRR1796061 is:  " + str(calculateSum(readcounts,1)))
print("The amount of reads in the library of sample SRR1796064 is:  " + str(calculateSum(readcounts,2)))
print("The amount of reads in the library of sample SRR1796094 is:  " + str(calculateSum(readcounts,3)))
print("The amount of reads in the library of sample SRR1796237 is:  " + str(calculateSum(readcounts,4)))
print("The amount of reads in the library of sample SRR1796312 is:  " + str(calculateSum(readcounts,5)))
print("The amount of reads in the library of sample SRR1796318 is:  " + str(calculateSum(readcounts,6)))


#
report = {}
for gene_name in report_unfiltered:
    if gene_name[2] != "No associated gene":
        report[gene_name[0]] = gene_name


#
print(
    "Gene_ID\t"
    "Name\t"
    "SRR1796061\t"
    "SRR1796064\t"
    "SRR1796094\t"
    "SRR1796237\t"
    "SRR1796312\t"
    "SRR1796318"
)

#create empty list reformattedread that will hold the reformatted data
reformatted_read = []

for gene_data in readcounts:
    new_data = gene_data
    if gene_data[0] in report:
        gene_info = report[gene_data[0]]
        new_data.insert(1,gene_info[3])
        reformatted_read.append(new_data)

#
with open('combined_file.txt', 'w', newline='') as output:
    output.write(
        "Gene_ID\t"
        "Name\t"
        "SRR1796061\t"
        "SRR1796064\t"
        "SRR1796094\t"
        "SRR1796237\t"
        "SRR1796312\t"
        "SRR1796318\n")
    for result in reformatted_read:
        output.write("\t".join(result) + "\n")
        
#    writer = csv.DictWriter(outcsv, fieldnames = ["Gene ID", "Name", "SRR1796061", "SRR1796064", "SRR1796094", "SRR1796237", "SRR1796312", "SRR1796318"])
#    writer.writeheader()
#    writer.writerows(reformatted_read)
    
        



