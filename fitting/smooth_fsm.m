clear
clc
close all

n = 99;
m = 350;
fsm_data = zeros(m,1);
fsm_data_vacc = fsm_data;

for i=0:n
	fileTitle = strcat('../Feb9_run_',int2str(i));
	fileTitle = strcat(fileTitle,'.dat');
	fileTitle_vacc = strcat('../Feb9_run_vacc_',int2str(i));
	fileTitle_vacc = strcat(fileTitle_vacc,'.dat');
	if(exist(fileTitle))
		current = load(fileTitle);
		fsm_data += current(:,2)/(n+1);
	endif
	if(exist(fileTitle_vacc))
		current = load(fileTitle_vacc);
		fsm_data_vacc += current(:,2)/(n+1);
	endif
endfor

days = transpose([1:length(fsm_data)]);

figure(1);
hold on;
plot(days,fsm_data_vacc,'linewidth',5)
%plot(days,fsm_data_vacc)
axis([0 350 0 1000])
xlabel('Turns since Outbreak','fontsize',24);
ylabel('New FSMs','fontsize',24);
set(gca(),'fontsize',24);
grid on;
box on;

print('Feb14_plot2.pdf','-dpdf')
