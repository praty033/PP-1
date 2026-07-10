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

    # NOTE: run this file directly first and check the printed RAW RESULT
    # to see the exact label names this model returns, then adjust below
    # if needed.
    if label in ("LABEL_1", "REAL", "TRUE"):
        prediction = "Likely Real News"
    else:
        prediction = "Potentially Fake News"

    return prediction, score


if __name__ == "__main__":
    sample = "Scientists confirm water boils at 100 degrees Celsius at sea level."
    raw_result = classifier(sample)
    print("RAW RESULT (check label names here):", raw_result)

    prediction, score = analyze_news(sample)
    print("Prediction:", prediction)
    print("Confidence Score:", score)