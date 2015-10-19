import corpus
import pymongo
import aiml
import commands
import inflect
import wordtonum 
import datetime
import re
from dateutil.relativedelta import relativedelta
import sys

sys.dont_write_bytecode = True

def gaiml(query):
	k = aiml.Kernel()
	k.learn("gla.aiml")
	k.setBotPredicate("name", "shiva") 
	query = query.lower()
	query = query.replace(".","")
	query = k.respond(query)
	query = query.lower()
	if "." in query:
		query = query.split(".")
	else:
		query = [query]
	return query

def gdisc(query):
	disc = corpus.disc
	query = query.replace("'s","")
	query = query.replace("&","and")
	query = re.sub(r'[^\w]',' ',query)
	key = query.split()
	key2 = query.split()
	for i in range(0,len(key)):
		if key[i] in disc:
			key2.remove(key[i])
	query = " ".join(key2)
	query = query.strip()
	return query

def gspl(fields):
	msg = "<NA>"
	key = []
	t = corpus.t
	w = corpus.w
	s = corpus.s
	m = corpus.m
	r = corpus.r
	sp = corpus.sp
	e = corpus.e
	key.extend(fields)
	key = list(set(key))
	for i in range(0,len(t)):
		if t[i] in key:
			msg = "<train status>"
			break
	for i in range(0,len(w)):
		if w[i] in key:
			msg = "<weather status>"
			break
	for i in range(0,len(s)):
		if s[i] in key:
			msg = "<stock status>"
			break
	for i in range(0,len(m)):
		if m[i] in key:
			msg = "<mineral status>"
			break
	for i in range(0,len(sp)):
		if sp[i] in key:
			msg = "<sports status>"
			break
	for i in range(0,len(r)):
		if r[i] in key:
			msg = "<review status>"
			break
	for i in range(0,len(e)):
		if e[i] in key:
			msg = "<exam status>"
			break
	return msg

def bulkmodules(fields):
	msg = "<NA>"
	key = []
	loc = corpus.loc
	mov = corpus.mov
	key.extend(fields)
	key = list(set(key))
	for i in range(0,len(loc)):
		if loc[i] in key:
			msg = "<locationcentric module>"
			flag = 1
			break
	for i in range(0,len(mov)):
		if mov[i] in key:
			msg = "<movie module>"
			flag = 1
			break
	return msg

def wordmatrix(query):
	#print query
	cols = []
	vals = []
	match = []
	temp = []
	rem = []
	client = pymongo.MongoClient()
	mdb = client['brainse']
	wg = mdb['wordgraph']
	query = query.split()		
	results = wg.find({"graph":{"$in":query}})
	for row in results:
		temp.append(row['word'])	
		rem.extend(row['graph'])
	for i in temp:
		results = wg.find({"word":i})
		for row in results:
			if len(row['graph'])>0:
				vals.append(row['graph'])
				try:
					query.remove(i)
				except:
					continue
	for i in range(0,len(vals)):
		x = len(list(set(query)&set(vals[i])))
		match.append(x)
	for i in rem:
		if i in query:
			query.remove(i)
	query = " ".join(query)
	while(len(match)>0):
		temp2 = temp[match.index(max(match))]
		match.remove(max(match))
		if temp2 not in cols:
			cols.append(temp2)
		temp.remove(temp2)
	if len(cols)==0:
		cols = ""	
	yield query
	yield cols

def getsymbol(query):
	query = query.split()
	low = corpus.low
	high = corpus.high
	maxi = corpus.maxi
	mini = corpus.mini
	avg = corpus.avg
	summ = corpus.summ
	symbol = ""
	flag = True
	for i in query:
		if i in low:
			symbol = "$lt"
			query.remove(i)
			flag = False
			break
		elif i in high:
			symbol = "$gt"
			query.remove(i)
			flag = False
			break
		elif i in maxi:
			symbol = "$max"
			query.remove(i)
			flag = False
			break
		elif i in mini:
			symbol = "$min"
			query.remove(i)
			flag = False
			break
		elif i in avg:
			symbol = "$avg"
			query.remove(i)
			flag = False
		elif i in summ:
			symbol = "$sum"
			query.remove(i)
			flag = False
	if flag:
		symbol = "<NA>"	
	yield query
	yield symbol
	
