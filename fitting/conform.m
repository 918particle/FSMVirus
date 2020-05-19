clear;
home;
close all;

%import the data set to which we are conforming
conform_data = load('cdc_data.dat');
%import the data set that must be conformed
model_data = load('fsm_example.dat');

%Separate the data components
conform_data_x = conform_data(:,1)-conform_data(1,1);
conform_data_y = conform_data(:,2);
model_data_x = model_data(:,1)-model_data(1,1);
model_data_y = model_data(:,2);

%Bin the data into x and y bins with errors
N_bins_x = 50;
bins = [0:1/N_bins_x:1-1/N_bins_x];
			
%Regularize the data and model data
conform_data_x = conform_data_x - conform_data_x(1);
conform_data_x = conform_data_x/max(conform_data_x);
conform_data_y = conform_data_y/max(conform_data_y);
model_data_x = model_data_x - model_data_x(1);
model_data_x = model_data_x/max(model_data_x);
model_data_y = model_data_y/max(model_data_y);

%First, bin the conform data
conform_data_y_binned = conform_data_y(1);
for i=[2:N_bins_x]
	index_x = find(and(conform_data_x>=bins(i-1),conform_data_x<bins(i)));
	conform_data_y_binned(end+1) = mean(conform_data_y(index_x));
endfor

%Second, bin the model data
model_data_y_binned = model_data_y(1);
for i=[2:N_bins_x]
	index_x = find(and(model_data_x>=bins(i-1),model_data_x<bins(i)));
	model_data_y_binned(end+1) = mean(model_data_y(index_x));
endfor

clear index_x
conform_data_y_binned = circshift(conform_data_y_binned,[0,-1]);
model_data_y_binned = circshift(model_data_y_binned,[0,-1]);

figure(1);
hold on;
semilogy(bins,conform_data_y_binned,'color','blue');
semilogy(conform_data_x,conform_data_y,'color','black');
semilogy(bins,model_data_y_binned,'color','red');
semilogy(model_data_x*5.5+0.05,model_data_y,'color','green');
axis([0 1 1e-6 10])