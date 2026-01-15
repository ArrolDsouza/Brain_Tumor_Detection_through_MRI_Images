# 🧠 AlphaDetect 

**AlphaDetect** is an end-to-end, deep learning–powered web application designed for **automatic brain tumor detection and classification** using **Magnetic Resonance Imaging (MRI)** scans. The application aims to assist in the early analysis of brain MRI images by leveraging the power of **convolutional neural networks (CNNs)** and **transfer learning**.

The core of AlphaDetect is built on a **VGG16 architecture**, a well-established deep learning model known for its strong feature extraction capabilities. By fine-tuning VGG16 on a labeled brain MRI dataset, the model learns to identify complex spatial patterns and visual cues associated with different types of brain tumors.

AlphaDetect can classify an MRI image into one of four categories:

* **Glioma** – aggressive tumors originating from glial cells
* **Meningioma** – tumors arising from the meninges
* **Pituitary Tumor** – tumors affecting the pituitary gland
* **No Tumor** – healthy brain MRI scans

The application is implemented using **Streamlit**, providing an intuitive and interactive user interface that allows users to upload MRI images and instantly receive predictions. Along with the predicted class, the app displays a **confidence score** and **class-wise probability distribution**, enabling users to better understand the model’s decision-making process.

> ⚠️ **Disclaimer:** AlphaDetect is intended for **educational, academic, and research purposes**, demonstrating the real-world application of deep learning in medical image analysis. It is **not a clinical diagnostic tool** and should not be used as a replacement for professional medical evaluation or diagnosis. It is **not a medical diagnostic tool** and should not be used as a substitute for professional medical advice.

---

## ✅ Features

* 1. Upload brain MRI images (`.jpg`, `.jpeg`, `.png`)
* 2. Detect presence of a brain tumor
* 3. Classify tumors into:
  * a. Glioma
  * b. Meningioma
  * c. Pituitary Tumor
  * d. No Tumor
* 4. Display confidence score and class-wise probabilities
* 5. Simple and user-friendly UI built with Streamlit

---

## 🧠 Model Details

* **1. Architecture:** VGG16 (Transfer Learning)
* **2. Framework:** TensorFlow / Keras
* **3. Input Size:** 128 × 128 RGB images
* **4. Output Classes:** 4 (Glioma, Meningioma, Pituitary, No Tumor)
* **5. Model File:** `model.h5`

The VGG16 model is fine-tuned on a labeled brain MRI dataset to extract deep spatial features and perform accurate classification.

---

## 🛠️ Tech Stack

* **1. Frontend:** Streamlit
* **2. Backend / ML:** TensorFlow, Keras, NumPy
* **3. Visualization:** Matplotlib
* **4. Language:** Python

---

## 📂 Project Structure

```
AlphaDetect/
|
├── Brain_Tumor_Dataset/                     # Dataset of Brain MRI Image
    │
    ├── Train
    ├── Test        
├── app.py                         # Streamlit application
├── model.h5                       # Trained VGG16 model
├── Training.py                       # Training VGG16 Model on Dataset
├── Brain_Tumor_Detector_Image.jpeg# App banner image
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## 📥 Installation & Setup

### 1️. Clone the Repository

```bash
git clone https://github.com/your-username/AlphaDetect.git
cd AlphaDetect
```

### 2️. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️. Run the Application

```bash
streamlit run app.py
```

The app will open in your default browser.

---

## ⚙️ How It Works

1. Upload a brain MRI image
2. Image is resized to **128×128** and normalized
3. VGG16-based model predicts tumor class
4. App displays:

   * Detection result
   * Confidence score
   * Class-wise probability distribution

---

## 📊 Output Example

<img width="1559" height="859" alt="Screenshot 2025-08-26 090344" src="https://github.com/user-attachments/assets/3bb8650c-3966-4036-abc4-4cc0d9ee1dad" />
<img width="1209" height="853" alt="Screenshot 2025-08-26 090417" src="https://github.com/user-attachments/assets/8117bfcd-4c33-44db-be6c-a809df1c876d" />
<img width="961" height="835" alt="Screenshot 2025-08-26 090551" src="https://github.com/user-attachments/assets/5672cf99-8302-4046-90f2-2cb325b8040b" />


## 📈 Model Performance & Results

### ✅ Overall Performance

* **Test Accuracy:** **96%**
* **Total Test Samples:** 1311

### 📊 Classification Report

<img width="402" height="207" alt="Screenshot 2025-09-04 191339" src="https://github.com/user-attachments/assets/a72053d7-ab7f-4672-99e4-02bb501d92c1" />


| Class      | Precision | Recall | F1-Score | Support |
| ---------- | --------- | ------ | -------- | ------- |
| Glioma     | 0.98      | 0.90   | 0.94     | 300     |
| Meningioma | 0.90      | 0.95   | 0.93     | 306     |
| No Tumor   | 1.00      | 1.00   | 1.00     | 405     |
| Pituitary  | 0.97      | 0.99   | 0.98     | 300     |

* **Macro Avg F1-score:** 0.96
* **Weighted Avg F1-score:** 0.96

### 🔲 Confusion Matrix
<img width="575" height="486" alt="Screenshot 2025-09-04 191315" src="https://github.com/user-attachments/assets/3a2e9423-49cb-4464-a963-16a2d5220539" />

```
[[269  30   0   1]
 [  5 291   1   9]
 [  0   0 405   0]
 [  0   2   0 298]]
```

Excellent class separation, especially for **No Tumor** cases (100% accuracy).

### 📉 Training History
<img width="846" height="422" alt="Screenshot 2026-01-15 141256" src="https://github.com/user-attachments/assets/648416c1-e625-4da7-b5eb-afa098c90272" />

* Accuracy steadily increases across epochs
* Loss consistently decreases, indicating good convergence
* No significant overfitting observed

### 📐 ROC–AUC Analysis
<img width="897" height="744" alt="Screenshot 2026-01-15 141243" src="https://github.com/user-attachments/assets/e650233d-e9d1-4d09-a449-f2eb8f25bd83" />

* ROC curves were generated for all four classes
* **AUC values ~0.95–1.00**, indicating excellent discriminative capability

These results validate the effectiveness of **VGG16 transfer learning** for brain tumor classification using MRI images.

---

## 🔮 Future Enhancements

* Grad-CAM visualization for explainability
* Support for DICOM (`.dcm`) images
* Multi-slice MRI analysis
* Deployment on cloud platforms (AWS / Hugging Face / Streamlit Cloud)
* Mobile-friendly UI

---

## 👨‍💻 Author

**Arrol Dsouza**
B.Tech – Artificial Intelligence & Data Science

* GitHub: [https://github.com/your-username](https://github.com/your-username)
* LinkedIn: [https://linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)

---


⭐ *If you like this project, don’t forget to star the repository!*







