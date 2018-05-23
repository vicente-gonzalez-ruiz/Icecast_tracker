var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {

var request = require('request');
var url = "http://150.214.150.68:4551";

request(url + "/status2.xsl", function (error, response, body) {
        if (!error && response.statusCode == 200) {
            
            var xsl = body.substring(body.indexOf("<pre>") + 5, body.indexOf("</pre>"))
            
            res.render('index', { title: "Express", xsl: xsl, url:url, scripts: ["javascripts/parserXsl.js"] });
        }
    })
});

router.get('/prueba', function(req, res, next) {
  res.send('Es una prueba');
});


module.exports = router;
