import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Platform": [
        "Instagram",
        "YouTube",
        "Facebook",
        "Snapchat",
        "WhatsApp"
    ],
    "Hours_Per_Day": [3, 2.5, 1.5, 2, 1]
}

df = pd.DataFrame(data)
print("SOCIAL MEDIA USAGE ANALYSIS")
print(df.to_string(index=False))

total = df["Hours_Per_Day"].sum()
average = df["Hours_Per_Day"].mean()
most_used = df.loc[df["Hours_Per_Day"].idxmax()]

print("\nTotal usage:", total, "hours per day")
print("Average usage:", round(average, 2), "hours")
print("Most used platform:", most_used["Platform"])
print("Usage time:", most_used["Hours_Per_Day"], "hours")

colors = [
    "#E1306C", "#FF0000", "#1877F2",
    "#FFCC00", "#25D366"
]

plt.figure(figsize=(9, 5))
plt.bar(df["Platform"], df["Hours_Per_Day"], color=colors)

plt.title("Daily Social Media Usage")
plt.xlabel("Platform")
plt.ylabel("Hours per day")
plt.tight_layout()
plt.show()
