//Lets require/import the HTTP module

var http = require('http');


//Lets define a port we want to listen to

const PORT=8080; 


//We need a function which handles requests and send response

function handleRequest(request, response){

    response.end('Hello World');

}


//Create a server

var server = http.createServer(handleRequest);


//Lets start our server

server.listen(PORT);
