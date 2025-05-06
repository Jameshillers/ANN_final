library(tidyverse)

results = read_csv("results.csv")

# Summarize mean F1-score per emotion across all models
mean_emotion_perf <- results %>%
  group_by(emotion) %>%
  summarize(mean_f1 = mean(f1-score, na.rm = TRUE)) %>%
  arrange(desc(mean_f1))

# Plot
ggplot(mean_emotion_perf, aes(x = reorder(emotion, mean_f1), y = mean_f1)) +
  geom_col(fill = "steelblue") +
  coord_flip() +
  labs(title = "Mean F1 Score per Emotion Across Models",
       x = "Emotion",
       y = "Mean F1 Score") +
  theme_minimal()
