function process(){
let msg = document.getElementById("word").value;
let speech = new SpeechSynthesisUtterance();

speech.lang = "en-US";
speech.text = msg;
speech.volume = 1;
speech.rate = 1;
speech.pitch = 1;

window.speechSynthesis.speak(speech);

}