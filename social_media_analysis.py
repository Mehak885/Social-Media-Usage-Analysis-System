
import pandas as pd
import matplotlib.pyplot as plt

# Social Media Usage Dataset
data = {
    "Platform": [
        "Instagram", "YouTube", "Facebook",
        "Snapchat", "WhatsApp"
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

# Bar chart
df.plot(
    x="Platform",
    y="Hours_Per_Day",
    kind="bar",
    legend=False,
    title="Daily Social Media Usage"
)

plt.ylabel("Hours per day")
plt.tight_layout()
plt.show()
