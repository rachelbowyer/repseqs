#!/bin/bash 
#SBATCH --job-name=3.fastqscreen
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
module load fastqscreen

num=1
read_num=1
file_name=Min_"$num"_S"$num"_R1_paired_trimmomatic

indir=/Users/evle4518/projects/quiescence/data/fastq/trimmed
outdir=/Users/evle4518/projects/quiescence/data/fastqscreen/trimmed
conf=/Users/evle4518/bin/fastq_screen.conf

fastq_screen --tag --conf $conf --force \
--outdir $outdir/$file_name \
$indir/"$file_name".fastq \


read_num=2
file_name=Min_"$num"_S"$num"_R2_paired_trimmomatic

indir=/Users/evle4518/projects/quiescence/data/fastq/trimmed
outdir=/Users/evle4518/projects/quiescence/data/fastqscreen/trimmed
conf=/Users/evle4518/bin/fastq_screen.conf

fastq_screen --tag --conf $conf --force \
--outdir $outdir/$file_name \
$indir/"$file_name".fastq \

echo Time is `date`
echo fastqscreen completed
