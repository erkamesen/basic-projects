var imgList = ['/images/dice1.png','/images/dice2.png','/images/dice3.png',
'/images/dice4.png','/images/dice5.png','/images/dice6.png'];



var heading = document.querySelector('h1');



function gameStart() {
var rn1 = Math.floor(Math.random()*imgList.length);
var rn2 = Math.floor(Math.random()*imgList.length);
var img1 = document.querySelector('img.img1');
var img2 = document.querySelector('img.img2');

img1.src = imgList[rn1];
img2.src = imgList[rn2];

if (rn1<rn2){
    heading.textContent = 'Player 2 Wins';
}
else if (rn1 === rn2){
    heading.textContent = 'DRAW';
}
else {
    heading.textContent = 'Player 1 Wins';
}
};

