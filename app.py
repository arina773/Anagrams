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


@app.route('/dictionary')
def dictionari():
    alphabet = 'abcdefghijklmnopqrstuv'
    return render_template('dictionary.html', count=0, is_a_word=False, alphabet=alphabet, cur_word='')


@app.route('/dictionary/<cur_word>')
def dictionary(cur_word):
    count = 0
    alphabet = 'abcdefghijklmnopqrstuv'
    with open('words_dict.txt') as f:
        lines = f.readlines()
        for line in lines:
            if cur_word.upper() == line.strip().upper():
                return render_template('dictionary.html', count=count, is_a_word=True, alphabet=alphabet, cur_word=cur_word)
            elif line.strip().upper().startswith(cur_word.upper()):
                count += 1
    return render_template('dictionary.html', count=count, is_a_word=False, alphabet=alphabet, cur_word=cur_word)


if __name__ == '__main__':
    app.run(debug=True)





