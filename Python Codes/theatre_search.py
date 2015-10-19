#search module for theatre module v3.0
#queries handled
#theatres in place-name showing movie-name
#movie-name timings/times/shows/showtimes in place-name
#theatres which/that show movie-name in place-name
#theatres showing movie-name in place-name
#theatre-name timings in place-name
#shows in theatre-name place-name
#movie-name showtimes in place-name

import MySQLdb
db=MySQLdb.connect("localhost","root","1","brainse")
cursor=db.cursor()
def fetching(row):
	return row[1],row[3],row[5],row[7],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17]

def display():
	c=[]
	results=cursor.fetchall()
	for row in results:
		th_name,city,m_name,times,img_link,releasedate,duration,director,language,genre,cast,rating,synopsis=fetching(row)
		avai_cities=availablecity(str(m_name))
		d={"theatrename":th_name,"city":city,"moviename":m_name,"times":times,"img_link":img_link,"rel_date":releasedate,"duration":duration,"director":director,"language":language,"genre":genre,"cast":cast,"rating":rating,"synopsis":synopsis,"avai_cities":avai_cities}
		c.append(d)
	disp={"theatre":c}
	return disp

def availablecity(moviename):
	cities=[]
	asql="SELECT distinct(`city`) from `showtimes` where `moviename`='%s';"%(str(moviename))
	cursor.execute(asql)
	results1=cursor.fetchall()
	for row in results1:
		r=str(row[0])
		r=r.replace("(","")
		r=r.replace(")","")
		cities.append(r)
	return cities	

def sql_mod(res1,res2):	
	sql=[]
	sql.append("SELECT * from `showtimes` where `city`='%s' and `moviename` LIKE '%s';"%(str(res1),str("%"+res2+"%")))
	sql.append("SELECT * from `showtimes` where `theatrename` LIKE '%s' and `city`='%s';"%(str("%"+res1+"%"),str(res2)))
	sql.append("SELECT * from `showtimes` where `theatrename` LIKE '%s' and `moviename`='%s';"%(str("%"+res1+"%"),str(res2)))
	#sql.append("SELECT distinct(`city`) from `showtimes` where `moviename`='%s';"%(str(res1)))
	return sql
	
def find(query1,query2):
	flag=0
	qlist=sql_mod(query1,query2)
	for i in range(0,len(qlist)):
		#print qlist[i]
		res=cursor.execute(qlist[i])
		if not res:
			continue
		else:	
			#print "found" 
			#if i==0 or i==2:
			#	x=display(0)
			x=display()
			flag=1
			break
	if flag==1:
		return x,1
	else:
		return "n/a",0
def search(query):
	#query="ab ambala"
	query=query.rsplit(" ",1)
	query1=query[0]
	query2=query[1]
	ans,status=find(query1,query2)
	if status==0:
		ans,status=find(query2,query1)
	#print ans
	return ans