def idnum(query):
	flag = False
	word = []
	word1 = []
	word2 = []
	typer = []
	reg = r'[0-9]+th|[0-9]+nd|[0-9]+rd|[0-9]+st'
	temp = re.findall(reg,query)
	word1.extend(temp)
	if len(word1)>0:
		flag = True
		for i in range(0,len(word1)):
			query = query.replace(word1[i],"<number>")
			query = query.strip()
			typer.append("<T1>")
	reg = r'[0-9]+'
	temp = re.findall(reg,query)
	word2.extend(temp)
	if len(word2)>0:
		flag = True
		for i in range(0,len(word2)):
			query.replace(word2[i],"<number>")
			query = query.strip()
			typer.append("<T2>")
	word.extend(word1)
	word.extend(word2)
	yield flag
	yield word
	yield typer
			
def idword(query):
	flag = False
	word = []
	typer = []
	totalnum = corpus.totalnum
	normal = corpus.normal
	temp = ""
	query = query.split()
	for i in range(0,len(query)):
		if query[i] in totalnum:
			temp = temp+" "+query[i]
			temp = temp.strip()
			if i==len(query)-1:
				word.append(temp)
				temp = temp.split()
				if temp[len(temp)-1] in normal.values():
					typer.append("<T3>")
				else:
					typer.append("<T4>")
		else:
			word.append(temp)
			temp = temp.split()
			if len(temp)>0:
				if temp[len(temp)-1] in normal.values():
					typer.append("<T3>")
				else:
					typer.append("<T4>")
			temp = ""
	while "" in word:
		word.remove("")		
	if len(word)>0:
		flag = True
	yield flag
	yield word
	yield typer

def getwords(word,wtnfinal):
	p = inflect.engine()
	temp = p.number_to_words(word)
	temp = temp.replace(",","")
	temp = temp.replace("-"," ")
	temp = temp.strip()
	wtnfinal.append(temp)
	ordins = corpus.ordins
	temp = temp.split()
	if temp[0] in ordins:
		temp.insert(0,"one")
	temp = " ".join(temp)
	temp = p.ordinal(temp)
	wtnfinal.append(temp)
	return wtnfinal

def t1(word):
	p = inflect.engine()
	endins = corpus.endins
	wtnfinal = []
	wtnfinal.append(word)
	for i in endins:
		if i in word:
			word = word.replace(i,"")
			wtnfinal.insert(0,word)
			break
	wtnfinal = getwords(word,wtnfinal)
	return wtnfinal

def t2(word):
	wtnfinal = []
	p = inflect.engine()
	wtnfinal.append(word)
	wtnfinal.append(p.ordinal(word))
	wtnfinal = getwords(word,wtnfinal)
	return wtnfinal

def t3(word):							
	wtnfinal = []
	normal = corpus.normal
	ordins = corpus.ordins
	p = inflect.engine()
	wtnobj = wordtonum.WordsToNumbers()
	word = word.split()
	temp = normal.keys()[normal.values().index(word[len(word)-1])]
	word.remove(word[len(word)-1])
	word.append(temp)
	if word[0] in ordins:
		word.insert(0,"one")
	word = " ".join(word)
	num = wtnobj.parse(word)
	wtnfinal.append(word)
	wtnfinal.insert(0,num)
	wtnfinal.insert(1,p.ordinal(num))
	temp = p.ordinal(word)
	wtnfinal.append(temp)	
	return wtnfinal

