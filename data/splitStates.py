dataFile = open('nytimes_state_data.csv','r')
theState = 'Oklahoma'
stateData = []
dates = []
for line in dataFile:
	pieces = line.split(',')
	if(pieces[1]==theState):
		dates.append(pieces[0])
		stateData.append(pieces[3])
dataFile.close()

saveFile = open('Oklahoma_data.dat','w')
for i in range(0,len(dates)):
	ymd = dates[i].split('-')
	time = 0
	if(ymd[1]=='03'):
		time+=0
	if(ymd[1]=='04'):
		time+=31
	if(ymd[1]=='05'):
		time+=(31+30)
	if(ymd[1]=='06'):
		time+=(31+30+31)
	time+=int(ymd[2])
	saveFile.write(str(time)+" "+str(stateData[i]))
	saveFile.write("\n")
saveFile.close()