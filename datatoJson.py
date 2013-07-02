import csv

surveyReader = csv.reader(open("Survey13-05-23 (2).csv"))

for row in surveyReader:
    print row
