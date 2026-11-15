from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def evaluate_answer(user_answer, expected_keywords, reference_answer):

    if not user_answer.strip():
        return {
            "score": 0,
            "similarity_score": 0,
            "keyword_score": 0,
            "matched_keywords": [],
            "missing_keywords": expected_keywords,
            "feedback": "Please write an answer first."
        }

    # Convert answers into TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words="english")

    try:
        vectors = vectorizer.fit_transform([
            user_answer,
            reference_answer
        ])

        similarity = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )[0][0]

        similarity_score = round(similarity * 100)

    except ValueError:
        similarity_score = 0

    # Check keyword coverage
    answer = user_answer.lower()

    matched_keywords = []
    missing_keywords = []

    for keyword in expected_keywords:

        if keyword.lower() in answer:
            matched_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)

    if expected_keywords:
        keyword_score = round(
            len(matched_keywords) / len(expected_keywords) * 100
        )
    else:
        keyword_score = 0

    # Combined score
    final_score = round(
        (similarity_score * 0.7) +
        (keyword_score * 0.3)
    )

    # Generate feedback
    if final_score >= 80:
        feedback = "Excellent! Your answer is closely aligned with the reference answer."
    elif final_score >= 60:
        feedback = "Good attempt! Improve your explanation with more relevant concepts."
    elif final_score >= 40:
        feedback = "Fair attempt. Try explaining the main concepts more clearly."
    else:
        feedback = "Keep practising. Review the reference answer and try again."

    return {
        "score": final_score,
        "similarity_score": similarity_score,
        "keyword_score": keyword_score,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "feedback": feedback
    }