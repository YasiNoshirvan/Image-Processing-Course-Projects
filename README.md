# 🖼️ Image Processing Course Projects

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white) ![Status](https://img.shields.io/badge/Type-Learning%20Repository-informational)

A collection of **21 hands-on exercises** completed while learning image processing and computer vision with Python. The repository starts with basic image operations and gradually moves into feature matching, video processing, detection, and optical character recognition (OCR).

The goal is to document my learning process, experiment with classical computer vision techniques, and keep the examples in one place for future reference.

## 📚 Topics covered

| Area | Examples |
| --- | --- |
| Image fundamentals | Reading images, drawing, cropping, color channels, and logical operations |
| Image enhancement | Thresholding, morphology, histograms, and CLAHE |
| Feature extraction | Canny and Sobel edges, Harris corners, template matching, and ORB feature matching |
| Video and detection | Webcam color detection, Haar cascades, hand landmarks, face mesh, and QR/barcode reading |
| Practical exercises | Motion detection, license plate localization, and English/Persian OCR |

## 📁 Repository contents

- **`1_...py` to `20_...py`** — individual Python exercises, organized by course order.
- **`21_ConvertImageToTextUsingPytesseractPackage.ipynb`** — OCR experiments using Tesseract.
- **`images/`** — sample images used across the exercises.
- **`videos/`** — sample video inputs.
- **`face and body data/`** — Haar cascade XML files used for detection exercises.

## ⚙️ Getting started

```bash
git clone https://github.com/YasiNoshirvan/Image-Processing-Course-Projects.git
cd Image-Processing-Course-Projects
pip install numpy opencv-python matplotlib imutils
```

Run an exercise individually, for example:

```bash
python 7_EdgeDetection.py
```

Some exercises also use **cvzone, MediaPipe, EasyOCR, pytesseract, qrcode, or pyzbar**. Install these as needed for the specific script. The Tesseract OCR engine (and relevant language data) must be installed separately for the notebook.

> **Setup note:** These files reflect coursework and some still contain local Windows paths such as `D:/Training Image Processing/...`. Update image/video paths to match the cloned `images/` and `videos/` folders before running. Some notebook filenames also need to be matched to the supplied sample files.

## 🔎 Related standalone projects

I expanded several course exercises into separate small projects:

- 🚗 [Smart Parking Space Detection](https://github.com/YasiNoshirvan/Smart-Parking-Space-Detection-by-Image-Processing)
- 🎥 [Movement Detection](https://github.com/YasiNoshirvan/Movement-Detection-by-Image-Processing)
- 🔍 [License Plate Detection and OCR](https://github.com/YasiNoshirvan/License-Plate-Detection-by-Image-Processing)

---

*Learning repository — practical exercises rather than a production-ready computer vision package.*
