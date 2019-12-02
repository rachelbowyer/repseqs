import numpy as np
import pandas as pd

"""
Reading in Data and Separated Based on Experiment

"""
data = pd.read_csv('sampleinfo.txt', sep="\t", header=0)


# p21 grouping
High = data.loc[data['p21'] == 'high']
Exp1_Clone1 = High[:5]
Exp2_Clone2 = High[-5:]

Low = data.loc[data['p21'] == 'low']
Ctrl1 = Low[:5]
Ctrl2 = Low[-5:]

NoInfo = data.loc[data['p21'] == 'noInfo']
Control = NoInfo.loc[data['treatment'] == 'control']
Ctrl3_4_5_6 = Control[:2]
Ctrl7_8_9_10 = Control[-2:]

# treatment grouping for NoInfo group
Serum_Starvation = NoInfo.loc[NoInfo['treatment'] == 'serum_s']

Exp3_Clone1 = Serum_Starvation[:2]
Exp7_Clone2 = Serum_Starvation[-2:]

Meki = NoInfo.loc[NoInfo['treatment'] == 'meki']

Exp4_Clone1 = Meki[:2]
Exp8_Clone2 = Meki[-2:]

CDK46i = NoInfo.loc[NoInfo['treatment'] == 'cdk46i']

Exp5_Clone1 = CDK46i[:2]
Exp9_Clone2 = CDK46i[-2:]

Contact_Inhibition = NoInfo.loc[NoInfo['treatment'] == 'contact_in']

Exp6_Clone1 = Contact_Inhibition[:2]
Exp10_Clone2 = Contact_Inhibition[-2:]

"""
Print statements for each experiment
"""

# print(Exp1_Clone1)
# print(Exp2_Clone2)

# print(Ctrl3_4_5_6)
# print(Ctrl7_8_9_10)

# print(Exp3_Clone1)
# print(Exp7_Clone2)

# print(Exp4_Clone1)
# print(Exp8_Clone2)

# print(Exp5_Clone1)
# print(Exp9_Clone2)

# print(Exp6_Clone1)
# print(Exp10_Clone2)