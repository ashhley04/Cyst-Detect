# 🩺 Cyst-Detect: PCOS Detection Using Ultrasound Images

### 💗 Cyst-Detect — Empowering PCOS Awareness Through AI

Cyst-Detect is a machine learning project developed as part of **Cyst-Detect**, a web-based platform designed to promote awareness of Polycystic Ovary Syndrome (PCOS) using Deep Learning and Computer Vision.

The project uses a **Convolutional Neural Network (CNN)** to classify ovarian ultrasound images into PCOS-positive and PCOS-negative categories. The website also provides educational information about PCOS, its symptoms, awareness videos, and medical guidance resources.

> ⚠️ **Disclaimer:** This project is an educational prototype and has not been clinically validated. It must not be used as a substitute for professional medical diagnosis or treatment.

---

## 📌 Table of Contents

- [🎯 Problem Statement](#-problem-statement)
- [💡 Project Overview](#-project-overview)
- [✨ Key Features](#-key-features)
- [🏗️ System Architecture](#️-system-architecture)
- [🧠 Modeling Approach](#-modeling-approach)
- [📊 Models and Performance](#-models-and-performance)
- [📈 Evaluation Metrics](#-evaluation-metrics)
- [🛠️ Technology Stack](#️-technology-stack)
- [💻 System Requirements](#-system-requirements)
- [📂 Dataset](#-dataset)
- [🚀 Getting Started](#-getting-started)
- [📁 Project Structure](#-project-structure)
- [⚠️ Limitations](#️-limitations)
- [🩺 Medical Disclaimer](#-medical-disclaimer)
- [🔮 Future Enhancements](#-future-enhancements)
- [🔗 References](#-references)

---
## 🎥 Project Demo

Watch Cyst-Detct in action and explore how AI can help make video content accessible across different Indian regional languages.

**▶️ [Click here to watch the Cyst-Detect Demo][(https://youtu.be/vms3xeauNjc)**

## 🎯 Problem Statement

Polycystic Ovary Syndrome (PCOS) is a hormonal disorder that can affect women's reproductive and metabolic health. Limited awareness and barriers to timely healthcare evaluation can make it difficult for some individuals to understand their symptoms and seek appropriate medical guidance.

Cyst-Detect explores how deep learning can be used to classify ovarian ultrasound images and support PCOS awareness through an accessible web-based platform.

The project aims to demonstrate the potential of **Artificial Intelligence and Machine Learning in healthcare-related image classification**, while encouraging users to seek professional medical evaluation.

## 💡 Project Overview

Cyst-Detect combines a CNN-based image classification model with a Flask web application to provide a simple interface for uploading ultrasound images and viewing model-generated predictions.

The project workflow includes:

- 📥 Collecting and organizing ultrasound image data.
- 🖼️ Preprocessing images and applying data augmentation.
- 🧠 Developing and training a CNN model.
- 📊 Evaluating the trained model.
- 🌐 Integrating the saved model into a Flask application.
- 💗 Providing PCOS awareness information and educational resources.

The model achieved a **reported accuracy of 97%** during the project's development. This is the result reported by our project and should not be interpreted as proof of clinical diagnostic accuracy.

## ✨ Key Features

- 🖼️ **Ultrasound Image Classification:** Upload an ultrasound image to obtain a model-generated prediction.
- 🧠 **CNN-Based Deep Learning:** Learns visual features from labeled ultrasound images.
- ⚙️ **Image Preprocessing:** Converts images to grayscale and prepares them for model input.
- 🔄 **Data Augmentation:** Introduces image variations during training.
- 📊 **98% Reported Accuracy:** Highlights the accuracy achieved in our project.
- 🌐 **Flask Web Application:** Integrates the trained model with a user-friendly website.
- 📚 **PCOS Awareness:** Provides information about PCOS and associated symptoms.
- 🎥 **Educational Resources:** Includes awareness videos and helpful information.
- 👩‍⚕️ **Medical Guidance:** Encourages consultation with qualified healthcare professionals.

## 🏗️ System Architecture

The system follows a machine learning pipeline from image collection to prediction.

```text
          📂 Ultrasound Image Dataset
                      |
                      ▼
             ⚙️ Image Preprocessing
             (Grayscale, Resize)
                      |
                      ▼
              🔄 Data Augmentation
                (Training Data)
                      |
                      ▼
                 🧠 CNN Model
              (Training & Testing)
                      |
                      ▼
             💾 Saved Trained Model
                      |
                      ▼
             🌐 Flask Web Application
                      |
                      ▼
              🖼️ Image Upload
                      |
                      ▼
             🔍 Model Prediction
                      |
                      ▼
            📊 Classification Result
                      |
                      ▼
             💗 PCOS Awareness
```

### Architecture Components

1. **📂 Data Layer:** Stores labeled ultrasound images for training and testing.
2. **⚙️ Preprocessing Layer:** Converts images to grayscale and prepares them for the CNN.
3. **🧠 Model Layer:** Extracts image features and performs binary classification.
4. **🌐 Application Layer:** Connects the saved model to the web interface using Flask.
5. **📊 Presentation Layer:** Displays the prediction and relevant educational resources.

## 🧠 Modeling Approach

The project uses **supervised learning for binary image classification**.

### 1. 📥 Data Collection

Ultrasound images were collected as part of the original project and organized into training and testing datasets. The dataset was also shared on Kaggle.

### 2. ⚙️ Image Preprocessing

- Convert ultrasound images to grayscale.
- Resize images to the dimensions expected by the model.
- Normalize pixel values where required.
- Apply augmentation to training images.
- Maintain separate training and testing sets.

### 3. 🧠 CNN Model Development

A Convolutional Neural Network learns visual patterns from the input images through convolutional operations and uses the extracted features to classify the images.

### 4. 🚀 Model Integration

The trained model is saved and integrated into the Flask application. When a user uploads an image, the application preprocesses it, performs inference, and displays the predicted category.

## 📊 Models and Performance

| Parameter | Details |
|---|---|
| 🤖 Primary Model | Convolutional Neural Network (CNN) |
| 📚 Learning Type | Supervised Learning |
| 🎯 Task | Binary Image Classification |
| 🖼️ Input | Preprocessed ovarian ultrasound image |
| 📤 Output | PCOS-positive or PCOS-negative class |
| ⚙️ Training Technique | Image Preprocessing and Augmentation |
| 🏆 **Achieved Accuracy** | **98% (reported project result)** |
| 🌐 Deployment | Flask Web Application |

### 🏆 Model Performance

Our CNN model achieved a **reported accuracy of 97%** during project development.

Accuracy measures the proportion of correctly classified images among all evaluated images. The result should be interpreted in the context of the dataset and evaluation procedure used.

Further evaluation using precision, recall, specificity, F1-score, and a confusion matrix would provide a more comprehensive understanding of model performance.

*Note: The reported accuracy is an experimental project result, not clinically validated diagnostic accuracy.*

## 📈 Evaluation Metrics

The following metrics are useful for evaluating a binary image-classification model:

| Metric | Description |
|---|---|
| 🎯 Accuracy | Overall proportion of correct predictions |
| ✅ Precision | Proportion of positive predictions that are correct |
| 🔍 Recall / Sensitivity | Proportion of actual positive cases correctly identified |
| 🛡️ Specificity | Proportion of actual negative cases correctly identified |
| ⚖️ F1-Score | Harmonic mean of precision and recall |
| 📊 Confusion Matrix | Displays true positives, true negatives, false positives, and false negatives |

Accuracy alone is not sufficient for healthcare-related applications. Independent testing, patient-level data separation, and careful assessment of false positives and false negatives are also important.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🧠 TensorFlow / Keras | CNN model development and training |
| 🖼️ OpenCV | Image processing, where used |
| 🌐 Flask | Backend web framework |
| 🎨 HTML, CSS, JavaScript | Frontend development |
| 🅱️ Bootstrap | Responsive UI design |
| 🗄️ MySQL | Database integration, if enabled |
| 📦 XAMPP | Local database environment, if required |
| ☁️ Google Colab / Jupyter | Model development and training |
| 📂 Kaggle | Dataset hosting |

## 💻 System Requirements

### Hardware Requirements

- 💻 Modern dual-core processor or better.
- 🧠 8 GB RAM recommended.
- 💾 Sufficient disk space for the dataset, libraries, and trained model.
- 🎮 GPU optional for model training.
- 🌐 Internet connection for downloading dependencies and datasets.

### Software Requirements

- Windows, Linux, or macOS.
- Python version compatible with the project's dependencies.
- TensorFlow / Keras.
- Flask.
- OpenCV and other libraries required by the source code.
- MySQL and XAMPP, if database functionality is used.
- Google Colab or Jupyter Notebook.
- A modern web browser.

## 📂 Dataset

The dataset is organized into two main directories: `train` and `test`. Each contains two class folders.

```text
data/
├── train/
│   ├── infected/
│   └── notinfected/
└── test/
    ├── infected/
    └── notinfected/
```

The folder names reflect the original dataset structure. For clarity, these categories refer to the project's PCOS-positive and PCOS-negative image labels; PCOS is not an infectious disease.

🔗 **Dataset Link:** [FightOS CNN Models — Kaggle](https://www.kaggle.com/code/aykorde/fightos-cnn-models/data)

The original project description states that the team collected primary data and applied image augmentation during model development.

For reliable evaluation, augmentation should be restricted to training data, and images from the same individual should not appear in both training and testing sets.

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_DIRECTORY>
```

Replace the placeholders with your repository URL and directory name.

### Step 2: Download the Dataset

Download the dataset from the [Kaggle project page](https://www.kaggle.com/code/aykorde/fightos-cnn-models/data) and place it in the directory expected by the notebook.

### Step 3: Train the Model

1. Open `FightOS_CNN_Models.ipynb` in Google Colab or Jupyter Notebook.
2. Configure the dataset path.
3. Install the required dependencies.
4. Run the preprocessing and training cells.
5. Evaluate the model.
6. Save the trained model.

If a trained model is already included, you may be able to run the web application without retraining.

### Step 4: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the dependencies specified by the project source code.

### Step 6: Configure the Database (If Required)

If the original MySQL integration is used:

1. Start the necessary services in XAMPP.
2. Create a MySQL database named `fightos`.
3. Import `fightos.sql`.
4. Configure the database connection in the Flask application.

Skip these steps if the version you are using does not require a database.

### Step 7: Run the Application

```bash
python flaskapp.py
```

Open the local URL shown in your terminal. With the default Flask configuration, it is commonly:

```text
http://127.0.0.1:5000/
```

The actual port depends on your application configuration.

🎥 **Implementation Video:** [Watch the FightOS Project Walkthrough](https://youtu.be/vms3xeauNjc)

## 📁 Project Structure

The following is an illustrative directory structure. Update it to reflect your actual repository.

```text
Cyst-Detect/
├── data/
│   ├── train/
│   └── test/
├── templates/
│   └── *.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── FightOS_CNN_Models.ipynb
├── flaskapp.py
├── fightos.sql
├── requirements.txt
└── README.md
```

The trained model file should also be included or downloaded separately if required by the application.

🔒 Avoid committing credentials, private data, or sensitive patient images to a public repository.

## ⚠️ Limitations

- Model performance depends on the size, quality, diversity, and labeling of the dataset.
- The reported accuracy may not generalize to other datasets or clinical environments.
- Data leakage, duplicate images, and class imbalance may inflate evaluation results.
- Ultrasound image classification alone cannot establish a PCOS diagnosis.
- The prototype has not been established as clinically safe or effective.
- Educational resources do not replace individualized medical advice.

## 🩺 Medical Disclaimer

**Cyst-Detect is an educational and research prototype, not a clinically validated diagnostic tool.**

The model's predictions may be incorrect. A PCOS-positive prediction does not confirm PCOS, and a PCOS-negative prediction does not rule it out.

This project must not be used to diagnose a condition, determine treatment, or make medical decisions. PCOS assessment requires appropriate evaluation by a qualified healthcare professional.

The project does not guarantee diagnostic accuracy, clinical suitability, or performance on real-world medical data. Users with health concerns should seek professional medical advice regardless of the model's output.

## 🔮 Future Enhancements

- 🧠 Explore additional CNN architectures and transfer-learning approaches.
- 📊 Add detailed evaluation reports and confusion-matrix visualizations.
- 🧪 Validate the model on independent datasets with patient-level separation.
- 🔍 Introduce appropriate model interpretability techniques.
- 🔒 Strengthen application security and privacy protections.
- 🎨 Improve interface accessibility and responsiveness.
- 👩‍⚕️ Explore clinical validation with qualified medical professionals and appropriate ethical oversight.

## 🔗 References

- 📂 **Dataset and Notebook:** [FightOS CNN Models — Kaggle](https://www.kaggle.com/code/aykorde/fightos-cnn-models/data)
- 🎥 **Implementation Video:** [FightOS Project Walkthrough](https://youtu.be/vms3xeauNjc)
- 🎨 **Frontend Template:** [Medilab — BootstrapMade](https://bootstrapmade.com/medilab-free-medical-bootstrap-theme/)

---

💗 *Developed as an academic machine learning and web development project to explore PCOS awareness and ultrasound image classification.*

