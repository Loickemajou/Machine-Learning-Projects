### 🫁 Pneumonia Classification using ResNet-50
A deep learning project that uses **Convolutional Neural Networks (CNNs)** to detect pneumonia from chest X-ray images. Built entirely in **PyTorch**, this notebook demonstrates how image data can be leveraged for medical diagnosis and healthcare insights. **Class Activation Maps (CAMs)** are used to visualize regions in the X-rays that influence the model's predictions.

---

### Overview
The notebook  walks through a complete image classification pipeline for medical imaging. It reads chest X-ray images, preprocesses and augments the data, and trains a **ResNet-50** model to classify images as **Pneumonia** or **Normal**.

---

### Project Workflow

**Data Loading**  
- Loads a dataset of chest X-ray images labeled as `Normal` or `Pneumonia`.

**Image Preprocessing & Augmentation**  
- Resizes images, normalizes pixel values, and applies augmentations (rotation, flips, etc.) to increase model robustness.

**Label Encoding**  
- Converts categorical labels into numeric form suitable for binary classification.

**Model Building**  
- Fine-tunes a **ResNet-50** architecture with pretrained weights from ImageNet.  
- Adds custom dense layers for binary classification.

**Training & Evaluation**  
- Trains the model on the prepared dataset.  
- Evaluates performance using metrics such as **accuracy, precision, recall, and F1-score**.  
- Generates predictions and visualizes results on sample X-rays.  
- Uses **Class Activation Maps (CAMs)** to highlight regions of the X-ray that influenced the model's decision.

---

### Objective
The goal of this project is to provide an automated tool for detecting pneumonia from chest X-rays. Such systems can support radiologists and healthcare providers by offering faster, data-driven diagnostic insights, while CAMs help explain model decisions.

---

### Key Features
- Preprocesses and augments chest X-ray images.  
- Utilizes a **ResNet-50 CNN** fully implemented in **PyTorch**.  
- Fine-tunes pretrained weights for medical imaging tasks.  
- Applies **Class Activation Maps (CAMs)** for interpretability.  
- Evaluates model with robust metrics for real-world reliability.  
- Serves as a foundation for AI-assisted radiology and diagnostic support.

---

### 💬 Summary
This project demonstrates how deep learning, CNNs, and CAMs can be used to analyze medical images for pneumonia detection. It’s a practical example of AI applied to healthcare, combining image processing, model training, explainability, and evaluation in a single PyTorch workflow.

**Example Result:**  
![Pneumonia Classification Result](PUT_YOUR_PNG_LINK_HERE)

Developed using **PyTorch** and **Python**.
