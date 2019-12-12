#!/bin/bash 
#SBATCH --job-name=3.RepEnrich_mapping
#SBATCH --mail-type=END# Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=evan.lester@colorado.edu # Where to send mail
#SBATCH --nodes=1 # Run on a single node
#SBATCH --ntasks=4
#SBATCH --mem=80gb # Memory limit
#SBATCH --time=23:00:00 # Time limit hrs:min:sec
#SBATCH --output=/Users/evle4518/projects/quiescence/eofiles/%x.o.%j # Standard output
#SBATCH --error=/Users/evle4518/projects/quiescence/eofiles/%x.e.%j # Standard error log  

### load your module(s) 
module load bowtie/1.1.2
module load samtools/1.8
module load bedtools
module load python/3.6.3

cd /Users/evle4518/projects/quiescence/scripts/3.RepEnrich

input_folder=/Users/evle4518/projects/quiescence/data/fastq/trimmed
output_folder=/Users/evle4518/projects/quiescence/data/RepEnrich/mapping
index=/scratch/Shares/public/genomes/Homo_sapiens/UCSC/hg38/Sequence/BowtieIndex/genome

#num=1

R1file_name=Min_"$num"_S"$num"_R1_paired_trimmomatic


file_name_out=Min_"$num"_S"$num"_trimmomatic

bowtie $index -p 16 -t -m 1 -S --chunkmbs 1000 \
--max $output_folder/"$file_name_out"_multimap.fastq \
$input_folder/"$R1file_name".fastq \
$output_folder/"$file_name_out"_unique.sam

####cleaning
#conver sam to bam
samtools view -bS $output_folder/"$file_name_out"_unique.sam > \
$output_folder/"$file_name_out"_unique.bam

#sort bam file
samtools sort $output_folder/"$file_name_out"_unique.bam \
-o $output_folder/"$file_name_out"_unique_sorted.bam

#index unique sorted file
samtools index $output_folder/"$file_name_out"_unique_sorted.bam


echo Time is `date`
echo RepEnrich_setup completed
