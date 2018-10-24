# Cinebuzz
This project called “CINEBUZZ” is a query handling system aimed particularly for movie lovers and for those who seek movie details.

This project accepts queries from users and depending upon the form of query, it displays two types of results
- Details of the movie as entered in the query
- Details of the theatres showing the movie which was mentioned in the query

The entire query processing application is made using Python and data for displaying results is stored in databases of MySQL and MongoDB.

The data is regularly updated for new content and for this we have web crawlers which are also made using Python.

The crawlers extracts theatre details and movie timings from BookMyShow.com.

The movie details are extracted from IMDb.

The front-end of the project i.e. the website is made using HTML and CSS. The queries are transferred to backend via Python programs that filters the query to extract the necessary details and sends it to the appropriate application.

The results are displayed on the website using JavaScript and Ajax calls.
