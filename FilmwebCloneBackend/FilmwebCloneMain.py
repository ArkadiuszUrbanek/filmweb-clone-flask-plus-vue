# Dołączanie modułu flask 
from flask import Flask
from flask import render_template, request, redirect, url_for, flash

# Tworzenie aplikacji
app = Flask("FilmwebApp")


@app.route('/', methods=['GET', 'POST'])
def index():
    # Przesłanie w odpowiedzi stworzonego widoku z pliku HTML (pliki muszą znajdować w folderze "templates")
    return "Hello World!<br>"


# Uruchomienie applikacji w trybie debug
app.debug = True
app.run()
