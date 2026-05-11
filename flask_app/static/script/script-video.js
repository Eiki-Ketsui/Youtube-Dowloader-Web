let lien;
let typededownload = "Video";

let button_download = document.getElementById("download-btn")
let button_video = document.getElementById("Video")
let button_audio = document.getElementById("Musique")

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



document.getElementById("Video").onclick = function() 
{
    if (typededownload == "Musique")
    {
        document.getElementById("Video").removeAttribute('desactive')

        document.getElementById("Musique").removeAttribute('name')
        document.getElementById("Musique").setAttribute("class","desactive")
        document.getElementById("Video").setAttribute("class","active")
        document.getElementById("Video").setAttribute("name","Video")

        document.getElementById("result").setAttribute("name","type")
        document.getElementById("result").setAttribute("value","Video")
      

        typededownload = "Video";
    }

console.log(typededownload);

}

document.getElementById("Musique").onclick = function() 
{
    console.log(typededownload);
    typededownload = "Musique"
    if (typededownload == "Musique")
    {
        document.getElementById("Musique").removeAttribute('desactive')

        document.getElementById("Video").removeAttribute('name')
        document.getElementById("Video").setAttribute("class","desactive")
   

        document.getElementById("Musique").setAttribute("class","active")
        document.getElementById("Musique").setAttribute("name","Musique")
        
        document.getElementById("result").setAttribute("name","type")
        document.getElementById("result").setAttribute("value","Musique")

        typededownload == "Musique"
    }

    console.log(typededownload);

}
