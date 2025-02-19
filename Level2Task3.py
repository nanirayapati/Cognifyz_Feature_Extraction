import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "C:/Users/SaiGanesh/Downloads/Dataset .csv"
df = pd.read_csv(file_path)

df['Restaurant Name Length'] = df['Restaurant Name'].apply(len)
df['Address Length'] = df['Address'].apply(len)
df['Has Table Booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})
df['Has Online Delivery'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})

plt.figure(figsize=(10, 5))
sns.histplot(df['Restaurant Name Length'], bins=30, kde=True, color="blue")
plt.title("Distribution of Restaurant Name Lengths")
plt.xlabel("Length of Restaurant Name")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(df['Address Length'], bins=30, kde=True, color="green")
plt.title("Distribution of Address Lengths")
plt.xlabel("Length of Address")
plt.ylabel("Count")
plt.show()

table_booking_counts = df['Has Table Booking'].value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=table_booking_counts.index, y=table_booking_counts.values)
plt.xticks([0, 1], ["No Table Booking", "Has Table Booking"])
plt.title("Availability of Table Booking")
plt.ylabel("Count")
plt.show()

online_delivery_counts = df['Has Online Delivery'].value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=online_delivery_counts.index, y=online_delivery_counts.values)
plt.xticks([0, 1], ["No Online Delivery", "Has Online Delivery"])
plt.title("Availability of Online Delivery")
plt.ylabel("Count")
plt.show()

avg_rating_booking = df.groupby('Has Table Booking')['Aggregate rating'].mean()
avg_rating_delivery = df.groupby('Has Online Delivery')['Aggregate rating'].mean()

plt.figure(figsize=(8, 4))
sns.barplot(x=avg_rating_booking.index, y=avg_rating_booking.values)
plt.xticks([0, 1], ["No Table Booking", "Has Table Booking"])
plt.title("Average Rating Based on Table Booking Availability")
plt.ylabel("Average Rating")
plt.ylim(0, 5)
plt.show()

plt.figure(figsize=(8, 4))
sns.barplot(x=avg_rating_delivery.index, y=avg_rating_delivery.values)
plt.xticks([0, 1], ["No Online Delivery", "Has Online Delivery"])
plt.title("Average Rating Based on Online Delivery Availability")
plt.ylabel("Average Rating")
plt.ylim(0, 5)
plt.show()
