$(function(){
    var xsl = $("#inputXsl").val();
    var url = $("#inputUrl").val();

    var elements = xsl.substring(xsl.indexOf("Source: ") + 8).split("\n");
    if(elements.length > 1){
        
        var res = elements[1].split(",");
        var resources = Array();
        
        for(var i = 0; i < res.length; i=i+6){
            var r = {"mountPoint":url+res[i+0], "listeners": res[i+3]};
            resources.push(r);
        }
        console.log(resources);
        
    }else{
        console.log("La estructura no es correcta");
    }
});
