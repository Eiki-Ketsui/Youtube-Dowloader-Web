let lien;
let typededownload = "video";

document.getElementById("download-btn").onclick = function() {
 lien = document.getElementById("url").value;
 console.log(lien);
}

document.getElementById("Video").onclick = function() {
 typededownload ="video";
 console.log(typededownload);

}

document.getElementById("Musique").onclick = function() {
 typededownload ="Musique";
 console.log(typededownload);
}

