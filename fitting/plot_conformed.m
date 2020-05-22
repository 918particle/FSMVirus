clear;
home;
close all;

%import the data set to which we are conforming
conform_data = load('cdc_data.dat');
%import the data set that must be conformed
model_data = load('average_data_nfood150_1000turns_100runs.dat');

%Separate the data components
conform_data_x = conform_data(:,1);
conform_data_y = conform_data(:,2);
model_data_x = model_data(:,1);
model_data_y = model_data(:,2);

%Bin the data into x and y bins with errors
N_bins_x = 40;
bins = [0:1/N_bins_x:1-1/N_bins_x];
bins = bins*max(conform_data_x);

%Provide for binned conform and model data, with statistical errors
conform_data_y_binned = [];
conform_data_y_binned_err = [];
model_data_y_binned = [];
a_x_best = 0.3;
a_y_best = 9;
model_data_x = model_data_x*a_x_best;
model_data_y = model_data_y*a_y_best;

%First, bin the conform data
conform_data_y_binned(end+1) = conform_data_y(1);
conform_data_y_binned_err(end+1) = conform_data_y(1)*0.1;
for i=[2:N_bins_x]
	index_x = find(and(conform_data_x>=bins(i-1),conform_data_x<bins(i)));
	conform_data_y_binned(end+1) = mean(conform_data_y(index_x));
	conform_data_y_binned_err(end+1) = std(conform_data_y(index_x));
endfor

%Second, bin the model data
model_data_y_binned(end+1) = model_data_y(1);
for i=[2:N_bins_x]
	index_x = find(and(model_data_x>=bins(i-1),model_data_x<bins(i)));
	model_data_y_binned(end+1) = mean(model_data_y(index_x));
endfor

figure(1);
hold on;
errorbar(bins,conform_data_y_binned,conform_data_y_binned_err);
plot(bins,model_data_y_binned,'color','red');
corr(conform_data_y_binned,model_data_y_binned)