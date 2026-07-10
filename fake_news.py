from transformers import pipeline

print("Loading fake news detection model... Please wait.")

classifier = pipeline(
    "text-classification",
    model="jy46604790/Fake-News-Bert-Detect"
)

print("Model loaded successfully!")

def analyze_news(news):
    result = classifier(news)
    label = result[0]["label"]
    score = result[0]["score"]

    # IMPORTANT: run this once and print(result) to see the exact label
    # names this model returns (e.g. "LABEL_0"/"LABEL_1" or "FAKE"/"REAL"),
    # then adjust the check below to match exactly what you see.
    if label in ("LABEL_1", "REAL", "TRUE"):
        prediction = "Likely Real News"
    else:
        prediction = "Potentially Fake News"

    return prediction, score


if __name__ == "__main__":
    sample = "Scientists confirm water boils at 100°C at sea level."
    result = classifier(sample)
    print("RAW RESULT (check label names here):", result)
    print(analyze_news(sample))