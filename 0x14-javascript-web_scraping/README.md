*Javascript - Web scraping*

we are going to solve:

0- Write a script that reads and prints the content of a file.

The first argument is the file path
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object

1- Write a script that writes a string to a file.

The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8
If an error occurred during while writing, print the error object

2- Write a script that display the status code of a GET request.

The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
You must use the module request

3- Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

The first argument is the movie ID
You must use the Star wars API with the endpoint http://swapi.co/api/films/:id
You must use the module request

4- Write a script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is the API URL of the Star wars API: http://swapi.co/api/films/
Wedge Antilles is character ID 18
You must use the module request

5- Write a script that gets the contents of a webpage and stores it in a file.

The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module request

6- Write a script that computes the number of tasks completed by user id.

The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
You must use the module request

100- Write a script that prints all characters of a Star Wars movie:

The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line
You must use the Star wars API
You must use the module request

101- Write a script that prints all characters of a Star Wars movie:

The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line in the same order of the list “characters” in the /films/ response
You must use the Star wars API
You must use the module request

102- Write a Javascript script that takes in 3 strings and sends a search request to the Twitter API

Use the Twitter API search endpoint
Use the Application-only authentication flow to do a search request
Create an Twitter application here
The first argument must be the Consumer Key (API Key)
The second argument must be the Consumer Secret (API Secret)
The third argument must be the search string
Display only 5 results in the following format: [<Tweet ID>] <Tweet text> by <Tweet owner name> (see example below)
Only these modules are allowed: request, base-64 and utf8
You don’t need to check arguments passed to the script (number or type) 