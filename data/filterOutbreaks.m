clear;
home;

data_dir = 'results_usa_2/';

file_list = dir(data_dir);
n = length(file_list);
outbreaks = [];

for i=[1:n]
	this_file_name = strcat(data_dir,file_list(i).name);
	if(strfind(this_file_name,"output"))
		temp_data = load(this_file_name);
		if(temp_data(400,2)==0)
			clear temp_data
		else
			outbreaks = [outbreaks temp_data(:,2)];
		endif
	endif
endfor
clear i temp_data this_file_name n
save('outbreaks.dat','outbreaks');