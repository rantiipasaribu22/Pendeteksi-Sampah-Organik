from flask import Flask, render_template, request
import os
import cv2
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO("weights/best.pt")

UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    labels = []
    filename = None

    if request.method == "POST":
        if "image" not in request.files:
            return render_template("index.html", labels=["Tidak ada file."])

        file = request.files["image"]
        if file.filename == "":
            return render_template("index.html", labels=["Tidak ada file dipilih."])

        if file:
            # Simpan file upload
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], "uploaded.jpg")
            file.save(filepath)

            # Deteksi objek
            results = model.predict(source=filepath, conf=0.5, save=False)
            annotated = results[0].plot()
            cv2.imwrite(filepath, annotated)

            # Ambil label hasil deteksi
            labels = list(set([model.names[int(cls)] for cls in results[0].boxes.cls]))

            return render_template("index.html", labels=labels, filename="uploaded.jpg")

    return render_template("index.html", labels=labels, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
