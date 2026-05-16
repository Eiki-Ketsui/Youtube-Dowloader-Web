let lien;
let videooumusique = ["Video","Musique"];

let strVideo = videooumusique[0];
let strMusique = videooumusique[1];

let choiseactive = ["active","desactive"];
let typededownload = "Video";


let button_download = document.getElementById("download-btn");
let button_video = document.getElementById(strVideo);
let button_audio = document.getElementById(strMusique);

let qualiteaudio =  ["160kbps","50kbps"];
let qualitevideo = ["2160p","1440p","1080p","720p","480p","360p","240p","144p"];


let qualitechoisisvideo = "1080p";


function Focus_traitement_audio(id)
{
    

    desactiveother(id);
};




function Focus_traitement_video(id)
{
    desactiveother(id);
};



function desactiveother(idignored)
{
    if(idignored.endsWith("p")){
        for(let i = 0; i <= qualitevideo.length - 1;i++)
            {
                if(qualitevideo[i] ==idignored)
                    {
                        document.getElementById(qualitevideo[i]).setAttribute("class","mini active");
                        document.getElementById("buttonqualityvideo").setAttribute("value",idignored);

                    }
                else
                    {                                
                        document.getElementById(qualitevideo[i]).setAttribute("class","mini desactive");
                       


                    };
            };
    }
    else{
        for(let i = 0; i <= qualiteaudio.length - 1;i++)
        {
            if(qualiteaudio[i] ==idignored)
                {
                    document.getElementById(qualiteaudio[i]).setAttribute("class","mini active");
                    document.getElementById("buttonqualityaudio").setAttribute("value",idignored);
                    
                }
            else
                {
                    document.getElementById(qualiteaudio[i]).setAttribute("class","mini desactive");
                };
        };

    };
};




button_video.onclick = function() 
{
    typededownload = strVideo;

    choix_type_telechargement(typededownload);
    document.getElementById("download_type").setAttribute("value","Video");


};



button_audio.onclick = function() 
{
    typededownload = strMusique;


    choix_type_telechargement(typededownload);
    document.getElementById("download_type").setAttribute("value","Musique");

};



   

function choix_type_telechargement(typededownload)
{
        
    docselec(typededownload);
    let text;
    let i = 0;

        if (typededownload == "Musique")
        {
            docselec(typededownload)
            document.getElementById(strVideo).removeAttribute('name');
            document.getElementById(strVideo).setAttribute("class","desactive");

        };

        if (typededownload == "Video")
        {   
            docselec(typededownload)
            document.getElementById(strMusique).removeAttribute('name');
            document.getElementById(strMusique).setAttribute("class","desactive");
        
        };
        document.getElementById("download_type").setAttribute("value","Video");

    
}

function docselec(typededownload){
        document.getElementById(typededownload).removeAttribute('desactive');
        document.getElementById(typededownload).setAttribute("class","active");
        


} 

/* ENDING BUTTON */

document.getElementById("160kbps").onclick = function()
{
    Focus_traitement_audio("160kbps");
};

document.getElementById("50kbps").onclick = function()
{
    Focus_traitement_audio("50kbps");
};



document.getElementById("2160p").onclick = function()
{
    Focus_traitement_video("2160p");
};


document.getElementById("1440p").onclick = function()
{
    Focus_traitement_video("1440p");
};

document.getElementById("1080p").onclick = function()
{
    Focus_traitement_video("1080p");
};

document.getElementById("720p").onclick = function()
{
    Focus_traitement_video("720p");
};

document.getElementById("480p").onclick = function()
{
    Focus_traitement_video("480p");
};

document.getElementById("360p").onclick = function()
{
    Focus_traitement_video("360p");
};

document.getElementById("240p").onclick = function()
{
    Focus_traitement_video("240p");
};

document.getElementById("144p").onclick = function()
{
    Focus_traitement_video("144p");
};




