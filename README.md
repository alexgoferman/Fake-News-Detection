# News Article Truth Classification using Multiple Models and Feature Engineering

This project tackles the problem of fake news detection by combining unsupervised and supervised learning techniques. We use Latent Dirichlet Allocation (LDA) to extract topic distributions from scraped article text, and then train multiple classifiers—including Logistic Regression, Random Forest, XGBoost, and Support Vector Machines—to predict whether an article is real or fake based on its topic signature.

Our goal is to build a pipeline that is both interpretable and accurate, showcasing the power of topic modeling in feature engineering for text classification.

---

## Project Structure

Here are the key files and folders included in this repository:

- `article_preprocessing.py`: Script that loads the original FakeNewsNet datasets, scrapes article text from URLs, balances the dataset, and outputs the final dataset with article content.
- `fake_news.ipynb`: Main notebook used for topic modeling, feature analysis, classifier training, evaluation, and visualization.
- `README.md`: This file.

### Zipped Datasets

To avoid GitHub's file size limitations, large datasets have been compressed into ZIP archives. You must extract them locally before running the scripts.

- `Original Datasets.zip`  
  Contains the four CSVs from FakeNewsNet:  
  - `politifact_real.csv`  
  - `politifact_fake.csv`  
  - `gossipcop_real.csv`  
  - `gossipcop_fake.csv`  

- `Dataset with Scraped Articles.zip`  
  Contains the Excel file `all_articles_scraped.xlsx`, which includes the full scraped article text used in our models. This dataset is used directly in modeling and analysis.

Total uncompressed sizes:
- Original datasets: ~43 MB
- Scraped articles: ~21 MB

---

## Getting Started

To run the project:

1. Clone the repository.
2. Download and extract both ZIP archives.
3. Run `article_preprocessing.py` to prepare the data (optional if using pre-scraped version).
4. Open `fake_news.ipynb` to explore topic modeling and classifier training.

---

## Notes

- Scraping is parallelized using `concurrent.futures` for efficiency, but is still slow and can fail if URLs are broken.
- All models use LDA-based topic vectors as input features for simplicity and interpretability.
- If you experience issues with large files, ensure your system has adequate RAM and disk space.
