# Importing the app to initialize
from emotion_detection import emotion_detector

text_to_analyze = "I hate working long hours."
result = emotion_detector(text_to_analyze)
print(result)