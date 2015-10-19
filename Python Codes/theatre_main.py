#retrieval code for theatre module
import theatre_gla
import theatre_search
def main(query):
	#query=raw_input("Ask? ").lower()
	query=theatre_gla.gl(query)
	#print query
	result=theatre_search.search(query)
	#print result
	return result
