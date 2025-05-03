from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image

# Load pre-trained Donut model
processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")

# Load an image of scanned exam
image = Image.open("scanned_exam.jpg").convert("RGB")

# Prepare input
pixel_values = processor(image, return_tensors="pt").pixel_values

# Generate prediction
outputs = model.generate(pixel_values)
predicted_text = processor.batch_decode(outputs, skip_special_tokens=True)[0]

print(predicted_text)
