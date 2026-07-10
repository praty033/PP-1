from transformers import pipeline

print("Loading AI image detection model... Please wait.")

image_classifier = pipeline(
    "image-classification",
    model="capcheck/ai-image-detection"
)

print("Image model loaded successfully!")

def analyze_image(image_path):
    result = image_classifier(image_path)
    top = result[0]  # highest-confidence guess
    label = top["label"]
    score = top["score"]

    if label.lower() == "fake":
        prediction = "Likely AI-Generated"
    else:
        prediction = "Likely Real Photo"

    return prediction, score