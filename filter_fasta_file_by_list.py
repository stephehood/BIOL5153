#! /usr/bin/env python3

# load the required modles
import argparse
from Bio import SeqIO


# create an ArguementParser object ('parser') that will hold all the information necessary to parse the command line
parser = argparse.ArgumentParser(description="This script organizes sequences from a FASTA file which organizes the sequences based on their headers")

# use the add_argument() method to add a positional argument
# positional arguments are *required* inputs, so their order/postion matters
# argparse treats all options as strings unless told to do otherwise
# argparse add_arguments will tell us what we can add in the ("")

parser.add_argument("fasta", help="name of FASTA file")
parser.add_argument( "gff", type= str,  help="name of gff file")

# add an optional arguments - header name
# optional arguments set with dashes --

parser.add_argument("-l", "--list", help="filter the sequence based on header titles", action= 'append')

# parse the arguments

args= parser.parse_args()

# the variable args above is  what we will call below (args)
print("We're gonna open this FASTA file:", args.fasta)

##############################################################################################################################
# read in genome in FASTA format

genome = SeqIO.read(args.fasta, "fasta")
print('sequence is ',len(genome.seq))
print("Headers of the FASTA file are: " , args.list)

# open GFF file
# read it in line by line using a for loop

gff = open(args.gff)
for line in gff:
	words = line.split("\t")
	species = (words[0])
	#start = int(words[3])
	#end = int(words[4])
	#strand = (words[6])
	source = (words[1])
	location = (words[2])
	gene = (words[8])
	print(">" + species + " | " + source + " | " + location + " | " + gene )

# use split command to split each line into a lists
gff.close()

# change parseGFF so that that input files come from a FASTA file and a GFF file. Add and commit
# message- now use arg parse
