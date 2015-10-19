function abc(){
$.ajax({
url:"/cgi-bin/movie_eng.py",
data:{query:$("#search").val().trim()},
type:"GET",

success:function(data){
$("#res").html("");
var json=JSON.parse(data);
if(Object.keys(json)[0]=="theatre")
{
var m=json["theatre"]
var img=$("<img id=\"img_link\" style=\"display:block;margin-left:auto;margin-right:auto;\"> ");
img.attr("src",m[0]["img_link"]);
$("#res").append(img);
$("#res").append("<br /><h3>Rating:"+m[0]["rating"]+"</h3><br />");
$("#res").append("<h3>Director:"+m[0]["director"]+"</h3><br />");
$("#res").append("<h3>Genre:"+m[0]["genre"]+"</h3><br />");
$("#res").append("<h3>Release Date:"+m[0]["rel_date"]+"</h3><br />");
$("#res").append("<h3>Duration:"+m[0]["duration"]+"</h3><br />");
$("#res").append("<h3>City:"+m[0]["city"]+"</h3><br />");
$("#res").append("<h3>Language:"+m[0]["language"]+"</h3><br />");
$("#res").append("<h3>Cast:"+m[0]["cast"]+"</h3><br />");
$("#res").append("<h3>Synopsis:<br /><h6><p>"+m[0]["synopsis"]+"</p></h6><br />");
$.each(m,function(index,value){
$("#res").append("<h3>Theatre:"+value["theatrename"]+":</h3>");
$("#res").append("<h3>"+value["times"]+"</h3><br />");

});
}
if(Object.keys(json)[0]=="movie")
{
var m=json["movie"]
var img=$("<img id=\"img_link\" style=\"display:block;margin-left:auto;margin-right:auto;\"> ");
img.attr("src",m[0]["img_link"]);
$("#res").append(img);
$("#res").append("<br /><h3>Movie:"+m[0]["movie"]+"</h3><br />");
$("#res").append("<br /><h3>Genre:"+m[0]["genre"]+"</h3><br />");
$("#res").append("<h3>Release:"+m[0]["release"]+"</h3><br />");
$("#res").append("<h3>Music:"+m[0]["music"]+"</h3><br />");
$("#res").append("<h3>Producer(s):"+m[0]["producer"]+"</h3><br />");
$("#res").append("<h3>Director:"+m[0]["director"]+"</h3><br />");
$("#res").append("<h3>Writer:"+m[0]["writer"]+"</h3><br />");
$("#res").append("<h3>Editor:"+m[0]["editor"]+"</h3><br />");
$("#res").append("<h3>Cinematographer:"+m[0]["cinematographer"]+"</h3><br />");
$("#res").append("<h3>Story:<br /><h6><p>"+m[0]["story"]+"</p></h6><br />");
$("#res").append("<h3>Cast:-</h3><br />");
$.each(m[0]["cast"],function(key,value){
$("#res").append("<h3>"+key+":"+value+"</h3><br />");
});
}
},
error:function(err){
console.log(err);
}
});
}

$(document).ready(function(){
$("#search").on("keypress",function(e){
if(e.keyCode===13){
abc();
}

});
$("#go").on("click",abc);

});
