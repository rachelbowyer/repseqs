#!/bin/bash 
#SBATCH --job-name=7.RepEnrich_setup
#SBATCH --mail-type=END# Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=evan.lester@colorado.edu # Where to send mail
#SBATCH --nodes=1 # Run on a single node
#SBATCH --ntasks=64 # number of cores
#SBATCH --mem=200gb # Memory limit
#SBATCH --time=23:00:00 # Time limit hrs:min:sec
#SBATCH --partition=short
#SBATCH --output=/Users/evle4518/projects/tau/2019-01-24_HEK293_tau_flow_iso/eofiles/%x.o.%j # Standard output
#SBATCH --error=/Users/evle4518/projects/tau/2019-01-24_HEK293_tau_flow_iso/eofiles/%x.e.%j # Standard error log 


### load your module(s) 
module load bowtie/1.1.2
module load samtools/1.8
module load bedtools
module load python/3.6.3

cd /Users/evle4518/projects/tau/2019-01-24_HEK293_tau_flow_iso/scripts/7.RepEnrich

data=/Users/evle4518/projects/tau/2019-01-24_HEK293_tau_flow_iso/data/RepEnrich
index=/scratch/Shares/public/genomes/Homo_sapiens/UCSC/hg38/Sequence/BowtieIndex/genome.fa

python RepEnrich_setup.py $data/hg38_repeatmasker_clean.txt $index $data/setup_folder_hg38


echo Time is `date`
echo RepEnrich_setup completed
