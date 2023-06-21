<!-- ⚠️ This README has been generated from the file(s) "blueprint.md" ⚠️-->
[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)](#medayu---ayurvedic-plant-identification-android-app)

# ➤ MedAyu - Ayurvedic Plant Identification Android App

![logoicon10 (3)](https://github.com/shoaib749/MedAyu-Ayurvedic-Classification-API/assets/66304849/44809f9c-3f17-470d-817b-1e078a45e665)



MedAyu is an Android application that utilizes machine learning to predict Ayurvedic plants by scanning their leaves. This repository contains the Flask application that serves as the API endpoint for MedAyu.


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#getting-started)

## ➤ Getting Started

These instructions will help you set up the Flask application on your local system for development and testing purposes.

### Prerequisites

Before running the application, ensure that you have the following installed:

- Python 3.x
- TensorFlow
- Keras
- OpenCV
- Flask

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/medayu-flask.git

```
Change to the project directory:
```bash

cd medayu-flask

```
Install the dependencies:
```bash

pip install -r requirements.txt

```
Run the Flask application:
```bash

python app.py

```
The application should now be running locally on http://localhost:5000.
[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#getting-started)

## ➤ API Endpoints

The Flask application provides the following API endpoint:

**Endpoint:** `https://flask-production-0d46.up.railway.app/class`
- **Method:** POST
- **Request Body:**
  - `test_url`: URL of the test image to be sent for prediction
- **Response Body:**
   - `PlantName`: Name of the predicted plant as a string
 
[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#getting-started)
## ➤ Deployments
The Flask application can be deployed on various platforms.
[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#getting-started)

## ➤ License
This project is licensed under the `MIT License`.

