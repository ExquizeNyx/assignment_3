#!/usr/bin/env python3

#How to run from assignment_3 folder: %run script/assignment_3_vandenbroek_s3118843


#### Define functions ############################################################################

# function for calcultating the sum of the read counts
def calculateSum (readcounts, column):
    totalsum = 0
    for read in readcounts:
        totalsum = totalsum + int(read[column])
    return totalsum

#### Main ########################################################################################

# read file line-for line and stores content in tab-delimited empty list
readcounts = []
with open ("raw/white_readcounts.txt", "r") as fh:
    next(fh)
    for line in fh:
        readcounts.append(line.strip().split('\t'))

# read file line-for-line and stores content in tab-delimited empty list
report_unfiltered = []
with open ("raw/MGIBatchReport_20211217_155157.txt", "r") as fh:
    next(fh)
    for line in fh:
        report_unfiltered.append(line.strip().split('\t'))

# print the library size of every sample
print("The amount of reads in the library of sample SRR1796061 is:  " + str(calculateSum(readcounts,1)))
print("The amount of reads in the library of sample SRR1796064 is:  " + str(calculateSum(readcounts,2)))
print("The amount of reads in the library of sample SRR1796094 is:  " + str(calculateSum(readcounts,3)))
print("The amount of reads in the library of sample SRR1796237 is:  " + str(calculateSum(readcounts,4)))
print("The amount of reads in the library of sample SRR1796312 is:  " + str(calculateSum(readcounts,5)))
print("The amount of reads in the library of sample SRR1796318 is:  " + str(calculateSum(readcounts,6)))


# create a dictionary, key for dictionary is gene_data[0] (the gene id: ENSMUSG00000000001, etc)
# there is no need to loop any more, because you can directly access the object with the key
# filter out the gene id's that have no associated gene name
report = {}
for gene_data in report_unfiltered:
    key = gene_data[0]
    if gene_data[2] != "No associated gene":
        report[key] = gene_data

# print headerline with gene ID, gene name and sample name
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

# create empty list reformattedread that will hold the reformatted data
reformatted_read = []

# loops over the list of reads, checks if the key(gene_id: ENSMUSG00000000001, etc) exist in the report
# if it does, it gets the object and adds the gene name to the newly created list
for read_data in readcounts:
    new_data = read_data
    key = read_data[0]
    if key in report:
        gene_info = report[key]
        new_data.insert(1,gene_info[3])
        reformatted_read.append(new_data)

# write the headerline and the results to tab-delimited output file
with open('output/new_readcounts.txt', 'w', newline='') as output:
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
        

    
        



