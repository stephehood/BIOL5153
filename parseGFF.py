
#!/usr/bin/env python3

# this script will parse a GFF file, extracting sequences for the annotated features

#load required modules
import sys
import os
import re
from Bio import SeqIO
import argparse

def get_args():
	# create an ArgumentParser object('parser')
	parser = argparse.ArgumentParser()

	#add required/positional arguments
	parser.add_argument("fasta", type= str,  help= "name of fasta file")
	parser.add_argument(  "gff", type= str,  help="name of gff file")

	#parse the arguments
	return parser.parse_args()


##############################################################################################################################
# read in genome in FASTA format
def parse_fasta():
	#open and read the FASTA file
	genome = SeqIO.read(args.fasta, "fasta")
	return genome.seq

# calculate the reverse complement
def reverse_comp(dna):
	return dna.reverse_complement()

def parse_gff():
	# open and parse the GFF file
	gff_file = open(args.gff, 'r')
	for line in gff_file:
		# split each line on a tab
		(seqid, source, feature, start, end, length, strand, phase, attributes) = line.split('\t')

		if(feature == 'CDS' or feature == 'tRNA' or feature == 'rRNA'):
			# split the attributes field
			atts = attributes.split(" ; ")
			# grab the gene name and, if present, the exon number
			gene = re.search("^Gene\s+(\S+)", atts[0])
			exon = re.search("exon\s+(\d+)",  atts[0])

			if(gene and exon):
				print(">" + seqid.replace(" ", "_") + "_" + gene.group(1) + "_" + exon.group(1))
			else:
				print(">" + seqid.replace(" ", "_") + "_" + gene.group(1))

			# extract the corresponding sequence
			fragment = dna[int(start)-1:int(end)]

			# print the sequence, either forward or reverse complemented
			if(strand == "+"):
				print(fragment)
			else:
				print(reverse_comp(fragment))
	gff_file.close()


def main():
	genome = parse_fasta()
	parse_gff(genome)

# get the command-line arguments
args = get_args()

#call main
main()

###################################################################################################
""""
Applying Dictionaries to our parseGFF.py script
Complex data structures:

Gene = cox1, nad1, rpl5
Exon = 1, 2, 3, 4 etc..
Sequence = ATCGCTAGC.. + or -

Genes: Key    Values
      Cox1 : [ATG...,CAA...,TGG....,CTTC....]
                1      2      3       4
      rpl5 : []

Sort a set of numbers- Dictionary, sorted keys, list

Sorted Keys : dictionaries with Key = Exon, value = sequence and sort for the exon value at the gene_dic

Read through the GFF file in a for loop
for .... print
Sort and print at the end..

"""
#################################################################################################

#Comments below refer to how the original Parse_GFF code was written


#use beginning and end coordinates to extract the sequence from the genome
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
