import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read dataset
df = pd.read_csv("raw_skills.csv")

print("========== TECH STACK RECOMMENDER ==========\n")

# User input
skill1 = input("Enter Skill 1: ")
skill2 = input("Enter Skill 2: ")
skill3 = input("Enter Skill 3: ")

# Validation
if skill1.strip() == "" or skill2.strip() == "" or skill3.strip() == "":
    print("\nPlease enter all three skills.")
    exit()

user_input = skill1 + " " + skill2 + " " + skill3

# Combine dataset with user input
documents = df["Skills"].tolist()
documents.append(user_input)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# User vector
user_vector = tfidf_matrix[-1]

# Job vectors
job_vectors = tfidf_matrix[:-1]

# Cosine Similarity
similarity_scores = cosine_similarity(user_vector, job_vectors)

# Add scores to dataframe
df["Similarity Score"] = similarity_scores.flatten()

# Sort by similarity
df = df.sort_values(by="Similarity Score", ascending=False)

# Display top 3
print("\nTop 3 Recommended Career Paths:\n")

top3 = df.head(3)

for index, row in top3.iterrows():
    print(f"Job Role : {row['Job Role']}")
    print(f"Match    : {row['Similarity Score']*100:.2f}%")
    print("-" * 35)
    