# repseqs
SWE4S Final Project

## Modules, Scripts, and Files
*data_sort.py*:  The data for this project is held in 40 folders that each have three files in them: (1) a class fraction count file, (2) a family fraction count file, (3) a fraction count file.  data_sort.py uses the file sampleinfo_pairings2.csv to group the data in these folders according to the "Sample Identity" column in that file.  The "Sample Identity" column refers to _____________________  data_sort.py utilizes the pandas dataframe package of python. The inputs of this module are the folders contained in data/raw_data/ in this repository.  This module has now output.

*data_cat.py*:  This modules builds off of data_sort.py and takes the groupings given by the module to created concatinated .csv files that have all samples with the same experimental treatment together. data_cat.py utilizes the pandas dataframe package of python. This module requires the data_sort.py module and outputs 18 .csv files.


## Example of Running Code
The modules in this program are designed to handle the data of this project.  Therefore, the user must download the appropriate data from the data/raw_data folder in this repository.  To run the modules, the user may use the following commands

```
python data_sort.py
python data_cat.py
```
