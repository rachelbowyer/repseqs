#!/bin/bash 
#SBATCH --job-name=3.RepEnrich_SE
#SBATCH --mail-type=END# Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=evan.lester@colorado.edu # Where to send mail
#SBATCH --nodes=1 # Run on a single node
#SBATCH --ntasks=4
#SBATCH --mem=80gb # Memory limit
#SBATCH --time=23:00:00 # Time limit hrs:min:sec
#SBATCH --output=/Users/evle4518/projects/stress_granules/repetitive_elements/eofiles/%x.o.%j # Standard output
#SBATCH --error=/Users/evle4518/projects/stress_granules/repetitive_elements/eofiles/%x.o.%j # Standard error log 

#num=8
file_name=Min_"$num"_S"$num"_trimmomatic

### load your module(s) 
module load bowtie/1.1.2
module load samtools/1.8
module load bedtools/2.23.0
module load python/2.7.14

data_folder=/Users/evle4518/projects/tau/2019-01-24_HEK293_tau_flow_iso/data/RepEnrich

input_folder=/Users/evle4518/projects/quiescence/data/RepEnrich/mapping

output_folder=/Users/evle4518/projects/quiescence/data/RepEnrich/counting

setup_folder=/Users/evle4518/projects/quiescence/scripts/3.RepEnrich/RepEnrich_setup_hg38

cd /Users/evle4518/projects/quiescence/scripts/3.RepEnrich


python RepEnrich.py \
$data_folder/hg38_repeatmasker_clean.txt \
$output_folder/$file_name $file_name \
$setup_folder \
$input_folder/"$file_name"_multimap.fastq \
$input_folder/"$file_name"_unique.bam \
--cpus 16 \


echo Time is `date`
echo RepEnrich_setup completed
