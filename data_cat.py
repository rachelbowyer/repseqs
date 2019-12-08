import numpy as np
import pandas as pd
import data_sort as ds


# categories = [ds.High['sampleName'], ds.Low['sampleName'], ds.Serum_Starvation['sampleName'], ds.Meki['sampleName'], ds.CDK46i['sampleName'], ds.Contact_Inhibition['sampleName']]


'''
**********************************************************
_________ Experiment 1, Clone_1_P21_high_v_low ___________

**********************************************************
'''

# ______________________ Ctrl1_Clone1_Low ______________________
i=0

for entry in ds.Ctrl1_Clone1_Low['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Ctrl1_Clone1_Low_frac = pd.DataFrame(frac_data[0])
        Ctrl1_Clone1_Low_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Ctrl1_Clone1_Low_frac[entry] = frac_data[3]

# ______________________ Exp1_Clone1_High ______________________

i=0

for entry in ds.Exp1_Clone1_High['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Exp1_Clone1_High_frac = pd.DataFrame(frac_data[0], columns = ['gene'])
        Exp1_Clone1_High_frac['gene'] = frac_data[0]
        
        Exp1_Clone1_High_frac['class'] = frac_data[1]
        Exp1_Clone1_High_frac['family'] = frac_data[2]
        Exp1_Clone1_High_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Exp1_Clone1_High_frac[entry] = frac_data[3]

Clone_1_P21_high_v_low = pd.concat([Exp1_Clone1_High_frac, Ctrl1_Clone1_Low_frac[Ctrl1_Clone1_Low_frac.columns[1:]]], axis=1, sort=False)
# print(Clone_1_P21_high_v_low)

# Clone_1_P21_high_v_low.to_csv('Clone_1_P21_high_v_low.csv')

'''
**********************************************************
_________ Experiment 2, Clone_2_P21_high_v_low ___________
**********************************************************
'''

# ______________________ Ctrl2_Clone2_Low ______________________
i=0

for entry in ds.Ctrl2_Clone2_Low['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Ctrl2_Clone2_Low_frac = pd.DataFrame(frac_data[0])
        
        Ctrl2_Clone2_Low_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Ctrl2_Clone2_Low_frac[entry] = frac_data[3]

# ______________________ Exp2_Clone2_High ______________________

i=0

for entry in ds.Exp2_Clone2_High['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Exp2_Clone2_High_frac = pd.DataFrame(frac_data[0], columns = ['gene'])
        Exp2_Clone2_High_frac['gene'] = frac_data[0]
        
        Exp2_Clone2_High_frac['class'] = frac_data[1]
        Exp2_Clone2_High_frac['family'] = frac_data[2]
        Exp2_Clone2_High_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Exp2_Clone2_High_frac[entry] = frac_data[3]

Clone_2_P21_high_v_low = pd.concat([Exp2_Clone2_High_frac, Ctrl2_Clone2_Low_frac[Ctrl2_Clone2_Low_frac.columns[1:]]], axis=1, sort=False)
# print(Clone_2_P21_high_v_low)

# Clone_2_P21_high_v_low.to_csv('Clone_2_P21_high_v_low.csv')

'''
**********************************************************
_________ Control for Experiments 3,4,5,6 ________________
**********************************************************
'''

# ______________________ Ctrl3_4_5_6 ______________________
i=0

for entry in ds.Ctrl3_4_5_6['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Ctrl3_4_5_6_frac = pd.DataFrame(frac_data[0])
        
        Ctrl3_4_5_6_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Ctrl3_4_5_6_frac[entry] = frac_data[3]

# print(Ctrl3_4_5_6_frac)

'''
**********************************************************
_________ Control for Experiments 7,8,9,10 ________________
**********************************************************
'''

# ______________________ Ctrl7_8_9_10 ______________________
i=0

for entry in ds.Ctrl7_8_9_10['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Ctrl7_8_9_10_frac = pd.DataFrame(frac_data[0])
        
        Ctrl7_8_9_10_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Ctrl7_8_9_10_frac[entry] = frac_data[3]

# print(Ctrl7_8_9_10_frac)

'''
**********************************************************
_________ Experiment 3, Serum_Starvation_1 ___________
**********************************************************
'''
i=0

for entry in ds.Serum_Starvation_1['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Serum_Starvation_1_frac = pd.DataFrame(frac_data[0], columns = ['gene'])
        Serum_Starvation_1_frac['gene'] = frac_data[0]
        
        Serum_Starvation_1_frac['class'] = frac_data[1]
        Serum_Starvation_1_frac['family'] = frac_data[2]
        Serum_Starvation_1_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Serum_Starvation_1_frac[entry] = frac_data[3]

Serum_Starvation_1 = pd.concat([Serum_Starvation_1_frac, Ctrl3_4_5_6_frac[Ctrl3_4_5_6_frac.columns[1:]]], axis=1, sort=False)
# print(Serum_Starvation_1)

# Serum_Starvation_1.to_csv('Serum_Starvation_1.csv')

'''
**********************************************************
_________ Experiment 4, Meki_1 ___________
**********************************************************
'''
i=0

for entry in ds.Meki_1['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Meki_1_frac = pd.DataFrame(frac_data[0], columns = ['gene'])
        Meki_1_frac['gene'] = frac_data[0]
        
        Meki_1_frac['class'] = frac_data[1]
        Meki_1_frac['family'] = frac_data[2]
        Meki_1_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Meki_1_frac[entry] = frac_data[3]

Meki_1 = pd.concat([Meki_1_frac, Ctrl3_4_5_6_frac [Ctrl3_4_5_6_frac.columns[1:]]], axis=1, sort=False)
# print(Meki_1)

# Meki_1.to_csv('Meki_1.csv')

'''
**********************************************************
_________ Experiment 5, CDK46i_1 ___________
**********************************************************
'''
i=0

for entry in ds.CDK46i_1['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        CDK46i_1_frac = pd.DataFrame(frac_data[0], columns = ['gene'])
        CDK46i_1_frac['gene'] = frac_data[0]
        
        CDK46i_1_frac['class'] = frac_data[1]
        CDK46i_1_frac['family'] = frac_data[2]
        CDK46i_1_frac[entry] = frac_data[3]

        i = i + 1

    else:

        CDK46i_1_frac[entry] = frac_data[3]

CDK46i_1 = pd.concat([CDK46i_1_frac, Ctrl3_4_5_6_frac [Ctrl3_4_5_6_frac.columns[1:]]], axis=1, sort=False)
# print(CDK46i_1)

# CDK46i_1.to_csv('CDK46i_1.csv')

'''
**********************************************************
_________ Experiment 6, Contact_Inhibition_1 ___________
**********************************************************
'''
i=0

for entry in ds.Contact_Inhibition_1['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Contact_Inhibition_1_frac = pd.DataFrame(frac_data[0], columns = ['gene'])
        Contact_Inhibition_1_frac['gene'] = frac_data[0]
        
        Contact_Inhibition_1_frac['class'] = frac_data[1]
        Contact_Inhibition_1_frac['family'] = frac_data[2]
        Contact_Inhibition_1_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Contact_Inhibition_1_frac[entry] = frac_data[3]

Contact_Inhibition_1 = pd.concat([Contact_Inhibition_1_frac, Ctrl3_4_5_6_frac[Ctrl3_4_5_6_frac.columns[1:]]], axis=1, sort=False)
# print(Contact_Inhibition_1)

# Contact_Inhibition_1.to_csv('Contact_Inhibition_1.csv')

'''
**********************************************************
_________ Experiment 7, Serum_Starvation_2 ___________
**********************************************************
'''
i=0

for entry in ds.Serum_Starvation_2['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Serum_Starvation_2_frac = pd.DataFrame(frac_data[0], columns = ['gene'])
        Serum_Starvation_2_frac['gene'] = frac_data[0]
        
        Serum_Starvation_2_frac['class'] = frac_data[1]
        Serum_Starvation_2_frac['family'] = frac_data[2]
        Serum_Starvation_2_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Serum_Starvation_2_frac[entry] = frac_data[3]

Serum_Starvation_2 = pd.concat([Serum_Starvation_2_frac, Ctrl7_8_9_10_frac[Ctrl7_8_9_10_frac.columns[1:]]], axis=1, sort=False)
# print(Serum_Starvation_2)

# Serum_Starvation_2.to_csv('Serum_Starvation_2.csv')

'''
**********************************************************
_________ Experiment 8, Meki_2 ___________
**********************************************************
'''
i=0

for entry in ds.Meki_2['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Meki_2_frac = pd.DataFrame(frac_data[0], columns = ['gene'])
        Meki_2_frac['gene'] = frac_data[0]
        
        Meki_2_frac['class'] = frac_data[1]
        Meki_2_frac['family'] = frac_data[2]
        Meki_2_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Meki_2_frac[entry] = frac_data[3]

Meki_2 = pd.concat([Meki_2_frac, Ctrl7_8_9_10_frac[Ctrl7_8_9_10_frac.columns[1:]]], axis=1, sort=False)
# print(Meki_2)

# Meki_2.to_csv('Meki_2.csv')

'''
**********************************************************
_________ Experiment 9, CDK46i_2 ___________
**********************************************************
'''
i=0

for entry in ds.CDK46i_2['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        CDK46i_2_frac = pd.DataFrame(frac_data[0], columns = ['gene'])
        CDK46i_2_frac['gene'] = frac_data[0]
        
        CDK46i_2_frac['class'] = frac_data[1]
        CDK46i_2_frac['family'] = frac_data[2]
        CDK46i_2_frac[entry] = frac_data[3]

        i = i + 1

    else:

        CDK46i_2_frac[entry] = frac_data[3]

CDK46i_2 = pd.concat([CDK46i_2_frac, Ctrl7_8_9_10_frac[Ctrl7_8_9_10_frac.columns[1:]]], axis=1, sort=False)
# print(CDK46i_2)

CDK46i_2.to_csv('CDK46i_2.csv')

'''
**********************************************************
_________ Experiment 10, Contact_Inhibition_2 ___________
**********************************************************
'''
i=0

for entry in ds.Contact_Inhibition_2['sampleName']:

    number = entry[1:]

    folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
    frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'

    frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)

    if i == 0:

        Contact_Inhibition_2_frac = pd.DataFrame(frac_data[0], columns = ['gene'])
        Contact_Inhibition_2_frac['gene'] = frac_data[0]
        
        Contact_Inhibition_2_frac['class'] = frac_data[1]
        Contact_Inhibition_2_frac['family'] = frac_data[2]
        Contact_Inhibition_2_frac[entry] = frac_data[3]

        i = i + 1

    else:

        Contact_Inhibition_2_frac[entry] = frac_data[3]

Contact_Inhibition_2 = pd.concat([Contact_Inhibition_2_frac, Ctrl7_8_9_10_frac[Ctrl7_8_9_10_frac.columns[1:]]], axis=1, sort=False)
# print(Contact_Inhibition_2)

# Contact_Inhibition_2.to_csv('Contact_Inhibition_2.csv')



"""
***
Below code is for Sample Info Pairing without Regard to Experiment Number
***
"""
# '''
# ______________________ High ______________________
# '''

# i=0

# for entry in ds.High['sampleName']:

#     number = entry[1:]

#     folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
#     frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
#     class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
#     family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

#     frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
#     class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
#     family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

#     if i == 0:

#         High_frac = pd.DataFrame(frac_data[0])
#         High_class = pd.DataFrame(class_data[0])
#         High_family = pd.DataFrame(family_data[0])
        
#         High_frac[entry] = frac_data[3]
#         High_class[entry] = class_data[1]
#         High_family[entry] = family_data[1]

#         i = i + 1

#     else:

#         High_frac[entry] = frac_data[3]
#         High_class[entry] = class_data[1]
#         High_family[entry] = family_data[1]   

# # print(High_family)
# # High_frac.to_csv('High_frac.csv')
# # High_class.to_csv('High_class.csv')
# # High_family.to_csv('High_family.csv')

# '''
# ______________________ Low ______________________
# '''
        
# i=0

# for entry in ds.Low['sampleName']:

#     number = entry[1:]

#     folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
#     frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
#     class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
#     family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

#     frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
#     class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
#     family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

#     if i == 0:

#         Low_frac = pd.DataFrame(frac_data[0])
#         Low_class = pd.DataFrame(class_data[0])
#         Low_family = pd.DataFrame(family_data[0])
        
#         Low_frac[entry] = frac_data[3]
#         Low_class[entry] = class_data[1]
#         Low_family[entry] = family_data[1]

#         i = i + 1

#     else:

#         Low_frac[entry] = frac_data[3]
#         Low_class[entry] = class_data[1]
#         Low_family[entry] = family_data[1]

# # print(Low_family)
# # Low_frac.to_csv('Low_frac.csv')
# # Low_class.to_csv('Low_class.csv')
# # Low_family.to_csv('Low_family.csv')

# '''
# ______________________ Serum Starvation ______________________
# '''
        
# i=0

# for entry in ds.Serum_Starvation['sampleName']:

#     number = entry[1:]

#     folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
#     frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
#     class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
#     family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

#     frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
#     class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
#     family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

#     if i == 0:

#         Serum_Starvation_frac = pd.DataFrame(frac_data[0])
#         Serum_Starvation_class = pd.DataFrame(class_data[0])
#         Serum_Starvation_family = pd.DataFrame(family_data[0])
        
#         Serum_Starvation_frac[entry] = frac_data[3]
#         Serum_Starvation_class[entry] = class_data[1]
#         Serum_Starvation_family[entry] = family_data[1]

#         i = i + 1

#     else:

#         Serum_Starvation_frac[entry] = frac_data[3]
#         Serum_Starvation_class[entry] = class_data[1]
#         Serum_Starvation_family[entry] = family_data[1]

# # print(Serum_Starvation_family)
# # Serum_Starvation_frac.to_csv('Serum_Starvation_frac.csv')
# # Serum_Starvation_class.to_csv('Serum_Starvation_class.csv')
# # Serum_Starvation_family.to_csv('Serum_Starvation_family.csv')

# '''
# ______________________ Meki ______________________
# '''
        
# i=0

# for entry in ds.Meki['sampleName']:

#     number = entry[1:]

#     folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
#     frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
#     class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
#     family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

#     frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
#     class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
#     family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

#     if i == 0:

#         Meki_frac = pd.DataFrame(frac_data[0])
#         Meki_class = pd.DataFrame(class_data[0])
#         Meki_family = pd.DataFrame(family_data[0])
        
#         Meki_frac[entry] = frac_data[3]
#         Meki_class[entry] = class_data[1]
#         Meki_family[entry] = family_data[1]

#         i = i + 1

#     else:

#         Meki_frac[entry] = frac_data[3]
#         Meki_class[entry] = class_data[1]
#         Meki_family[entry] = family_data[1]

# # print(Meki_family)
# # Meki_frac.to_csv('Meki_frac.csv')
# # Meki_class.to_csv('Meki_class.csv')
# # Meki_family.to_csv('Meki_family.csv')

# '''
# ______________________ CDK46i ______________________
# '''
        
# i=0

# for entry in ds.CDK46i['sampleName']:

#     number = entry[1:]

#     folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
#     frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
#     class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
#     family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

#     frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
#     class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
#     family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

#     if i == 0:

#         CDK46i_frac = pd.DataFrame(frac_data[0])
#         CDK46i_class = pd.DataFrame(class_data[0])
#         CDK46i_family = pd.DataFrame(family_data[0])
        
#         CDK46i_frac[entry] = frac_data[3]
#         CDK46i_class[entry] = class_data[1]
#         CDK46i_family[entry] = family_data[1]

#         i = i + 1

#     else:

#         CDK46i_frac[entry] = frac_data[3]
#         CDK46i_class[entry] = class_data[1]
#         CDK46i_family[entry] = family_data[1]

# # print(CDK46i_family)
# # CDK46i_frac.to_csv('CDK46i_frac.csv')
# # CDK46i_class.to_csv('CDK46i_class.csv')
# # CDK46i_family.to_csv('CDK46i_family.csv')

# '''
# ______________________ Contact_Inhibition ______________________
# '''
        
# i=0

# for entry in ds.Contact_Inhibition['sampleName']:

#     number = entry[1:]

#     folder_name = 'Min_' + number + '_' + entry + '_trimmomatic/'
#     frac_name = 'Min_' + number + '_' + entry + '_trimmomatic_fraction_counts.txt'
#     class_name = 'Min_' + number + '_' + entry + '_trimmomatic_class_fraction_counts.txt'
#     family_name = 'Min_' + number + '_' + entry + '_trimmomatic_family_fraction_counts.txt'

#     frac_data = pd.read_csv('./data/raw_data/' + folder_name + frac_name, sep="\t", header=None)
#     class_data = pd.read_csv('./data/raw_data/' + folder_name + class_name, sep="\t", header=None)
#     family_data = pd.read_csv('./data/raw_data/' + folder_name + family_name, sep="\t", header=None)

#     if i == 0:

#         Contact_Inhibition_frac = pd.DataFrame(frac_data[0])
#         Contact_Inhibition_class = pd.DataFrame(class_data[0])
#         Contact_Inhibition_family = pd.DataFrame(family_data[0])
        
#         Contact_Inhibition_frac[entry] = frac_data[3]
#         Contact_Inhibition_class[entry] = class_data[1]
#         Contact_Inhibition_family[entry] = family_data[1]

#         i = i + 1

#     else:

#         Contact_Inhibition_frac[entry] = frac_data[3]
#         Contact_Inhibition_class[entry] = class_data[1]
#         Contact_Inhibition_family[entry] = family_data[1]

# # print(Contact_Inhibition_family)
# # Contact_Inhibition_frac.to_csv('Contact_Inhibition_frac.csv')
# # Contact_Inhibition_class.to_csv('Contact_Inhibition_class.csv')
# # Contact_Inhibition_family.to_csv('Contact_Inhibition_family.csv')
