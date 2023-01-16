
/* Oyuna bulunan renkler */
var buttonColors = ["red", "blue", "green", "yellow"];

/* 0 ile 3 arası sayı üretip buttonColors listesinden bir rengi alıp randomColors listesine pushluyoruz 
   Aynı zaman da her tıkladığımız rengi userClick listesine ekleyip if ile karşılştırıyoruz */
var userClick = [];
var randomColors = [];

/* Oyunun başlyıp başlamayacağını kontrol etmek için kullanıyoruz eğer bu koşulu koymazsak oyun oynanırken
   her tuşa bastığımızda oyun başa saracak */
var start = false;
var level = 0;

//Oyunun başlama kısmı 
$(document).keypress(function() {
  if (!start) {
    $("#level-title").text("Level " + level);
    nextSequence();
    start = true;
  }
});

$(".btn").click(function() {
//  Bastığımız tuşun id sini, yani rengini alıyoruz ve bir değişkene atıyoruz ve listeye pushluyoruz
  var userChosenColour = $(this).attr("id");
  userClick.push(userChosenColour);
// Sesi çalıyoruz ve animasyonu ekliyoruz
  makeSound(userChosenColour);
  addPressed(userChosenColour);
  
  var currentLevel = userClick.length-1;
  checkAnswer(currentLevel);
});

function checkAnswer(currentLevel) {

    if (randomColors[currentLevel] === userClick[currentLevel]) {
      if (userClick.length === randomColors.length){
        setTimeout(function () {
          nextSequence();
        }, 1000);
      }
    } else {
      makeSound("wrong");
      $("body").addClass("game-over");
      $("#level-title").text("Game Over, Press Any Key to Restart");

      setTimeout(function () {
        $("body").removeClass("game-over");
      }, 200);

      startOver();
    }
}


function nextSequence() {
  userClick = [];
  level++;
  $("#level-title").text("Level " + level);
  var rn = Math.floor(Math.random() * 4);
  var randomColor = buttonColors[rn];
  randomColors.push(randomColor);

  $("#" + randomColor).fadeIn(100).fadeOut(100).fadeIn(100);
  makeSound(randomColor);
}

function addPressed(currentColor) {
  $("#" + currentColor).addClass("pressed");
  setTimeout(function () {
    $("#" + currentColor).removeClass("pressed");
  }, 100);
}

function makeSound(name) {
  var audio = new Audio("sounds/" + name + ".mp3");
  audio.play();
}

function startOver() {
  level = 0;
  randomColors = [];
  start = false;
}


/*
$(document).on('keydown', function(event){
    var choiceList = [];
    $('h1').text('level '+level);
    var rn = Math.floor(Math.random()*4);
    var newbutton = $('.btn')[rn].id;
    makeSound(newbutton);
    addPressed(newbutton);
    compList.push(newbutton);
    for (var i=0;i<compList.length;i++){
        $('.btn').on('click', function(event){
        var color = event.currentTarget.id;
        addPressed(color);
        makeSound(color);
        console.log(compList[i]);
        console.log(choiceList[i]);
        if (compList[i] === choiceList[i]){
            level++
        else{

            level = -111111
        }
    })
    };

    }});

function makeSound(clr){
  var sound = new Audio('sounds/'+clr + '.mp3');
  sound.play();
};

function addPressed(clr){
  $('#'+clr).addClass('pressed');
  setTimeout(function() {
  $('#'+clr).removeClass('pressed');
  }, 200);
}
*/




