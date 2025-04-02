# 🎬 Movie Recommender System

## 📌 Overview
The **Movie Recommender System** is a content-based recommendation system that suggests movies similar to a given movie. It uses natural language processing techniques to analyze movie metadata and compute similarity scores between movies.

## 🚀 Features
- Suggests movies based on similarity to a selected movie
- Uses **TF-IDF Vectorization** and **cosine similarity** for recommendations
- Interactive **Streamlit** web app for easy usage
- Lightweight and fast movie recommendations

## 🛠️ Technologies Used
- **Python**
- **Streamlit** (for the web app)
- **Pandas & NumPy** (for data processing)
- **Scikit-learn** (for vectorization and similarity calculation)
- **Pickle and Joblib** (for model storage)

## 📂 Project Structure
```
Movie-Recommender-System/
│-- datasets/
│   ├── movies.csv
│   ├── credits.csv
│-- model/
│   ├── movies_list.pkl
│   ├── similarity.pkl
│-- Movie_Recomender_system.ipynb
│-- app.py
│-- requirements.txt
│-- README.md
```

## 🔧 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/raj-prateek-gupta/Movie-Recommender-System.git
   cd Movie-Recommender-System
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## 📊 Dataset
The system uses the **TMDB 5000 Movies Dataset**, which includes movie titles, genres, overviews, and credits.

## 🖥️ Usage
1. Open the web app.
2. Select a movie from the dropdown menu.
3. Get a list of recommended movies.

## 📞 Contact
- **GitHub**: [raj-prateek-gupta](https://github.com/raj-prateek-gupta)
- **LinkedIn**: (https://www.linkedin.com/in/prateek-kumar-03127b229)

