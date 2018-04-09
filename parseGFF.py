
#!/usr/bin/env python3

from Bio import SeqIO
import csv
# read in genome in FASTA format

genome = SeqIO.read("watermelon.fsa", "fasta")
print('sequence is ',len(genome.seq))

# open GFF file
# read it in line by line using a for loop

gff = open("watermelon.gff", 'r')
for line in gff:
	words = line.split("\t")
	species = (words[0])
	start = int(words[3])
	end = int(words[4])
	gene = (words[8])
	print(">" + species + " | " + gene + genome.seq[start-1:end]) 
# use split command to split each line into a lists
gff.close() 

"""
with open("watermelon.gff") as tsv:
	for line in csv.reader(tsv, delimiter="\t"):
		print zip(*[line.split() for line in tsv])[4:6]
"""
#use beginning and end coordinates to extract the sequence from the genome

"""

# goal of this is to extract the sequences from watermelon.fasta (done)
# use the watermelon.gff to obtain the sequence locations/ lengths (ok)
#read in genome(FASTA format), store it as a varibale. Use SeqIO for this. (ok)
#open GFF file (ok)
# read it in line by line using a for loop (ok)
# for line in ... (ok)
# (python parse tab delimited file) Tab delimited files are easy to parse (ok)
# package called 'csv' : import csv <-- parsing comma seperated value files (ok)
# Take the string and split it into a list-  split- specify which character you want to split on (ok)
# split (ok)
# use begin and end coordinates to extract the sequence from the genome 
# index into a list
# have genome, beginning and end coordinate
# print to screen
# close GFF file

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from collections import  defaultdict

# read names and positions from bed file
positions = defaultdict(list)
with open ("watermelon.gff") as f:
        for line in f:
                name, start, stop = line.split()
                positions[name].append(((start), (stop)))
seq_size = open ("watermelon.gff")
seq_data = seq_size.read()
print (seq_data)


# parse fasta file and turn into dictionary

records = SeqIO.to_dict(SeqIO.parse(open("watermelon.fsa", "fasta"))
# search for seqences

for record in SeqIO.parse("watermelon.fsa", "fasta"):
        print(record.id)
        print (sequence is' , record.seq)
        #for (start, stop) in postions[name]
                #long_seq_record = records[name]
                #long_seq = long_seq_record.seq
                #alphabet = long_seq.alphabet
                #sequence_record =  SeqRecord(Seq(long_seq, alphabet) id.name, description='')
                #sequence_record.append(sequence_record)
# write to file
with open ('homework_5.fasta', 'w') as f:
        SeqIO.write(sequence_record, f, 'fasta')
"""

