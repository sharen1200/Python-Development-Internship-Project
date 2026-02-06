# Python Development Internship Project

This project was developed as part of an **Python Development**.  
It covers data analysis, machine learning, web development, voice processing, and generative AI concepts using Python.

## Project Structure
project/
├── data_analysis/
│ ├── analysis.py
│ ├── linear_regression.py
│ ├── matrix.py
│ └── house_rent_data.csv
│
├── sentiment_app/
│ ├── app.py
│ ├── static/
│ │ └── style.css
│ └── templates/
│ └── index.html
│
├── voice_assistant/
│ └── assistant.py
│
├── speech_to_image/
│ └── speech_image.py
│
├── gemini_chat/
│ └── gemini.py
│
├── requirements.txt


---

## Slab 1 – Completed Tasks

### 1. Data Analysis & Visualization
- Loaded CSV data using Pandas  
- Performed basic data analysis  
- Created bar charts, scatter plots, and heatmaps using Matplotlib and Seaborn  

**File:** `data_analysis/analysis.py`

---

### 2. Linear Regression Model
- Built a linear regression model using Scikit-learn  
- Predicted house rent based on features such as size and number of bedrooms  

**File:** `data_analysis/linear_regression.py`

---

### 3. Matrix Operations Tool
- Implemented using NumPy  
- Supports addition, subtraction, multiplication, transpose, and determinant  

**File:** `data_analysis/matrix.py`

---

## Slab 2 – Completed Tasks

### 4. Sentiment Analysis Web Application
- Developed using Flask  
- Used TextBlob for sentiment analysis  
- Classifies text as Positive, Negative, or Neutral  
- Displays polarity and subjectivity  
- Styled using CSS  

**Folder:** `sentiment_app/`

---

### 5. Voice-Activated Personal Assistant
- Implemented using SpeechRecognition and pyttsx3  
- Supports basic commands such as time and greetings  
- Includes text fallback when microphone is unavailable  

**Folder:** `voice_assistant/`

---

### 6. Speech-to-Image Generation
- Implemented the pipeline:  
  Speech → Text → Image Prompt  
- Speech is converted to text using SpeechRecognition  
- Image generation logic implemented using external APIs  
- Due to free-tier API restrictions, image generation is simulated  
- Complete pipeline and error handling are preserved  

**Folder:** `speech_to_image/`

---

### 7. Google Gemini Integration with Memory
- Implemented Gemini integration logic with conversation memory  
- Conversation history is stored to provide contextual responses  
- Due to SDK deprecation and model availability restrictions, responses are simulated during execution  

**Folder:** `gemini_chat/`

---

## Technologies Used
- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- Flask  
- TextBlob  
- SpeechRecognition  
- pyttsx3  

---

## How to Run


```bash
1. Create Virtual Environment
python -m venv .venv
2. Activate Virtual Environment
.venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Modules
python data_analysis/analysis.py
python sentiment_app/app.py
python speech_to_image/speech_image.py
python gemini_chat/gemini.py

Notes:-

Some AI services impose free-tier limits and model restrictions

To ensure stable execution during evaluation, simulated outputs are used where required

All logic and integration pipelines are correctly implemented

Author

Name: Bandam SharenTeja
Domain: AI & Data Science Internship

