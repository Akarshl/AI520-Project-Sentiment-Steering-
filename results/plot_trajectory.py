import matplotlib.pyplot as plt

# Example story trajectory (replace with real BERT outputs per paragraph)
paragraphs = [1, 2, 3, 4, 5]
scores = [0.8, 0.85, 0.9, 0.88, 0.9]  # e.g., Positive sentiment confidence

plt.plot(paragraphs, scores, marker="o", linestyle="-", color="green")
plt.ylim(0, 1)
plt.xticks(paragraphs)
plt.title("Emotional Trajectory Across Story Paragraphs")
plt.xlabel("Paragraph")
plt.ylabel("Sentiment Confidence")
plt.savefig("results/emotional_trajectory.png")
plt.show()
