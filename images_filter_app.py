from flask import Flask, render_template, request, redirect, send_file
from flask_bootstrap import Bootstrap
from app_functions import filter


app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def index():
    """Отображает домашнюю страницу.
    Загружает файл изображения."""
    if request.method == "POST":

        # Если файл не загружен, то вернуть домашнюю страницу
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        # Если у файла нет имени, то вернуть домашнюю страницу
        if file.filename == "":
            return redirect(request.url)


    return render_template("index.html")


@app.route("/downloading", methods = ["GET", "POST"])
def downloading():
    """Отображает страницу загрузки, преобразовывает
     изображение в скетч."""
    filestr = request.files["file"].read()
    sketch = filter(filestr)
    return render_template("downloading.html", sketch=sketch)


@app.route("/download")
def download_sketch():
    """Отправка файла пользователю."""
    file = "static/sketch/sketch.png"
    return send_file(file, as_attachment=True)


# Перевод на страницу с ошибкой в случае загрузки файла неправильного формата
@app.errorhandler(500)
def error_file(error):
    return render_template("error-file.html")


if __name__ == "__main__":
    app.run(debug=False)

