def proc(data):
	a = []
	for i in data:
		if ord(i) >= ord('a') and ord(i) <= ord('z') or ord(i) >= ord('A') and ord(i) <= ord('Z') or ord(i) == ord(' '):
			a.append(i.lower())
		else:
			a.append(' ')

	return "".join(a)

def getData(category):
	a = ""
	for ind in range(100,400):

		try:
			data = open(str("./BCC_news_data/" + str(category) + "/" + str(ind) + ".txt"), "r")
			a += proc(data.read())
		except:
			pass

	return "".join(a)

def getBusiness():
	res = getData("business")
	return res

def getEntertainment():
	res = getData("entertainment")
	return res

def getPolitics():
	res = getData("politics")
	return res

def getSports():
	res = getData("sport")
	return res

def getTech():
	res = getData("tech")
	return res
