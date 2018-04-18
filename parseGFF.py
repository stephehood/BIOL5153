
#!/usr/bin/env python3

from Bio import SeqIO
import argparse

# create an ArgumentParser object('parser')
def get_args():
	parser = argparse.ArgumentParser(description="This script filters out sequences from a FASTA file based on information provided by a GFF file")
	parser.add_argument("fasta", type= str,  help= "name of fasta file")
	parser.add_argument(  "gff", type= str,  help="name of gff file")
	# parse the arguments
	args = parser.parse_args()
	return parser.parse_args()


##############################################################################################################################
# read in genome in FASTA format
# declare our DNA sequence
#count each nucleotide in our DNA string
# NOTE: we're assuming that our sequence is just A,C,G, and T
def get_genome():
	genome = SeqIO.read(args.fasta, "fasta")
	return genome.seq


# calculate the reverse complement
def get_reverse_complement():
		genome = SeqIO.read(args.fasta, "fasta")
		reverse_complement = genome.reverse_complement()
		return reverse_complement.seq

# open GFF file
# read it in line by line using a for loop
def parse_gff():
	gff = open(args.gff)
	genome = SeqIO.read(args.fasta, "fasta")
	for line in gff:
		words = line.split("\t")
		species = (words[0])
		start = int(words[3])
		end = int(words[4])
		strand = (words[6])
		gene = (words[8])
		return (">" + species + " | " + gene + genome.seq[start-1:end])
		# use split command to split each line into a lists
		gff.close()



def main():
		for strand in genome:
			if strand.startswith('+'):
				print (genome)
			else:
				print(reverse_complement)

# outside of main(), get a value defined below
args = get_args()
genome = get_genome()
reverse_complement = get_reverse_complement()
strand = parse_gff()
#call main
main ()


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
