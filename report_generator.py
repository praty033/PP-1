from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_report(content_type, content, prediction, score, filename=None):
    if filename is None:
        os.makedirs("reports", exist_ok=True)
        filename = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    c = canvas.Canvas(filename)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "ProofPixels Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, 770, f"Type: {content_type}")
    c.drawString(50, 750, f"Prediction: {prediction}")
    c.drawString(50, 730, f"Confidence: {score:.2%}")
    c.drawString(50, 700, "Content analyzed:")
    c.drawString(50, 680, str(content)[:100])
    c.save()
    return filename