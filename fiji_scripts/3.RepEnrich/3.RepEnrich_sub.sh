for a in `seq 568 2 647`;
do

script=3.RepEnrich_sub.sh
jobname="$a"_$script
e_o_dir=/Users/evle4518/projects/quiescence/eofiles


#pass the variable $a, job name, output, and error files to submission
sbatch --export=num=$a \
--job-name=$jobname \
--output=$e_o_dir/%x.o.%j \
--error=$e_o_dir/%x.o.%j \
$script

done       
