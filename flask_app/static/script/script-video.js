let lien;
let videooumusique = ["Video","Musique"]

let strVideo = videooumusique[0]
let strMusique = videooumusique[1]

let choiseactive = ["active","desactive"]
let typededownload = "Video";


let button_download = document.getElementById("download-btn")
let button_video = document.getElementById(strVideo)
let button_audio = document.getElementById(strMusique)

let qualiteaudio =  ["160kbps","50kbps"];
let qualitevideo = ["2160p","1440p","1080p","720p","480p","360p","240p","144p"]

/* 

async function loadData() 
{
  let response = await fetch("data.json");
  let data = await response.json();
}


button_download.onclick = function() 
{ 
    lien = document.getElementById("url").value;

    loadData();
    return(console.log("done loading data"))
}
*/

button_video.onclick = function() 
{
    typededownload = strVideo

    choix_type_telechargement(typededownload)

}



button_audio.onclick = function() 
{
    typededownload = strMusique


    choix_type_telechargement(typededownload)

}

function choix_type_telechargement(typededownload){
        
    
    let text;
    let i = 0;
    
    if (typededownload == "Musique")
    {
        docselec(typededownload)
        document.getElementById(strVideo).removeAttribute('name')
        document.getElementById(strVideo).setAttribute("class","desactive")

    }

    if (typededownload == "Video")
    {   
        docselec(typededownload)
        document.getElementById(strMusique).removeAttribute('name')
        document.getElementById(strMusique).setAttribute("class","desactive")
      
    }
  
        console.log(qualitevideo.length)

    while ( i <= qualitevideo.length-1) {
    

    if (qualitevideo[i] == typededownload){

    
        document.getElementById(typededownload).setAttribute("class","active")
        set_inactive(typededownload)
        break
    }
    else{
        document.getElementById(qualitevideo[i]).removeAttribute('name')
        document.getElementById(qualitevideo[i]).setAttribute("class","desactive")
        
    }
    text = "The number is " + i;
    console.log(text,qualitevideo[i] )
    i++
    }
    console.log("le texte a break")
}

function set_inactive(typededownload){
    let text;
    let i = 0;
    while ( i <= qualitevideo.length -1) {
        if (qualitevideo[i] == typededownload){
            continue
        }
        else{
            document.getElementById(qualitevideo[i]).setAttribute("class","desactive")

        }
    }

}

function docselec(typededownload){
        document.getElementById(typededownload).removeAttribute('desactive')
        document.getElementById(typededownload).setAttribute("class","active")
        document.getElementById(typededownload).setAttribute("name",typededownload)
        document.getElementById("result").setAttribute("name","type")
        document.getElementById("result").setAttribute("value",typededownload)

}
/*  minisoo*/
document.getElementById("2160p").onclick = function() 
{
    typededownload = "2160p"

    choix_type_telechargement(typededownload)

}

document.getElementById("1440p").onclick = function() 
{
    typededownload = "1440p"

    choix_type_telechargement(typededownload)

}

document.getElementById("1080p").onclick = function() 
{
    typededownload = "1080p"

    choix_type_telechargement(typededownload)

}

document.getElementById("720p").onclick = function() 
{
    typededownload = "720p"

    choix_type_telechargement(typededownload)

}