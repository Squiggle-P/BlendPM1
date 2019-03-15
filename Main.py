

import numpy as np, pandas as pd, matplotlib.pyplot as plt

# Hardcodes

debug = True

FreshConsData = True
FilteredConsFile = 'FiltByCons.csv'

FreshGradeData = True
GradeFilePrefix = 'PM1 Blend Ratio Data - '

FreshPercentCalcs = True
PercentCalcsPrefix = 'PM1 Blend Ratio Results - '

SheetBreakTimeBefore = '2m'
SheetBreakTimeAfter = '5m'

if debug:
    CSVFileName = 'ShortPull.csv'
    SepChar = ','
else:
    CSVFileName = 'LongPull.csv'
    SepChar = ';'



# Read raw data from CSV, basic cleaning if necessary

RawDF = pd.read_csv(CSVFileName, sep=SepChar)

# Apply consistency filters
# Select consistency value(s)
# Flag bad data due to consistency
# Mark SheetBreaks & Flag Ranges
# Export to CSV


# Identify Grade Change Points
# ID Unique grade runs
# Bag DFs into groups and export to individual CSVs



# Calc dry stock tons on each line
# Calc dry stock %s at each tank
# Pick a metric (base sheet, full sheet, etc) and plot avg/LCL/UCL for each grade run
#




# print(RawDF)