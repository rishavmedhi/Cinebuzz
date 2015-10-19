import pymongo
import corpus
import difflib

client = pymongo.MongoClient()
mdb = client['brainse']

def getanswer(msg,query,fields,wtn,orig_query):
	query = " ".join(query)
	if msg == "<locationcentric module>":
		ans = locationcentric(query,fields)
	elif msg == "<movie module>":
		ans = movie(query,fields,wtn,orig_query)
	return ans

def locationcentric(query,fields):
	ans = "<NA>"
	import locentric
	ans = locentric.main(query)
	return ans

def movie(query,fields,wtn,orig_query):
	query1=query.split(" ")
	#print len(query1)
	a=list()
	if "movie" in fields:
		fields.remove("movie")
	mov = corpus.mov
	fin_fields = []
	for i in fields:
		if i in mov:
			fin_fields.append(i)
	ans = []
	qb = mdb['movies']
	#print "#------------------------MOVIE----------------#"
	results = qb.find({"$text":{"$search":"\'"+query+"\'"}})    #??
	allmovies = []
	ratios = []
	for row in results:
		row.pop("_id")
		a.append(row)
		allmovies.append(row['movie'].lower())
	#print allmovies
	for i in allmovies:
		r = difflib.SequenceMatcher(i.lower(),query)
		ratios.append(r.ratio())
		
	if(len(ans)==0):
		for i in range(0,len(allmovies)):
			flag=0
			for u in range(0,len(query1)):
				if(query1[u] in allmovies[i]):
					flag=1
					continue;
				else:
					flag=0;
					break;
			if(flag==1):
				if(str(allmovies[i]) in orig_query):
					pos=i
					if len(fin_fields)>0:
						for j in fin_fields:
							try:
								ans.append(a[pos][j])
								ans.append(a[pos])
							#print a[pos]
							except:
								#print "e" +str(a[pos])
								ans.append(a[pos])
					else:
						ans.append(a[pos])	
	#print pos
	if len(ans)==0:
		ans = "<NA>"

	return ans

