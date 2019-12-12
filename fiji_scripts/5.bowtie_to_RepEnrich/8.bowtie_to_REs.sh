#!/bin/bash 
#SBATCH --job-name=bowtie_to_REs.sh
#SBATCH --mail-type=END# Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=evan.lester@colorado.edu # Where to send mail
#SBATCH --nodes=1 # Run on a single node
#SBATCH --ntasks=64 # number of cores
#SBATCH --mem=200gb # Memory limit
#SBATCH --time=23:00:00 # Time limit hrs:min:sec
#SBATCH --output=/Users/evle4518/projects/tau/2019-01-24_HEK293_tau_flow_iso/eofiles/%x.o.%j # Standard output
#SBATCH --error=/Users/evle4518/projects/tau/2019-01-24_HEK293_tau_flow_iso/eofiles/%x.e.%j # Standard error log   


#num=1
#repeat=U1
file_name=Min_"$num"_S"$num"_R1_paired_trimmomatic


indir=/Users/evle4518/projects/quiescence/data/fastq/trimmed
outdir=/Users/evle4518/projects/quiescence/data/bowtie/MamGypLTR1b
index=/Users/evle4518/projects/quiescence/data/bowtie/MamGypLTR1b/ref/MamGypLTR1b

### load your module(s)
module load bowtie/1.1.2
module load samtools/1.8
module load tophat/2.1.1 

### script
pwd; hostname; date

bowtie $index -p 16 -t -S $indir/"$file_name".fastq $outdir/"$file_name".sam

samtools view -bS $outdir/"$file_name".sam > $outdir/"$file_name".bam

#sort file for IGV viewing
samtools sort $outdir/"$file_name".bam -o $outdir/"$file_name".sorted.bam

#make index for IGV viewing
samtools index $outdir/"$file_name".sorted.bam


echo Time is `date`
echo tophat completed
