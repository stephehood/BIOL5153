!/bin/bash

#PBS -N RAxML
#PBS -q debug16core
#PBS -j oe
#PBS -m abe
#PBS -M seg013@uark.edu
#PBS -o $HOME/RAxMLanal/RAxMLanal_redo2.out
#PBS -l nodes=1:ppn=8
#PBS -l walltime=00:00:30:00

cd $PBS_O_WORKDIR

$HOME/seg013/raxmlHPC-SSE -T 4 -s Lipin1_seqs_for_RAxML.aln -n rbcL.out -m GTRCAT -f a -x 9346346 -N 20 -p 463574



Done


