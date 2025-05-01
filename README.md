# Emotion Recognition

This project explores **emotion recognition** from natural language text using machine learning techniques. It includes a full pipeline: from data collection via APIs (e.g., Reddit or Twitter), to preprocessing, model training, evaluation, and visualization.

## Project Goals
- Collect text data from real-world sources (via API)
- Label or infer emotions (manually or weakly)
- Preprocess and vectorize text
- Train classification models (SVM, Random Forest, etc.)
- Evaluate performance and visualize results
- Package code in a modular, reproducible format

## 📁 Project Structure
```
emotion_recognition/
├── data/                  # Raw and processed datasets
│   ├── raw/              # Unprocessed pulled data (e.g., from API)
│   └── processed/        # Cleaned and labeled datasets
├── models/               # Saved model files (e.g., .pkl)
├── notebooks/            # Jupyter notebooks for exploration and analysis
├── src/                  # Source code for pipeline
│   ├── __init__.py
│   ├── get_data.py       # Scripts to pull data from APIs (e.g., Twitter, Reddit)
│   ├── preprocess.py     # Text cleaning, tokenization, vectorization
│   ├── train_model.py    # Model training and evaluation
│   └── utils.py          # Helper functions
├── main.py               # Optional: entry point to run the full pipeline
├── requirements.txt      # List of required packages
└── README.md             # Project overview and instructions
```

## Requirements
To install dependencies:
```bash
pip install -r requirements.txt
```

## TODO (Work in Progress)
- [ ] Implement data collection using Reddit or Twitter API
- [ ] Preprocess and clean text data
- [ ] Train baseline classifiers (SVM, RF)
- [ ] Evaluate with confusion matrix, precision/recall/F1
- [ ] Visualize results (e.g., word clouds, t-SNE)
- [ ] Package code for reproducibility

## 📌 Status
Currently in early development.

---

Feel free to fork, suggest improvements, or open an issue!
