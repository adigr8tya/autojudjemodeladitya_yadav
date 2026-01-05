# AutoJudge: Predicting Programming Problem Difficulty

## Project Overview
AutoJudge is an intelligent system that predicts the difficulty of programming problems using only their textual descriptions.
The system performs two tasks:

- Classification: Predicts the difficulty class (Easy / Medium / Hard)
- Regression: Predicts a numerical difficulty score

The prediction is based purely on:
- Problem description
- Input description
- Output description

No contest metadata (such as Codeforces divisions) is used.

---

## Dataset Used
We use the TaskComplexityEval-24 dataset, a publicly available dataset of programming problems annotated with:

- Problem descriptions
- Difficulty class labels (Easy / Medium / Hard)
- Numerical complexity scores

Dataset Source:
https://github.com/AREEG94FAHAD/TaskComplexityEval-24

The dataset is stored locally in the Data/ directory as a JSONL file.

---

## Approach and Models Used

### Data Preprocessing
- Converted all text to lowercase
- Removed special characters and extra whitespace
- Handled missing values
- Combined title, description, input, and output fields into a single text field

### Feature Extraction
- TF-IDF vectorization
- Unigrams and bigrams
- English stopword removal

### Classification Models
- Logistic Regression (baseline)
- Linear Support Vector Machine (final classifier)

### Regression Model
- Random Forest Regressor

---

## Evaluation Metrics

### Classification
Accuracy ≈ 0.45

Predicting difficulty from text alone is challenging due to the subjective nature of difficulty labels and the absence of implementation-level information. The model performs better than a random baseline and demonstrates a complete and correct ML pipeline.

### Regression
Mean Absolute Error (MAE): ~1.69  
Root Mean Squared Error (RMSE): ~2.04  

---

## How to Run the Project Locally

1. Clone the repository

2. Pull large model files (Git LFS)

3. Install dependencies

4. Run the web application

The application will open automatically in your browser.

---

## Web Interface Explanation
The web interface is built using Streamlit and allows users to:

1. Paste the problem description
2. Paste the input description
3. Paste the output description
4. Click Predict Difficulty

The application then displays:
- Predicted difficulty class
- Predicted numerical difficulty score

The app runs completely locally; no hosting is required.

---

## Demo Video
Demo Video Link:
https://drive.google.com/file/d/14eovPqWd9CKkVvWfunXLQRMN4T4kWXbF/view?usp=sharing

The demo video shows:
- Brief project explanation
- Model approach
- Live prediction using the Streamlit web interface

---

## Notes and Limitations
- The model predicts difficulty based solely on textual complexity.
- Contest-based difficulty labels (e.g., Codeforces Divisions) are not used.
- Predictions may differ from contest difficulty levels due to the absence of contextual metadata.

---

## Author
Aditya Yadav  
Department of Computer Science  
Indian Institute of Technology Roorkee (IIT Roorkee)
