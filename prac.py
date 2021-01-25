import math as ma

#data = [45,45,63,36,45,36,45,45,9,36,
#54,54,81,72,54,45,54,54,36,45,
#72,72,36,81,36,54,9,18,72,54,
#81,81,45,63,72,72,45,36,54,9,
#36,36,54,9,45,63,72,72,45,72,
#45,54,72,18,81,9,18,54,63,27,
#54,72,27,54,18,18,36,36,18,36,
#9,27,36,27,27,45,81,18,54,45,
#45,63,54,72,45,54,45,45,72,81,
#27,81,9,36,54,81,63,63,36,63]

#data = [21,32,43,23,12,32,41,52,32,1,23,4,0,1,11,2,4,5,1,1]

#input
while True:
	data = []
	while True:
		userinput = input('enter some data (enter individual data like 10 20 30 etc. type stop to exit):')
		if userinput == 'stop':
			break
		try:
			userinput = int(userinput)
			data.append(userinput)
		except:
			print('this is not a number!')
		data.sort()
	print('----------------------------------------')
	
	#mean
	added = 0
	for l in data:
		added = added + l
	mean = added / len(data)

	#mode
	countlist = []
	for u in data:	
		i = data.count(u)
		countlist.append(i)
	indexofmode = countlist.index(max(countlist))
	mode = data[indexofmode]

	#median
	if len(data) % 2 == 1:
		indexofmedian = len(data) / 2
		median = (data[int(indexofmedian - 1.5)] + data[int(indexofmedian - 0.5)]) / 2
	else:
		indexofmedian = len(data) / 2
		median = data[int(indexofmedian - 1)]

	#range
	differ = max(data) - min(data)

	#standard deviation
	sumofsample = 0
	for s in data:
		sumofsample = sumofsample + ma.pow((s - mean), 2)
	if len(data) != 1:
		sd = ma.sqrt(sumofsample / (len(data) - 1))
	if len(data) == 1:
		sd = ma.sqrt(sumofsample / (len(data)))

	#variance
	var = ma.pow(sd,2)

	#IQR
	indexofq3 = 3 * (len(data)+1) / 4
	q3 = data[ma.floor(indexofq3 - 1)] + float(0 + (indexofq3 % 1)) * (data[ma.ceil(indexofq3 - 1)] - data[ma.floor(indexofq3 - 1)])
	indexofq1 = (len(data)+1) / 4
	q1 = data[ma.floor(indexofq1 - 1)] + float(0 + (indexofq1 % 1)) * (data[ma.ceil(indexofq1 - 1)] - data[ma.floor(indexofq1 - 1)])
	iqr = q3 - q1

	#P,Q,D
	ask = input('would you like to find the quartile, percentile and decile? (type yes or no):')
	if ask == 'yes':
		askp = input('what percentile? (answer from 1 to 100):')
		askd = input('what decile? (answer from 1 to 10):')
		askq = input('what quartile? (answer from 1 to 4):')

		#percentile
		try:
			askp = int(askp)
			if 1 <= int(askp) <= 100:
				print('finding the', askp, 'percentile')
				if askp == 100:
					indexofp = (len(data))
				elif askp == 1:
					indexofp = 1
				else:
					indexofp = askp * (len(data)+1) / 100
				percentile = data[ma.floor(indexofp - 1)] + float(0 + (indexofp % 1)) * ((data[ma.ceil(indexofp - 1)] - data[ma.floor(indexofp - 1)]))
			else:
				print('that is not a number between 1 to 100!')
				print('percentile will not be calculated')
				askp = 'None'
				percentile = 'None'
		except:
			print('that is not a number!')
			print('percentile will not be calculated')
			askp = 'None'
			percentile = 'None'

		#decile
		try:
			askd = int(askd)
			if 1 <= int(askd) <= 10:
				print('finding the', askd, 'decile')
				if askd == 10:
					indexofd = (len(data))
				elif askd == 1:
					indexofd = 1
				else:
					indexofd = askd * (len(data)+1) / 10
				decile = data[ma.floor(indexofd - 1)] + float(0 + (indexofd % 1)) * ((data[ma.ceil(indexofd - 1)] - data[ma.floor(indexofd - 1)]))
			else:
				print('that is not a number between 1 to 10!')
				print('decile will not be calculated')
				askd = 'None'
				decile = 'None'
		except:
			print('that is not a number!')
			print('decile will not be calculated')
			askd = 'None'
			decile = 'None'

		#quartile
		try:
			askq = int(askq)
			if 1 <= int(askq) <= 4:
				print('finding the', askq, 'quartile')
				if askq == 4:
					indexofq = (len(data))
				elif askq == 1:
					indexofq = 1
				else:
					indexofq = askq * (len(data)+1) / 4
				quartile = data[ma.floor(indexofq - 1)] + float(0 + (indexofq % 1)) * ((data[ma.ceil(indexofq - 1)] - data[ma.floor(indexofq - 1)]))
			else:
				print('that is not a number between 1 to 4!')
				print('quartile will not be calculated')
				askq = 'None'
				quartile = 'None'
		except:
			print('that is not a number!')
			print('quartile will not be calculated')
			askq = 'None'
			quartile = 'None'

		print('----------------------------------------')
		print('the', askp, 'percentile is', percentile)
		print('the', askd, 'decile is', decile)
		print('the', askq, 'quartile is', quartile)
		print('units is', len(data))
		print('max is', max(data))
		print('min is', min(data))
		print('range is', differ)
		print('median is', median) 
		print('mode is', mode)
		print('mean is', ma.ceil(mean*100)/100)
		print('standard deviation is', ma.ceil(sd*100)/100)
		print('variance is', ma.ceil(var*100)/100)
		print('interquartile range is', iqr)
		print('----------------------------------------')

	else:
		print('----------------------------------------')
		print('units is', len(data))
		print('max is', max(data))
		print('min is', min(data))
		print('range is', differ)
		print('median is', median) 
		print('mode is', mode)
		print('mean is', ma.ceil(mean*100)/100)
		print('standard deviation is', ma.ceil(sd*100)/100)
		print('variance is', ma.ceil(var*100)/100)
		print('interquartile range is', iqr)
		print('----------------------------------------')

	exitinput = input('would you like to run again? (yes or no):')
	print('----------------------------------------')
	if exitinput == 'yes':
		continue
	elif exitinput =='no':
		print('thank you for using this program')
		break
	else:
		print('not a yes or no answer!')
		break