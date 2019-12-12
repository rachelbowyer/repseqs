#!/bin/bash 
#SBATCH --job-name=2.trimmomatic.sh
#SBATCH --mail-type=END# Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=evan.lester@colorado.edu # Where to send mail
#SBATCH --nodes=1 # Run on a single node
#SBATCH --ntasks=4
#SBATCH --mem=80gb # Memory limit
#SBATCH --time=23:00:00 # Time limit hrs:min:sec
#SBATCH --output=/Users/evle4518/projects/quiescence/eofiles/%x.o.%j # Standard output
#SBATCH --error=/Users/evle4518/projects/quiescence/eofiles/%x.e.%j # Standard error log  

module load fastx-toolkit

in=/Users/evle4518/projects/quiescence/data/fastq/raw/from_seq_core
out=/Users/evle4518/projects/quiescence/data/fastq/trimmed

#num=1

basename=Min_"$num"_S"$num"

read_num=1
R1file_name=Min_"$num"_S"$num"_R"$read_num"
read_num=2
R2file_name=Min_"$num"_S"$num"_R"$read_num"

#trim the starter sequence from the R1 read
fastx_trimmer -f 9 -Q33 \
-i $in/"$R1file_name".fastq \
-o $out/"$R1file_name"_trimmed.fastq

#trim the stopper sequence from the R2 read
fastx_trimmer -f 7 -Q33 \
-i $in/"$R2file_name".fastq \
-o $out/"$R2file_name"_trimmed.fastq

#remove low quality tails
fastq_quality_trimmer -t 10 -l 20 -Q33 -v \
-i $out/"$R1file_name"_trimmed.fastq \
-o $out/"$R1file_name"_trimmed_cleaned.fastq

fastq_quality_trimmer -t 10 -l 20 -Q33 -v \
-i $out/"$R2file_name"_trimmed.fastq \
-o $out/"$R2file_name"_trimmed_cleaned.fastq


infile1=$out/"$R1file_name"_trimmed_cleaned.fastq
paired_outfile1=$out/"$R1file_name"_paired_trimmomatic.fastq
unpaired_outfile1=$out/"$R1file_name"_unpaired_trimmomatic.fastq

infile2=$out/"$R2file_name"_trimmed_cleaned.fastq
paired_outfile2=$out/"$R2file_name"_paired_trimmomatic.fastq
unpaired_outfile2=$out/"$R2file_name"_unpaired_trimmomatic.fastq

java -jar /opt/trimmomatic/0.36/trimmomatic-0.36.jar PE -threads 64 -phred33 \
-trimlog $out/"$basename".trimlog \
$infile1 $infile2 \
$paired_outfile1 $unpaired_outfile1 \
$paired_outfile2 $unpaired_outfile2 \
ILLUMINACLIP:/opt/bbmap/38.05/resources/adapters.fa:2:30:10:2:keepBothReads LEADING:3 TRAILING:3 MINLEN:36



echo 'trimomatic has completed running'



