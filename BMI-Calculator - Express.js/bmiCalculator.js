const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const port = 5000;

app.use(bodyParser.urlencoded({extended:true}))

app.get("/", (req, res) => res.sendFile(__dirname+"/index.html"))

app.post("/", (req, res) => {
    var height = parseFloat(req.body.height);
    var weight = parseFloat(req.body.weight);
    var BMI = weight / (height/100)**2;
    res.send(`Your BMI is ${BMI}`)

})



app.listen(port, () => console.log(`http://127.0.0.1:${port}`));
