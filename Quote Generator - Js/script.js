let apiQuotes = [];
var quoteContainer = document.querySelector("#quote-container");
var quoteButton = document.querySelector("#new-quote");
var twitterButton = document.querySelector("#twitter");
var quotesText = document.querySelector("#quote");
var quotesAuthor = document.querySelector("#author");
var loader = document.querySelector("#loader");


/* API ile iletişim ve DOM */
async function getQuotes() {
    loadingSpinner();
    const apiURL = 'https://type.fit/api/quotes';
    try{
        /* API Kısmı */
        const response = await fetch(apiURL);
        apiQuotes = await response.json();
        var newQuotes = apiQuotes[getRandomNumber(apiQuotes)];
        /* DOM Kısmı */
        quotesText.textContent = newQuotes.text
        /* İsimleri 'null' olarak gelen sözleri Unknown olarak değiştiriyoruz. */
        if (quotesAuthor.textContent == "") {
            quotesAuthor.textContent = "Unknown"
        } else{
            quotesAuthor.textContent = newQuotes.author
        }
        setTimeout(completeSpinner, 300);

    } catch (error) {
        
    }
}

/* Gelen response arrayin uzunluğunda random sayı üretmek için fonksiyon */
function getRandomNumber(responseList){
    var rn = Math.floor(Math.random()*responseList.length);
    return rn
}


quoteButton.addEventListener("click", getQuotes);
twitterButton.addEventListener("click", function(){
    var twitterUrl = `https://twitter.com/intent/tweet?text=${quotesText.textContent} - ${quotesAuthor.textContent}`;
  window.open(twitterUrl, '_blank');
});


/* Spinner Ayarları */
function loadingSpinner(){
    loader.hidden = false
    quoteContainer.hidden = true
}
function completeSpinner(){
    loader.hidden = true
    quoteContainer.hidden = false
}


/* Çalıştır */
getQuotes();
