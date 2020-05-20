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
N_bins_x = 15;
bins = [0:1/N_bins_x:1-1/N_bins_x];
			
%Regularize the data and model data times
conform_data_x = conform_data_x/max(conform_data_x);
model_data_x = model_data_x/max(model_data_x);

%Provide for binned conform and model data, with statistical errors
conform_data_y_binned = [];
conform_data_y_binned_err = [];
model_data_y_binned = [];

%Space of scale parameters a_x and a_y
a_x = [5:0.1:10.0];
a_y = [15.0:0.1:20.0];
chi_2_r = 1.0e7;
a_x_best = 0.0;
a_y_best = 0.0;

for ix = a_x
	for iy = a_y
		model_data_x_current = model_data_x*ix;
		model_data_y_current = model_data_y*iy;

		%First, bin the conform data
		conform_data_y_binned(end+1) = conform_data_y(1);
		conform_data_y_binned_err(end+1) = conform_data_y(1)*0.1;
		for i=[2:N_bins_x]
			index_x = find(and(conform_data_x>=bins(i-1),conform_data_x<bins(i)));
			conform_data_y_binned(end+1) = mean(conform_data_y(index_x));
			conform_data_y_binned_err(end+1) = std(conform_data_y(index_x));
		endfor

		%Second, bin the model data
		model_data_y_binned(end+1) = model_data_y_current(1);
		for i=[2:N_bins_x]
			index_x = find(and(model_data_x_current>=bins(i-1),model_data_x_current<bins(i)));
			model_data_y_binned(end+1) = mean(model_data_y_current(index_x));
		endfor

		clear index_x
		conform_data_y_binned = circshift(conform_data_y_binned,[0,-1]);
		conform_data_y_binned_err = circshift(conform_data_y_binned_err,[0,-1]);
		model_data_y_binned = circshift(model_data_y_binned,[0,-1]);

		%Compute reduced chi-squared between model and data set.
		chi_2_r_temp = mean( (conform_data_y_binned - model_data_y_binned).^2 ./ (conform_data_y_binned_err).^2 );
		if(chi_2_r_temp < chi_2_r)
			chi_2_r = chi_2_r_temp;
			a_x_best = ix;
			a_y_best = iy;
			[a_x_best a_y_best chi_2_r]
		endif

		conform_data_y_binned = [];
		conform_data_y_binned_err = [];
		model_data_y_binned = [];

	endfor
endfor

%Now for keeps.
conform_data_y_binned = [];
conform_data_y_binned_err = [];
model_data_y_binned = [];
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
plot(bins,conform_data_y_binned,'color','blue');
plot(bins,model_data_y_binned,'color','red');