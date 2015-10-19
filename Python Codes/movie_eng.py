#!/usr/bin/python -v3
import cgi,cgitb
import movie_test
import theatre_main
import json
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
query=fs.getvalue("query")
query=query.lower()
try:
	if "movie" in query or "film" in query or "cinema" in query:
		ans=json.dumps(movie_test.main(query))
	elif "theatre" in query or "theater" in query:
		ans=json.dumps(theatre_main.main(query))
	else:
		ans={}
except:
	ans={}
print ans

