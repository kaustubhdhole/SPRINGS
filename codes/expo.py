# SRINGS version 1.0
# Copyright (c) ABC Lab, BITS Pilani - K.K. Birla Goa Campus, India.
# All Rights Reserved.
# We advise the users to exercise the following code as it is.
# Any alteration(s) made to the below given code may result in
# the improper functioning of the software.
# SPRINGS recommends Python 2.7.4 & GNU Octave 3.6.4 and above versions.
# =============================================== CODE BEGINS ==================================================
import os
import math
os.chdir('..')
n=os.getcwd()
os.chdir(n+"/Output1")
for files in os.listdir("."):
    infile=files
    x=infile.split('.')[0]
    path=n+'/input_prsa/'
    infile=x+'.txt'
    with open(infile, 'r') as file:
        file_info=''
        fname=file.name
        l=[1.1]*186
        j=0
	for line in file:
		j=0
        	for i in range(180):
        	    	l[i]=float(math.exp((-1)*float(line[j:j+3])))
        	    	l[i]=round(1/(1+l[i]),2)
        	    	j+=3
        	s=line.split(' ')
        	l[185]=float(s[-1])
        	l[184]=round(1/(1+float(math.exp((-1)*float(s[-2])))),2)
        	l[183]=round(1/(1+float(math.exp((-1)*float(s[-3])))),2)
        	l[182]=round(1/(1+float(math.exp((-1)*float(s[-4])))),2)
        	l[181]=round(1/(1+float(math.exp((-1)*float(s[-5])))),2)
        	l[180]=round(1/(1+float(math.exp((-1)*float(s[-6])))),2)
        	for k in range(186):
        	    file_info+=' '+ str(l[k])
        	file_info+='\n'
        f=n+'/Output2/'+ fname
        with open(f,"w") as ofile:
            ofile.write(file_info)
#
# ============================================ END OF CODE =====================================================
#
# For any assistance please feel free to mail us at suku@goa.bits-pilani.ac.in
#
