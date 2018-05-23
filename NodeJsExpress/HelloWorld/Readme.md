Starting with NodeJs Express framework
======================================

Installation of NodeJs Express
------------------------------
First create a directory named NodeJsExpress and run 
```
npm init
```
This command create a package.json to manage dependencies of the project.
This command prompt your for a number of things such as the name and version. You can hit enter for all promps to accept the default value except for 
```
entry point: (index.js)
```
Enter app.js

Then install Express as a dependency. To do this, run
```
npm install express --save
```


NodeJs Express HelloWorld
-------------------------
To write a helloworld app, create a file called app.js and add the following code to it
```javascript
var express = require('express');
var app = express();

app.get('/', function (req, res) {
  res.send('Hello World!');
});

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
```

The app listens on port 3000. Every request to the root, the app respond with Hello World! message. Otherwise, respond with a 404 Not Found.

To start the HTTP server, run 

```
node app.js
```

And load http://yourdomain:3000 in a browser to see the results
