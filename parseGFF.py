#!/usr/bin/env python3

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from collections import  defaultdict

# read names and positions from bed file
positions = defaultdict(list)
with open ("watermelon.gff") as f:
	for line in f:
		name, start, stop = line.split()
		positions[name].append(((start), (stop)))

# parse fasta file and turn into dictionary

records = SeqIO.to_dict(SeqIO.parse(open("watermelon.fasta", "fasta"))
# search for seqences

for name in positions:
	for (start, stop) in postions[name]:
		long_seq_record = records[name]
		long_seq = long_seq_record.seq
		alphabet = long_seq.alphabet
		sequence_record =  SeqRecord(Seq(long_seq, alphabet) id.name, description='')
		sequence_record.append(sequence_record)
# write to file
with open ('homework_5.fasta', 'w') as f:
	SeqIO.write(sequence_record, f, 'fasta')
#for record in SeqIO.parse ("watermelon.fsa", "fasta"):
	#print(record.id)
	#print('sequence is ', record.seq)

#seq_size = open ("watermelon.gff")
#seq_data = seq_size.read()
#print (seq_data)
# need to turn the text into a list of list

#import csv

#with open("watermelon.gff") as tsv:
	#for line in csv.reader(tsv, delimiter="\t"):
		#print zip(*[line.split() for line in tsv])[4:6]

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
