import gla
import bulk
import sys
import MySQLdb
conn=MySQLdb.connect("localhost","root","1","brainse")
co=conn.cursor()
def main(query):
	sys.dont_write_bytecode = True
	orig_query=str(query)
	query = gla.gaiml(query)
	flag = 1
	#print "#------------------------AIML------------------#"
	#print query
	for i in query:
		query = gla.gdisc(i)
		#print "#------------------------DISC------------------#"
		#print "Rest :",query
		query,fields = gla.wordmatrix(query)
		if fields=="":
			fields = "<NA>"
		#print "#-----------------------WM---------------------#"
		#print "Rest :",query
		#print "Fields :",fields
		#print "#-----------------------LOG---------------------#"
		query,symbol,wtn,date = gla.logic(query)
		#print "Rest :",query
		#print "Symbol :",symbol
		#print "Values :",wtn
		#print "Date :",date
		try:
			fields.extend(query)
		except:
			fields = []
			fields.extend(query)
		msg = gla.gspl(fields)

		for j in query:
			fields.remove(j)
		if(flag):
			msg = gla.bulkmodules(fields)
			if msg!="<NA>":
				#print "#-------------------BULK--------------------#"
				ans = bulk.getanswer(msg,query,fields,wtn,orig_query)
				if ans!="<NA>":
					a=ans[0]["movie"].lower()
					sql="SELECT `image` FROM `movie` WHERE `name`='%s';"%(a)
					r=co.execute(sql)
					if r:
						res=co.fetchone()
						img="http://"+str(res[0])
					else:
						img="http://cdn.traileraddict.com/img/noposter-319x365.jpg"
					ans[0]["img_link"]=str(img)
					#print ans[0]["movie"]
					answer={"movie":ans}
					return answer
					#for i in ans:
					#	print i
				
					flag = 0
		#print "#---------------------END-----------------------#" 
