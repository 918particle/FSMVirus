clear
clc
close all

k = 99;
t = 198;
n = 100;
m = 2;
fsm_data = zeros(n,m);
fsm_data_vacc = fsm_data;

for i=0:k
	fileTitle = strcat('../virus_spatial_',int2str(i));
	fileTitle = strcat(fileTitle,'_','turn',int2str(t),'.dat');
	if(exist(fileTitle))
		current = load(fileTitle);
		fsm_data += current/k;
	endif
endfor

figure(1);
hold on;
image(fsm_data)
caxis([0 0.01])
h = colorbar();
colormap('jet')
axis([1 m 1 n])
set(gca(),'fontsize',20)
set(h,'fontsize',20)
