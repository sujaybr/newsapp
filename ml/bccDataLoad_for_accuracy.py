def proc(data):
	a = []
	for i in data:
		if ord(i) >= ord('a') and ord(i) <= ord('z') or ord(i) >= ord('A') and ord(i) <= ord('Z') or ord(i) == ord(' '):
			a.append(i.lower())
		else:
			a.append(' ')

	return "".join(a)

def getData(category):
	a = []
	for ind in range(11,100):

		try:
			data = open(str("./BCC_news_data/" + str(category) + "/0" + str(ind) + ".txt"), "r")
			a.append(proc(data.read()))
		except:
			print (ind)
			pass

	return a

def agetBusiness():
	res = getData("business")
	return res

def agetEntertainment():
	res = getData("entertainment")
	return res

def agetPolitics():
	res = getData("politics")
	return res

def agetSports():
	res = getData("sport")
	return res

def agetTech():
	res = getData("tech")
	return res
