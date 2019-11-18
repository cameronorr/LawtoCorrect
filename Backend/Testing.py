from textblob import TextBlob

text = TextBlob("I thinke I jus found a way to ruu this wihhout TensorFlow")
print(text.correct())