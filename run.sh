#!/usr/bin/bash

#pull columns out of data file; save to txt files
./data.py

#mean of logins in September
./mean.R < SeptOutput.txt > SepMean.txt

#mean of logins in January
./mean.R < JanOutput.txt > JanMean.txt

#user inputs alpha level
./alpha.py

CRITICALZ=$(./criticalz.R < alpha.txt);
#echo "Z value is $CRITICALZ"

#calculate standard deviation
./standarddeviation.py

#calculate standard errors of january and september
./standarderror.py

STANDARDERROR_JAN=$(cat standarderror_jan.txt)
STANDARDERROR_SEP=$(cat standarderror_sep.txt)

#calculate margin of error of january
JAN_MARGIN=$(./marginoferror.R $CRITICALZ $STANDARDERROR_JAN);

#calculate margin of error of september
SEP_MARGIN=$(./marginoferror.R $CRITICALZ $STANDARDERROR_SEP);

#create january 2020 confidence interval
JAN_MEAN=$(cat JanMean.txt)
JAN_CONFIDENCE=$(./confidenceinterval.R $JAN_MEAN $JAN_MARGIN)

#create september 2020 confidence interval
SEP_MEAN=$(cat SepMean.txt)
SEP_CONFIDENCE=$(./confidenceinterval.R $SEP_MEAN $SEP_MARGIN)

echo "January confidence interval is $JAN_CONFIDENCE"
echo "September confidence interval is $SEP_CONFIDENCE"

