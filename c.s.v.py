import pandas 
import csv
import os
PATH = r''
filenames = ['x','y']
x_vals = []                      #comma separated values
y_vals = []
if not os.path.exists(PATH):
    with open(PATH,'w') as fp:
        writer =  csv.DictWriter(fp,fieldnames=filenames)
        writer.writeheader()
        for index,value in enumerate(range(len(x_vals))):
            writer.writerow({'x':x_vals[index],'y':y_vals[index]})
        

