function getRecommendations(){

let movie=document.getElementById("movieInput").value;

movie=encodeURIComponent(movie);

let container=document.getElementById("results");

container.innerHTML=`
<div class="loader-container">
<div class="loader"></div>
<p>Fetching AI recommendations...</p>
</div>
`;

fetch("http://127.0.0.1:5000/recommend/"+movie)

.then(res=>res.json())

.then(data=>{

container.innerHTML="";

if(!data.recommendations || data.recommendations.length===0){

container.innerHTML=`
<div class="loader-container">
<h3>No movie found 😢</h3>
<p>Try searching a valid movie name</p>
</div>
`;

return;

}

data.recommendations.forEach(function(movie){

let card=document.createElement("div");

card.className="movie-card";

card.innerHTML=`
<img src="${movie.poster}">
<h3>${movie.title}</h3>
<p>⭐ Rating: ${movie.rating}</p>
`;

container.appendChild(card);

});

})

.catch(error=>{

container.innerHTML=`
<div class="loader-container">
<h3>Error loading recommendations</h3>
</div>
`;

});

}


function autocomplete(){

let query=document.getElementById("movieInput").value;

fetch("http://127.0.0.1:5000/search/"+query)

.then(res=>res.json())

.then(data=>{

let box=document.getElementById("suggestions");

box.innerHTML="";

data.forEach(function(movie){

let item=document.createElement("div");

item.innerText=movie;

item.onclick=function(){

document.getElementById("movieInput").value=movie;

box.innerHTML="";

}

box.appendChild(item);

});

});

}


function loadTrending(){

fetch("http://127.0.0.1:5000/trending")

.then(res=>res.json())

.then(data=>{

let container=document.getElementById("trending");

container.innerHTML="";

data.forEach(function(movie){

let card=document.createElement("div");

card.className="movie-card";

card.innerHTML=`<h3>${movie}</h3>`;

card.onclick=function(){

document.getElementById("movieInput").value=movie;

getRecommendations();

}

container.appendChild(card);

});

});

}


window.onload=function(){

loadTrending();

}