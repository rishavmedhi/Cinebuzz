#theatre in showing badlapur
#theatre showing badlapur in chennai
#query=raw_input("Ask?")
def gl(query):
	disc=["theatres","theaters","theatre","theater","showtimes","schedule","showing","timings","shows","times","which","show","movie","what","that"]
	for i in range (0,len(disc)):
		query=query.replace(disc[i],"")
	if " in " in query:
		query=query.replace(" in "," ")
	if "   " in query:
		query=query.replace("   "," ")
	if "  " in query:
		query=query.replace("  "," ")
	query=query.lstrip()
	return query
