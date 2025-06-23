**#🗑️ Organic Waste Detection System Using YOLOv8**

A smart web-based image classification system to automatically detect and classify organic waste using state-of-the-art YOLOv8 object detection models. The system helps support sustainable waste management by providing instant detection from user-uploaded images.

#🧱 Background
Waste management is a major challenge in urban areas. Improper separation of organic and non-organic waste leads to increased environmental impact and inefficiencies in recycling. This project introduces a computer vision-based solution to assist in classifying waste by detecting organic materials from images automatically.

🎯 Objectives
✅ Build a YOLOv8-based system to detect organic waste from user-submitted images
✅ Enable detection via a clean, accessible web interface
✅ Help raise awareness about waste sorting using real-time feedback
✅ Provide detection results with high accuracy and speed

📂 Dataset Information
🧪 Organic Waste Dataset

Source: Roboflow Universe

Classes: Organic waste (e.g., food scraps, leaves, etc.)

Total Images: Hundreds of annotated waste images

Format: YOLOv8-compatible

⚙️ Implementation Process

Dataset Preparation – Images were labeled and prepared using Roboflow.

Model Training – YOLOv8 was trained on the labeled dataset to detect and classify organic waste.

Web Interface – Built with Flask to support image upload and detection output.

Integration – Detection results are shown on the web UI with bounding boxes and classification info.

🚀 How to Use the System (Web-Based)
📦 1. Install Requirements

bash
Copy code
pip install flask ultralytics opencv-python roboflow numpy  
🛠️ 2. Place Trained YOLOv8 Weights

bash
Copy code
weights/best.pt  # Model trained to detect organic waste  
🖥️ 3. Run the Application

bash
Copy code
python app.py  
🔗 Open in Browser:
http://localhost:5000/

🧪 4. Use the Interface
Upload Image (JPG/PNG) → System detects and highlights organic waste → Displays result with confidence scores

📊 Model Accuracy

Precision: 96.70%

Recall: 90.88%

mAP@0.5: 96.87%

mAP@0.5:0.95: 89.77%

Fitness Score: 90.48%

🌟 System Features
🖼️ Image upload with annotated detection
⚡ Fast and responsive detection using YOLOv8
📊 Display of bounding boxes and class confidence
🧘 Responsive UI (desktop/mobile friendly)

🖼️ UI Preview
![image](https://github.com/user-attachments/assets/30986cfd-e6b5-436e-aeae-8fd0c92a84a7)


👩‍💻 Developed By
Qonita Milla Hanifa
Final Year Project – 2025
Smart Waste Classification using YOLOv8 & Flask

📌 Suggestions for Future Work

Expand to multi-class detection (inorganic vs organic)

Integrate database for logging detections

Add camera support for real-time detection

Deploy to edge devices for field usage (e.g., trash sorting machines)
