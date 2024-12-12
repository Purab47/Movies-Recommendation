# Movie Recommendation System

## Overview
This project is a **Content-Based Movie Recommendation System** that suggests movies to users based on their preferences. Using the metadata of movies, such as genres, cast, crew, and plot keywords, the system calculates similarities between movies and recommends the most relevant ones.

## Features
- Suggests movies similar to a selected movie.
- Content-based filtering using metadata such as genres, cast, and keywords.
- Easy-to-use interface for entering movie preferences.

## Technologies Used
- **Programming Language:** Python
- **Libraries and Frameworks:**
  - NumPy
  - Pandas
  - Scikit-learn
  - Flask (for deployment)
- **Deployment Platform:** [Heroku](https://www.heroku.com)

## How It Works
1. **Data Collection:** The system uses a dataset containing metadata of movies, including genres, cast, crew, and keywords.
2. **Preprocessing:**
   - Cleaning and standardizing text data.
   - Combining relevant features into a single string.
3. **Feature Extraction:**
   - Using TF-IDF or Count Vectorizer to create feature vectors from movie metadata.
   - Calculating the cosine similarity between movie vectors.
4. **Recommendation:**
   - Based on a user-selected movie, the system identifies and recommends movies with the highest similarity scores.

## Installation
### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Purab47/movie-recommendation-system.git
   cd movie-recommendation-system
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application locally:
   ```bash
   python app.py
   ```
4. Access the application in your browser at `http://localhost:5000`.

## Dataset
The dataset used in this project is sourced from [TMDB](https://www.themoviedb.org/). Ensure you have the `movies_metadata.csv` file in the `data/` folder.

## Deployment
The system is deployed on Heroku. To deploy it yourself:
1. Create a Heroku account and install the Heroku CLI.
2. Login to Heroku:
   ```bash
   heroku login
   ```
3. Create a Heroku app:
   ```bash
   heroku create
   ```
4. Deploy the app:
   ```bash
   git push heroku main
   ```
5. Open the app:
   ```bash
   heroku open
   ```

## Usage
1. Enter the name of a movie you like in the input field.
2. Get a list of movies similar to your selection.

## Screenshots
![Home Page](path-to-your-screenshot/home.png)
![Recommendation Example](path-to-your-screenshot/recommendation.png)

## Future Enhancements
- Integrate collaborative filtering for enhanced recommendations.
- Add user ratings and reviews for personalized recommendations.
- Implement a modern frontend framework for an improved UI.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
**Purab Ganvir**  
GitHub: [@Purab47](https://github.com/Purab47)  
LinkedIn: [Purab Ganvir](https://www.linkedin.com/in/purab-ganvir)

---
Thank you for exploring this project! Feel free to reach out for questions or feedback.
