Express application generator
=============================

This tool can be used to quickly create an application skeleton

Installation of NodeJs Express Generator
----------------------------------------
First go to your nodejs express app and run
```
sudo npm install express-generator -g
```

To create an express skeleton app called HelloWorld run 
```
express HelloWorld
```

And install dependencies

```
cd HelloWorld
npm install
```

The directory structure looks like the following

```
.
├── app.js
├── bin
│   └── www
├── package.json
├── public
│   ├── images
│   ├── javascripts
│   └── stylesheets
│       └── style.css
├── routes
│   ├── index.js
│   └── users.js
└── views
    ├── error.jade
    ├── index.jade
    └── layout.jade

```

To run the app, write

```
npm start
```

To run your app in debug mode, launch
```
DEBUG=HelloWorld:* npm start
```

Folder structure
----------------
The folders is used in the skeleton are
  * Bin: Contains libraries of the framework. For example, the app contains www file, that is used to run the HTTP server
  * Public: Contains javascript, css and images
  * Routes: Contains all routes of the app, grouped in files. The index file contains routes that starts by /, the users file contains all routes that starts by /users/, etc
  * Views: Contains all views of the app. The views is writing in Jade syntax. For more information, visit [Jade template engine](http://jade-lang.com/)

Nodemon to reload your app
--------------------------
When you develop a NodeJs app, you will need to restart your app each time you make a change. There are a package that reload your application each time it changes. It call **Nodemon**. To install it, use the following command
```
npm install -g nodemon
```

Then you can start your app with
```
nodemon
```
