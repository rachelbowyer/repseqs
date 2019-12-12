
cd /Users/evle4518/projects/tau/2019-01-24_HEK293_tau_flow_iso/scripts/8.bowtie_to_REs


for b in '7SLRNA'
do

for a in 1 2 3 4
do

script=8.bowtie_to_REs.sh
jobname=$a.$b
e_o_dir=/Users/evle4518/projects/tau/2019-01-24_HEK293_tau_flow_iso/eofiles

#pass the variable $a, job name, output, and error files to submission
sbatch --export=num=$a,repeat=$b \
--job-name=$jobname \
--output=$e_o_dir/%x.o.%j \
--error=$e_o_dir/%x.o.%j \
$script

done

done





