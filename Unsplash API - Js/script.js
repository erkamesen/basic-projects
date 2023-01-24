// https://api.unsplash.com/photos/?client_id=YOUR_ACCESS_KEY
const imageContainer = document.querySelector("#image-container");
const loader = document.querySelector("#loader");

let photosArray = [];
let ready = false;
let imagesLoaded = 0;
let totalImages = 0;
let count = 5;

const apiKey = "uJADJPX07Im_tGqky9n0sPrNanCXXPCaelUCTTCpyrs";
const apiUrl = 'https://api.unsplash.com/photos/random/?client_id=uJADJPX07Im_tGqky9n0sPrNanCXXPCaelUCTTCpyrs&count=10';

// Check Image Loaded

function imageLoaded(){
    imagesLoaded++;
    if (imagesLoaded === totalImages) {
        ready = true;
        loader.hidden = true;
    }
}

// Util for DOM Elements

function setAttributes(element, attributes) {
    for (const key in attributes) {
      element.setAttribute(key, attributes[key]);
    }
  }

// Elements 
function displayPhotos() {
    imagesLoaded = 0;
    totalImages = photosArray.length;
    // Run function for each object in photosArray
    photosArray.forEach((photo) => {
      // Create <a> to link to full photo
      const item = document.createElement('a');
      setAttributes(item, {
        href: photo.links.html,
        target: '_blank',
      });
      // Create <img> for photo
      const img = document.createElement('img');
      setAttributes(img, {
        src: photo.urls.regular,
        alt: photo.alt_description,
        title: photo.alt_description,
      });
      // Event Listener, check when each is finished loading
      img.addEventListener('load', imageLoaded);
      // Put <img> inside <a>, then put both inside imageContainer Element
      item.appendChild(img);
      imageContainer.appendChild(item);
    });
  }


// Checking for infinite scroll

window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 1000 && ready) {
      ready = false;
      getPhotos();
    }
  });


// Get Photos

async function getPhotos() {
    try{
        const response = await fetch(apiUrl);
        photosArray = await response.json();
        displayPhotos();

    } catch (error){

    }
}


getPhotos();