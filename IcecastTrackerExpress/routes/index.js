var express = require('express');
var router = express.Router();
var url = require('url');

/* Array of icecast servers */
var urls = ['http://ugkkf004b1ec.giaku.koding.io:8000', 'http://150.214.150.68:4551'];

/* Base url */
router.get('/', function(req, res, next) {

    console.log(getAllMedia());
    
    // Print an array with all media with the current listeners
    res.send(getAllMedia());
});

/* Path with any content (Except the base url) */
router.get('/*', function(req, res, next) {

    var url_parts = url.parse(req.url, true);
    var filename = url_parts.path.substring(1);
    
    // Get the url to the media whith the minimum listeners
    var redirectTo = getMinListenerMedia(filename);
    
    if(!redirectTo){
        console.log("Not found " + redirectTo);
        
        // Not found
        res.sendStatus(404);
    }else{
        console.log("Redirecting to " + redirectTo);

        // Redirect to this media
        res.redirect(307, redirectTo);
    }
});

// Get the media with the minimum listeners
function getMinListenerMedia(name){
    var requestSync = require('sync-request');

    var path="";
    var minListeners = -1;
    
    for(var i = 0; i < urls.length; i++){
        try{
            var result = requestSync('GET', urls[i]+"/status2.xsl").getBody().toString();
            
            var xslAux = result.substring(result.indexOf("<pre>") + 5, result.indexOf("</pre>"));
            var xsl = xslAux.substring(xslAux.indexOf("Source: ") + 8).split("\n");
        
            if(xsl.length > 1){
                var data = xsl[1].split(",");
        
                for(var j = 0; j < data.length - 1; j=j+6){
                    
                    if(data[j+0].substring(1) == name){
                    
                        var mountPointUrl = urls[i]+data[j+0];
                        var mountPountListeners = data[j+3];

                        //console.log("minListeners="+minListeners);
                        //console.log(mountPountListeners + "<" + minListeners + "=" + (mountPountListeners < minListeners).toString());
                    
                        if(minListeners == -1 || mountPountListeners < minListeners){
                            path = mountPointUrl;
                            minListeners = mountPountListeners;
                        }
                    }
                    
                }
            }else{
                console.log("La estructura no es correcta");
            }
        }catch(e){
            console.log("EXCEPCION" + e);
        }
    }
    
    return path;
}

// Get an array with all media and the actual listeners
function getAllMedia(){
    var requestSync = require('sync-request');

    var mountPoints = Array();
    
    for(var i = 0; i < urls.length; i++){
        try{
            var result = requestSync('GET', urls[i]+"/status2.xsl").getBody().toString();
            
            var xslAux = result.substring(result.indexOf("<pre>") + 5, result.indexOf("</pre>"));
            var xsl = xslAux.substring(xslAux.indexOf("Source: ") + 8).split("\n");
        
            if(xsl.length > 1){
                var data = xsl[1].split(",");
        
                for(var j = 0; j < data.length - 1; j=j+6){
                    var mountPointUrl = urls[i]+data[j+0];
                    var mountPountListeners = data[j+3];
                    mountPoints.push([mountPointUrl, mountPountListeners]);
                }
            }else{
                console.log("La estructura no es correcta");
            }
        }catch(e){
            console.log("EXCEPCION" + e);
        }
    }
    
    return mountPoints;
}

module.exports = router;
