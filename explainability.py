from fake_news import classifier

def explain_news(news, top_n=5, max_words=50):
    # Limit to the first 50 words so this doesn't take forever on long articles
    words = news.split()[:max_words]

    baseline = classifier(" ".join(words))[0]
    baseline_score = baseline["score"]
    baseline_label = baseline["label"]

    impacts = []
    for i in range(len(words)):
        reduced_text = " ".join(words[:i] + words[i+1:])
        if not reduced_text.strip():
            continue
        new_result = classifier(reduced_text)[0]

        if new_result["label"] != baseline_label:
            impact = 1.0  # removing this word flipped the whole prediction
        else:
            impact = abs(baseline_score - new_result["score"])

        impacts.append((words[i], impact))

    impacts.sort(key=lambda x: x[1], reverse=True)
    return impacts[:top_n]