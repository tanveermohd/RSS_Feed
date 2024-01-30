def classify_and_update_database(article):
    # Perform category classification using NLTK or spaCy
    # Example NLTK-based classification
    categories = classify_with_nltk(article['content'])
    article['category'] = categories

    # Update the database with the assigned category
    update_database(article)

    return article