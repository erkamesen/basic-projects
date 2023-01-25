from flask import Flask, render_template, request

translator = {
    "q": " --.-", "w": " .--", "e": " .", "r": " .-.", "t": " -",
    "y": " -.--", "u": " ..-", "ı": " ..", "o": " ---", "p": " --",
    "ğ": " --.-.", "ü": " ..--", "a": " .-", "s": " ...", "d": " -..",
    "f": " ..-.", "g": " --.", "h": " ....", "j": " .---", "k": " -.-",
    "l": " .-..", "ş": " .--..", "i": " .-..-", ",": " --..--", "z": " --..",
    "x": " -..-", "c": " -.-.", "v": " ...-", "b": " -...", "n": " -.",
    "m": " --", "ö": " ---.", "ç": " -.-..", ".": " .-.-.-", '0': ' -----',
    '1': ' .----', '2': ' ..---', '3': ' ...--', '4': ' ....-', '5': ' .....',
    '6': ' -....', '7': ' --...', '8': ' ---..', '9': ' ----.', '?': ' ..--..',
    "'": ' .----.', '!': ' -.-.--', '/': ' -..-.', '(': ' -.--.', ')': ' -.--.-',
    '&': ' .-...', ':': ' ---...', ';': ' -.-.-.', '=': ' -...-', '+': ' .-.-.',
    '-': ' -....-',  '_': ' ..--.-',  '"': ' .-..-.',  '$': ' ...-..-',  '@': ' .--.-.',
    '¿': ' ..-.-', '¡': ' --...-',
}

def toMorse(sentence):
    code = str.maketrans(translator)
    return sentence.translate(code)

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userInput = request.form.get('msg').lower()
        return render_template('index.html', mors=toMorse(userInput), msg=userInput)
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
