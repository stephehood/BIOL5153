#! /usr/bin/env python3

# load the required modles
import argparse
from Bio import SeqIO


# create an ArguementParser object ('parser') that will hold all the information necessary to parse the command line
parser = argparse.ArgumentParser(description="This script filters out sequences from a FASTA file that are shorter than a user-specified length cutoff")

# use the add_argument() method to add a positional argument
# positional arguments are *required* inputs, so their order/postion matters
# argparse treats all options as strings unless told to do otherwise
# argparse add_arguments will tell us what we can add in the ("")

parser.add_argument("fasta", help="name of FASTA file")
parser.add_argument( "gff", type= str,  help="name of gff file")


# no errors yet
# add an optional arguments - length cut-off
# optional arguments set with dashes --

parser.add_argument("-m", "--min_seq_length", help="filter sequences that are <= min_seq_length in length (default = 300 nt)", type=int, default=300)

# parse the arguments

args= parser.parse_args()

# the variable args above is  what we will call below (args)
print("We're gonna open this FASTA file:", args.fasta)
print("filter sequences less that", args.min_seq_length, "nt in length")


##############################################################################################################################
# read in genome in FASTA format

genome = SeqIO.read(args.fasta, "fasta")
print('sequence is ',len(genome.seq))

# open GFF file
# read it in line by line using a for loop

gff = open(args.gff)
for line in gff:
	words = line.split("\t")
	species = (words[0])
	start = int(words[3])
	end = int(words[4])
	strand = (words[6])
	gene = (words[8])
	print(">" + species + " | " + gene + genome.seq[start-1:end])


# use split command to split each line into a lists
gff.close()

# change parseGFF so that that input files come from a FASTA file and a GFF file. Add and commit
# message- now use arg parse
