const express = require('express') // import express.js as express
const app = express() // create app variable from express function ?
const port = 3000 // create variable for listen port - - 3000 - - 


app.get('/', (req, res) => {
    res.send('<h1 style="color:red;">Hello World!</h1>')
  }) // if client send a get request this function is our response.
  
app.get('/contact', (req, res) => {
    res.send('<form> Your Message: <input type="text"> <button><input type="submit"></button></form1>')
  }) // This is /contact route

app.get('/about', (req, res) => {
    res.send('<img src="https://avatars.githubusercontent.com/u/120065120?v=4"> <br><p style="color:#5d58be">\
    Hi there, I\'m erkamesen </p> <p style="color:#3e1128"> I graduated from Karabuk University as Energy Systems Engineer and at the same time,\
     I am a Computer Programming student at Anadolu University.I love coding and creating new projects with what I have learned. I\'ve 1.5 years of \'CNC Programming-Operator\'\
      experience. I\'ve been in the music industry for 14 years. The instruments that I can play are the guitar, drums and piano.</p>')
  }) // This is /about route
    

// app.listen(3000);

app.listen(port, () => {
    console.log(`http://127.0.0.1:${port}`) // localhost:port
  }) 

// nodemon server.js = FLASK_DEBUG=True


