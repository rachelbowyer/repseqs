#!/bin/bash 
#SBATCH --job-name=1.fastqc
#SBATCH --mail-type=END# Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=evan.lester@colorado.edu # Where to send mail
#SBATCH --nodes=1 # Run on a single node
#SBATCH --ntasks=4
#SBATCH --mem=80gb # Memory limit
#SBATCH --time=23:00:00 # Time limit hrs:min:sec
#SBATCH --output=/Users/evle4518/projects/quiescence/eofiles/%x.o.%j # Standard output
#SBATCH --error=/Users/evle4518/projects/quiescence/eofiles/%x.e.%j # Standard error log     


### load your module(s)
module load bowtie/2.2.9  
module load samtools/1.3.1 
module load tophat/2.1.1 
module load fastqc/0.11.5    
### script
pwd; hostname; date


#num=1

IN=/Users/evle4518/projects/quiescence/data/fastq/raw/from_seq_core
OUT=/Users/evle4518/projects/quiescence/data/fastqc/raw

read_num=1
file_name=Min_"$num"_S"$num"_R"$read_num"
fastqc -t 1 $IN/"$file_name".fastq -o $OUT

read_num=2
file_name=Min_"$num"_S"$num"_R"$read_num"
fastqc -t 1 $IN/"$file_name".fastq -o $OUT


date
