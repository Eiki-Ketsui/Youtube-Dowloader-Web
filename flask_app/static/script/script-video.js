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
    print(qualitevideo[i])

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
  
        if (typededownload == "2160p")
    {   
        docselec(typededownload)
        for(i > qualitevideo - 1){
        document.getElementById(qualitevideo[i]).removeAttribute('name')
        document.getElementById(qualitevideo[i]).setAttribute("class","desactive")
        print(qualitevideo[i])
        }

      
    }
/** 
    while ( i <= qualitevideo.length-1) {
    
print("quality video :", qualitevideo[i] , type(qualitevideo[i]), "typededownload :" ,typededownload)
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
    */
    console.log("le texte a break")
    document.getElementById("result").setAttribute("name","type")
    document.getElementById("result").setAttribute("value",typededownload)
}

function set_inactive(typededownload){
    let text;
    let i = 0;
    while ( i <= qualitevideo.length -1) {
        if (qualitevideo[i] == typededownload){
            console.log(qualitevideo[i],typededownload)
            continue
        }
        else{
            document.getElementById(qualitevideo[i]).setAttribute("class","desactive")
           
        }
     i++;
    }


}

function docselec(typededownload){
        document.getElementById(typededownload).removeAttribute('desactive')
        document.getElementById(typededownload).setAttribute("class","active")
        document.getElementById(typededownload).setAttribute("name",typededownload)


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

document.getElementById("480p").onclick = function() 
{
    typededownload = "480p"

    choix_type_telechargement(typededownload)

}

document.getElementById("240p").onclick = function() 
{
    typededownload = "240p"

    choix_type_telechargement(typededownload)

}

document.getElementById("160kbps").onclick = function() 
{
    typededownload = "160kbps"

    choix_type_telechargement(typededownload)

}

document.getElementById("50kbps").onclick = function() 
{
    typededownload = "50kbps"

    choix_type_telechargement(typededownload)

}