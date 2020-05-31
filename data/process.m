	title_base = "May21_output_200by200_1000_150_900_run";
n_runs = 100;
all_data = [];
x_axis = [];

for i=0:n_runs-1
	if(exist(strcat(title_base,num2str(i),".dat"))~=0)
		temp_data = load(strcat(title_base,num2str(i),".dat"));
		all_data = [all_data temp_data(:,2)];
		if(length(x_axis)==0)
			x_axis = temp_data(:,1);
		endif
	endif
endfor

mean_data = mean(all_data,2);
std_data = std(all_data,0,2);
mean_data_minus = mean_data-std_data;
mean_data_plus = mean_data+std_data;

figure(1)
hold on;
plot(x_axis,mean_data,'color','black','linewidth',3);
plot(x_axis,mean_data_minus,'color','red','linewidth',3);
plot(x_axis,mean_data_plus,'color','blue','linewidth',3);