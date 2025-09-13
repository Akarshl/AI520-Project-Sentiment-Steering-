import matplotlib.pyplot as plt

# Example average sentiment scores (replace with real values from your app evaluation)
emotions = ["Happy", "Sad", "Hopeful", "Eerie"]
scores = [0.92, 0.89, 0.75, 0.78]

plt.bar(emotions, scores, color="skyblue")
plt.ylim(0, 1)
plt.title("Sentiment Alignment Scores by Emotion")
plt.xlabel("Target Emotion")
plt.ylabel("Average Confidence Score")
plt.savefig("results/sentiment_scores.png")
plt.show()