def t4(word):
	wtnfinal = []
	ordins = corpus.ordins
	word = word.split()
	if word[0] in ordins:
		word.insert(0,"one")
	word = " ".join(word)
	wtnfinal.append(word)
	p = inflect.engine()
	wtnobj = wordtonum.WordsToNumbers()
	num = wtnobj.parse(word)
	wtnfinal.insert(0,num)
	wtnfinal.insert(1,p.ordinal(num))
	word = word.split()
	normal = corpus.normal
	if word[len(word)-1] in normal.keys():
		word.insert(len(word)-1,normal[word[len(word)-1]])
		word.remove(word[len(word)-1])
	wtnfinal.append(" ".join(word))
	return wtnfinal

def getwordtonum(query):
	wtn = []
	query = " ".join(query)
	cquery = ""+query
	flag,word,typer = idnum(query)
	if flag:
		for i in range(0,len(typer)):
			if(typer[i]=="<T1>"):
				wtnfinal = t1(word[i])
				cquery = cquery.replace(word[i],"<number>")
				query = query.replace(word[i],"")
				query = query.strip()
				wtn.append(wtnfinal)
			elif(typer[i]=="<T2>"):
				wtnfinal = t2(word[i])
				cquery = cquery.replace(word[i],"<number>")
				query = query.replace(word[i],"")
				query = query.strip()
				wtn.append(wtnfinal)
	flag,word,typer = idword(query)
	if flag:
		for i in range(0,len(typer)):
			if(typer[i]=="<T3>"):
				wtnfinal = t3(word[i])
				cquery = cquery.replace(word[i],"<number>")
				query = query.replace(word[i],"")
				query = query.strip()
				wtn.append(wtnfinal)
			elif(typer[i]=="<T4>"):
				wtnfinal = t4(word[i])	
				cquery = cquery.replace(word[i],"<number>")
				query = query.replace(word[i],"")
				query = query.strip()
				wtn.append(wtnfinal)
	
	if len(wtn)==0:
		wtn = "<NA>"
	yield wtn
	yield query
	yield cquery

def delay_factor(query):
	y = 0
	negetive = corpus.negetive
	positive = corpus.positive
	temp = list(set(query)&set(negetive))
	if len(temp)>0:
		for i in temp:
			if i in query:
				query.remove(i)
		y = -1
	else:
		temp = list(set(query)&set(positive))
		if len(temp)>0:
			for i in temp:
				if i in query:
					query.remove(i)
		y = 1
	yield y
	yield query


def getexactdate(query,x):
	x = int(x)
	date = "<NA>"
	temp = ""
	dayx = 0
	calender = corpus.calender
	yearbox = corpus.yearbox
	query = query.split()
	for i in query:
		if i in calender:
			temp = temp+i
			query.remove(i)
			break
	y,query = delay_factor(query)
	x = x*y
	today = datetime.date.today()
	common = len(list(set(yearbox)&set([temp])))
	if "day" in temp:
		date = today+datetime.timedelta(days=x)	
	elif "week" in temp:
		date = today+datetime.timedelta(weeks=x)
	elif "month" in temp:
		date = today+relativedelta(months=x)
	elif common>0:
		if "decade" in temp:
			x = x*10
		elif "centur" in temp:
			x = x*100
		date = today+relativedelta(years=x)
	yield query
	yield date

def getcount(query):
	count = -1
	flag = False
	daters = corpus.daters
	query = query.split()
	for i in range(0,len(query)):
		if query[i]=="<number>":
			count = count+1
			if i!=(len(query)-1):
				if query[i+1] in daters:
					flag = True
	yield count
	yield flag

def logic(query):
	query,symbol = getsymbol(query)
	wtn,query,cquery = getwordtonum(query)
	if len(wtn)>0:
		count,flag = getcount(cquery)
		if flag:
			query,date = getexactdate(query,wtn[count][0])
			wtn.remove(wtn[count])
		else:
			query,date = getexactdate(query,1)
	else:
		query,date = getexactdate(query,1)
	if len(query) == 0:	
		query = "<Empty>"
	yield query
	yield symbol
	yield wtn
	yield date

def gettable(query,cols): #Do it now
	tabs = []
	client = pymongo.MongoClient()
	mdb = client['kb']				#??
	if len(tabs)==0:
		tabs = "<NA>"
	return tabs
