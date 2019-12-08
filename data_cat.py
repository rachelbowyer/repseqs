import numpy as np
import pandas as pd
import data_sort as ds


# categories = [ds.High['sampleName'], ds.Low['sampleName'], ds.Serum_Starvation['sampleName'], ds.Meki['sampleName'], ds.CDK46i['sampleName'], ds.Contact_Inhibition['sampleName']]


'''
______________________ High ______________________
'''

i=0

for entry in ds.High['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
    class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
    family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
    class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
    family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

    if i == 0:

        High_frac = pd.DataFrame(frac_data[0])
        High_class = pd.DataFrame(class_data[0])
        High_family = pd.DataFrame(family_data[0])
        
        High_frac[entry] = frac_data[3]
        High_class[entry] = class_data[1]
        High_family[entry] = family_data[1]

        i = i + 1

    else:

        High_frac[entry] = frac_data[3]
        High_class[entry] = class_data[1]
        High_family[entry] = family_data[1]   

# print(High_family)
High_frac.to_csv('High_frac.csv')
High_class.to_csv('High_class.csv')
High_family.to_csv('High_family.csv')

'''
______________________ Low ______________________
'''
        
i=0

for entry in ds.Low['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
    class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
    family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
    class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
    family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

    if i == 0:

        Low_frac = pd.DataFrame(frac_data[0])
        Low_class = pd.DataFrame(class_data[0])
        Low_family = pd.DataFrame(family_data[0])
        
        Low_frac[entry] = frac_data[3]
        Low_class[entry] = class_data[1]
        Low_family[entry] = family_data[1]

        i = i + 1

    else:

        Low_frac[entry] = frac_data[3]
        Low_class[entry] = class_data[1]
        Low_family[entry] = family_data[1]

# print(Low_family)
Low_frac.to_csv('Low_frac.csv')
Low_class.to_csv('Low_class.csv')
Low_family.to_csv('Low_family.csv')

'''
______________________ Serum Starvation ______________________
'''
        
i=0

for entry in ds.Serum_Starvation['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
    class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
    family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
    class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
    family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

    if i == 0:

        Serum_Starvation_frac = pd.DataFrame(frac_data[0])
        Serum_Starvation_class = pd.DataFrame(class_data[0])
        Serum_Starvation_family = pd.DataFrame(family_data[0])
        
        Serum_Starvation_frac[entry] = frac_data[3]
        Serum_Starvation_class[entry] = class_data[1]
        Serum_Starvation_family[entry] = family_data[1]

        i = i + 1

    else:

        Serum_Starvation_frac[entry] = frac_data[3]
        Serum_Starvation_class[entry] = class_data[1]
        Serum_Starvation_family[entry] = family_data[1]

# print(Serum_Starvation_family)
Serum_Starvation_frac.to_csv('Serum_Starvation_frac.csv')
Serum_Starvation_class.to_csv('Serum_Starvation_class.csv')
Serum_Starvation_family.to_csv('Serum_Starvation_family.csv')

'''
______________________ Meki ______________________
'''
        
i=0

for entry in ds.Meki['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
    class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
    family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
    class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
    family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

    if i == 0:

        Meki_frac = pd.DataFrame(frac_data[0])
        Meki_class = pd.DataFrame(class_data[0])
        Meki_family = pd.DataFrame(family_data[0])
        
        Meki_frac[entry] = frac_data[3]
        Meki_class[entry] = class_data[1]
        Meki_family[entry] = family_data[1]

        i = i + 1

    else:

        Meki_frac[entry] = frac_data[3]
        Meki_class[entry] = class_data[1]
        Meki_family[entry] = family_data[1]

# print(Meki_family)
Meki_frac.to_csv('Meki_frac.csv')
Meki_class.to_csv('Meki_class.csv')
Meki_family.to_csv('Meki_family.csv')

'''
______________________ CDK46i ______________________
'''
        
i=0

for entry in ds.CDK46i['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
    class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
    family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
    class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
    family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

    if i == 0:

        CDK46i_frac = pd.DataFrame(frac_data[0])
        CDK46i_class = pd.DataFrame(class_data[0])
        CDK46i_family = pd.DataFrame(family_data[0])
        
        CDK46i_frac[entry] = frac_data[3]
        CDK46i_class[entry] = class_data[1]
        CDK46i_family[entry] = family_data[1]

        i = i + 1

    else:

        CDK46i_frac[entry] = frac_data[3]
        CDK46i_class[entry] = class_data[1]
        CDK46i_family[entry] = family_data[1]

# print(CDK46i_family)
CDK46i_frac.to_csv('CDK46i_frac.csv')
CDK46i_class.to_csv('CDK46i_class.csv')
CDK46i_family.to_csv('CDK46i_family.csv')

'''
______________________ Contact_Inhibition ______________________
'''
        
i=0

for entry in ds.Contact_Inhibition['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
    class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
    family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
    class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
    family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

    if i == 0:

        Contact_Inhibition_frac = pd.DataFrame(frac_data[0])
        Contact_Inhibition_class = pd.DataFrame(class_data[0])
        Contact_Inhibition_family = pd.DataFrame(family_data[0])
        
        Contact_Inhibition_frac[entry] = frac_data[3]
        Contact_Inhibition_class[entry] = class_data[1]
        Contact_Inhibition_family[entry] = family_data[1]

        i = i + 1

    else:

        Contact_Inhibition_frac[entry] = frac_data[3]
        Contact_Inhibition_class[entry] = class_data[1]
        Contact_Inhibition_family[entry] = family_data[1]

# print(Contact_Inhibition_family)
Contact_Inhibition_frac.to_csv('Contact_Inhibition_frac.csv')
Contact_Inhibition_class.to_csv('Contact_Inhibition_class.csv')
Contact_Inhibition_family.to_csv('Contact_Inhibition_family.csv')