import pandas as pd

df_real_politifact = pd.read_csv("politifact_real.csv")
df_fake_politifact = pd.read_csv("politifact_fake.csv")

df_real_gossipcop = pd.read_csv("gossipcop_real.csv")
df_fake_gossipcop = pd.read_csv("gossipcop_fake.csv")

df_real_politifact['source'] = 'politifact'
df_fake_politifact['source'] = 'politifact'
df_real_gossipcop['source'] = 'gossipcop'
df_fake_gossipcop['source'] = 'gossipcop'

df_real = pd.concat([df_real_politifact, df_real_gossipcop], ignore_index=True)
df_fake = pd.concat([df_fake_politifact, df_fake_gossipcop], ignore_index=True)

df_real['label'] = 1
df_fake['label'] = 0

df = pd.concat([df_real, df_fake], ignore_index=True)

def what_is_missing(df):
    if df.isnull().values.any():
        print("There are some missing values. Let's look at each column:")
        print(df.isnull().sum())
    else:
        print("No missing values!")

num_politifact = (df['source'] == 'politifact').sum()
num_gossipcop = (df['source'] == 'gossipcop').sum()

what_is_missing(df)

df = df.drop(columns=['tweet_ids'])

from newspaper import Article
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except:
        return None

def fetch_articles_parallel(df, max_workers=10):
    urls = df['news_url'].tolist()
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(get_article_text, url): url for url in urls}
        for future in as_completed(future_to_url):
            try:
                results.append(future.result())
            except:
                results.append(None)

    df = df.copy()
    df['article_text'] = results
    return df

def balance_fake_real_articles(df):
    df_fake = df[df['label'] == 0]
    df_real = df[df['label'] == 1]

    min_count = min(len(df_fake), len(df_real))

    df_fake_sampled = df_fake.sample(n=min_count, random_state=42)
    df_real_sampled = df_real.sample(n=min_count, random_state=42)

    df_balanced = pd.concat([df_fake_sampled, df_real_sampled], ignore_index=True)
    print(f"Balanced dataset created with {min_count} fake and {min_count} real articles.")
    return df_balanced

df_with_articles = fetch_articles_parallel(df, max_workers=10)
df_with_articles.to_excel("all_articles_scraped.xlsx", index=False)
df_with_articles = pd.read_excel("all_articles_scraped.xlsx")
