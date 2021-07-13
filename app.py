from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/words/<word>')
def start(word):
    list_of_anagrams = []
    with open('words.txt') as f:
        lines = f.readlines()
        for line in lines:
            if sorted(line.strip()) == sorted(word.upper()):
                list_of_anagrams.append(line.strip())
    return render_template('index.html', anagrams=list_of_anagrams)


if __name__ == '__main__':
    app.run(debug=True)





