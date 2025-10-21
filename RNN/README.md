
#  Medical Text Classification using LSTM

A deep learning project that uses **Natural Language Processing (NLP)** to predict **diseases** and **prescriptions** from patient-reported medical problems.
Built using **TensorFlow/Keras**, this notebook demonstrates how text data can be transformed into actionable healthcare insights.

---

##  Table of Contents

* [Overview](#overview)
* [Project Workflow](#project-workflow)
* [Objective](#objective)
* [Key Features](#key-features)
* [Summary](#summary)

---

##  Overview

The notebook `13bd7ca3-050c-407e-813a-4e0faa1a6d90.ipynb` walks through a complete NLP pipeline for medical data.
It reads text describing patient problems, preprocesses and encodes the data, and trains an **LSTM (Long Short-Term Memory)** model to predict relevant medical outcomes.

---

##  Project Workflow

1. **Data Loading**

   * Reads a dataset (`medical_data.csv`) containing `Patient_Problem`, `Disease`, and `Prescription` columns.

2. **Text Preprocessing**

   * Tokenizes the patient text and applies sequence padding to ensure consistent input length.

3. **Label Encoding**

   * Converts the categorical disease and prescription labels into numeric form using `LabelEncoder` and one-hot encoding.

4. **Model Building**

   * Constructs an LSTM model with embedding and dense layers for classification tasks.

5. **Training & Evaluation**

   * Trains the model on the prepared dataset and evaluates its performance on predicting medical outcomes.

---

##  Objective

The goal of this project is to **automate the interpretation of medical text** — helping identify diseases and possible prescriptions based on patient problem descriptions.

Such systems can support doctors, healthcare assistants, and triage systems in making faster, data-driven decisions.

---

##  Key Features

* Preprocesses and vectorizes raw medical text.
* Uses an **LSTM deep learning architecture** for classification.
* Encodes multiple target variables (disease and prescription).
* Provides a foundation for applying **AI in healthcare** and clinical decision support.

---

## 💬 Summary

This project demonstrates how **deep learning and NLP** can be used together to understand and predict medical information from unstructured text.
It’s a great starting point for exploring the intersection of **AI, language, and healthcare innovation**.

---

**Developed with using TensorFlow and Python**
