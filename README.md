# https-server
Interview Test

Working on fun mini-project!


This code is a Flask web server written in Python.

First, it imports the necessary modules from Flask, which include Flask, request, jsonify, and send_file. It also imports json.

Then it creates an instance of the Flask class, which is used to handle the routing of web requests. Two empty dictionaries are also created: key_value_store and uploaded_files.

Next, it defines several routes for the web server, which determine what the server will do in response to different types of HTTP requests. The first route, '/', returns a simple message of "Welcome to my Flask web server" when accessed via a web browser.

The '/key-value' route is set up to handle HTTP POST requests, which are used to submit data to the server. When a POST request is made to this route, the key_value() function is called. This function retrieves the 'action', 'key', and 'value' fields from the request in JSON format, and then performs different operations based on the value of the 'action' field.

The 'set' action adds a new key-value pair to the key_value_store dictionary, the 'get' action looks up the value associated with the specified key in the dictionary and returns it, the 'get_all' action returns all the data in the dictionary, the 'delete' action deletes the key and value associated with the key in the dictionary, and 'clear' action clears the entire dictionary.

The '/upload' route is set up to handle file uploads, it checks if the file is present in the request and if yes, it saves the file using the save() method of the file object and returns success status.

The '/files' route returns the list of uploaded files.

The '/download/path:filename' route is set up to handle file downloads, it checks if the requested file is present or not and if present it sends the file as an attachment using the send_file() method of Flask.

Finally, the last line of the code tells the script to run the web server when the script is run.
