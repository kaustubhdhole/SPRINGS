% SRINGS version 1.0
% We advise the users to exercise the following code as it is.
% Any alteration(s) made to the below given code may result in
% the improper functioning of the software.
% SPRINGS recommends Python 2.7.4 & GNU Octave 3.6.4 and above versions.
% =============================================== CODE BEGINS ==================================================
codes_folder=pwd();
cd ..
folder_name=pwd()
cd codes
xdirlist=dir(strcat(folder_name,'/','Output2'));
for j=3:length(xdirlist)
	xfilename=strcat(xdirlist(j).name);
	X=load(strcat(folder_name,'/','Output2/',xfilename));
	load(strcat(folder_name,'/','codes/','Theta1.txt'));
	load(strcat(folder_name,'/','codes/','Theta2.txt'));
	m = size(X, 1);
	num_labels = size(Theta2, 1);
	p = zeros(size(X, 1), 1);
	h1 = sigmoid([ones(m, 1) X] * Theta1');
	h2 = sigmoid([ones(m, 1) h1] * Theta2');				
	p=h2>0.5;									
	out_filename=strcat(folder_name,'/','Output3/',xdirlist(j).name);
	save (out_filename, 'p');
end
# ============================================ END OF CODE =====================================================
#
# For any assistance please feel free to mail us at suku@goa.bits-pilani.ac.in
#
