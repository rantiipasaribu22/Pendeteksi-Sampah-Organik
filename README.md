# 🗑️ Organic Waste Detection System Using YOLOv8

A smart web-based image classification system to automatically detect and classify **organic waste** using YOLOv8 object detection models. This system is designed to support sustainable waste management by providing real-time organic waste recognition from user-submitted images.

---

## 🧱 Background

Urban environments face increasing challenges in waste management. Improper sorting between organic and inorganic waste often leads to inefficient recycling processes and environmental issues. This project aims to address this by using a deep learning-based detection system that can automatically classify organic waste from images, improving awareness and supporting eco-friendly practices.

---

## 🎯 Objectives

- ✅ Build a YOLOv8-based model to detect organic waste in images
- ✅ Deploy a web interface for image upload and detection
- ✅ Deliver fast and accurate feedback to users
- ✅ Contribute to smart and sustainable waste management solutions

---

## 📂 Dataset Information

### 🧪 Organic Waste Dataset
- **Source:** [Roboflow Universe – Klasifikasi Sampah Berdasarkan Nama](https://universe.roboflow.com/siscer-project/klasifikasi-sampah-berdasarkan-nama/dataset/15/images?split=train)
- **Classes:** Organic waste (e.g., food scraps, leaves, natural debris)
- **Images:** Several hundred annotated images
- **Format:** YOLOv8-compatible bounding boxes

### 🍎 Fruit & Vegetable Dataset (Extended Classification)
- **Source:** [Roboflow Universe – Buah Sayuran](https://universe.roboflow.com/pcb-t7dcy/buah-sayuran/dataset/1)
- **Classes:** Various organic food items (e.g., fruits, vegetables)
- **Use Case:** Extended organic waste classification, training augmentation
- **Format:** YOLOv8-compatible

---

## ⚙️ Implementation Process

1. **Dataset Preparation** – Labeled via Roboflow platform  
2. **Model Training** – YOLOv8 used to train organic waste detection model  
3. **Web Development** – Flask used to build upload and detection interface  
4. **Model Integration** – System loads trained model and processes user images  
5. **Visualization** – Results shown with bounding boxes and class confidence  

---

## 🚀 How to Use the System (Web-Based)

### 📦 1. Install Requirements
```bash
pip install flask ultralytics opencv-python roboflow numpy
```
### 🛠️ 2. Place Trained YOLOv8 Weights
```bash
weights/best.pt  # Model trained for organic waste detection

```
### 🖥️ 3. Run the Application
```bash
python app.py

```
Then open your browser and go to:
```
http://localhost:5000/
```
### 🧪 4. Use the Interface
![image](https://github.com/user-attachments/assets/4cdd6e80-8c24-499b-bfab-355ca6bdb26b)

---

## 📊 Model Performance
| Metric           | Value    |
|------------------|----------|
| Precision        | 96.70%   |
| Recall           | 90.88%   |
| mAP@0.5          | 96.87%   |
| mAP@0.5:0.95     | 89.77%   |
| Fitness Score    | 90.48%   |

---

## 👩‍💻 Developed By
Rantika Darmayanti Br Pasaribu
Final Year Project – 2025
"Organic Waste Detection System Using YOLOv8"


