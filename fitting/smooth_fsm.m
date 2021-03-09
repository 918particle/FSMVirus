clear
clc
close all

scale_factor = 2.5;
n = 357;
fsm_data = zeros(n,1);

for i=1:400
	fileTitle = strcat('../March6_run_',int2str(i));
	fileTitle = strcat(fileTitle,'.dat');
	if(exist(fileTitle))
		current = load(fileTitle);
		fsm_data += current(:,2)/n;
	endif
endfor

fsm_data_err = sqrt(fsm_data);
owid_data = load('owid.dat');
owid_data = owid_data(:,2);
days = transpose([1:length(owid_data)]);
fsm_data *= scale_factor;
fsm_data_err *= scale_factor;

figure(1,'position',[0,0,1000,500]);
plot(days,owid_data,'o','color','black','markersize',14);
hold on;
errorbar(days,fsm_data,fsm_data_err);
axis([-10 400 0 1100])
xlabel('Days since Outbreak','fontsize',24);
ylabel('New Cases per Day / 10^6','fontsize',24);
set(gca(),'fontsize',24);