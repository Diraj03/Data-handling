# import the required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# import the dataset
data = pd.read_csv('spotify.csv', encoding='ISO-8859-1')
print(data.columns)
print(data)

# Describe function to find the stats of each column
print(data.describe().T)

# checking the Nan values each columns
print(data.isnull().sum())

# Replacing the null values by zero
data.fillna(0, inplace=True)

data.isnull().sum()
# Info of each columns
print(data.info())

top_artist = data.sort_values(['Views'], ascending=False)
print(top_artist)

# Filtering out the top songs based on the views and stream
Top_songs = data.groupby('Track').sum()
Top_songs['TotalListened'] = Top_songs['Views'] + Top_songs['Stream']
Top_songs = Top_songs.sort_values(
    'TotalListened', ascending=False).reset_index().head(10)
print(Top_songs)

# Filtering out the top albums based on the Stream
top_album = data.sort_values(['Stream'], ascending=False)
print(top_album)

fig = plt.figure(figsize=(30, 25))
fig.suptitle('Spotify Music Analysis Dashboard \n Diraj Kumar-2204560 \n\n This dashboard provides a visual analysis of Spotify music data, focusing on the top 10 songs listened based on their views,stream and likes.The bar plot shows the total number of times each song was played. \n The scatter plot describes their stream and like counts.The violin plot shows the duration based on the album type, and the final plot describes the danceability and energy of the songs.',
             fontweight='bold', fontsize=24)

# Creating grid spec
gs = GridSpec(2, 2, figure=fig)
ax1 = fig.add_subplot(gs[0, 0])
# creating barplot
sns.set_style("dark")
sns.barplot(data=Top_songs, y='Track', x='TotalListened', palette='Blues')
# labels to x & y axis
plt.xlabel('Video Likes in millions', fontweight='bold', fontsize=20)
plt.ylabel('Tracks', fontweight='bold', fontsize=20)
plt.xticks(fontweight='bold', fontsize=18)
plt.yticks(fontweight='bold', fontsize=18)
# adding title to the plot
plt.title('Top 10 Songs', fontweight='bold', fontsize=20)

ax2 = fig.add_subplot(gs[0, 1])
sns.set_style("dark")
# creating scatterplot
plt.scatter(data['Stream'], data['Likes'], c='steelblue')
# labels to x & y axis
plt.xlabel('Stream Count', fontweight='bold', fontsize=20)
plt.ylabel('Likes', fontweight='bold', fontsize=20)
plt.xticks(fontweight='bold', fontsize=18)
plt.yticks(fontweight='bold', fontsize=18)
# adding title to the plot
plt.title('Most streamed music based on likes', fontweight='bold', fontsize=20)

ax3 = fig.add_subplot(gs[1, 0])
sns.set_style("dark")
# creating violinplot
sns.violinplot("Album_type", "Duration_ms", data=top_artist,
               palette=["lightblue", "deepskyblue", "dodgerblue"])
# labels to x & y axis
plt.xlabel('Album Type', fontweight='bold', fontsize=20)
plt.ylabel('Duration (ms)', fontweight='bold', fontsize=20)
plt.xticks(fontweight='bold', fontsize=18)
plt.yticks(fontweight='bold', fontsize=18)
# adding title to the plot
plt.title('Duration of Songs by Album Type', fontweight='bold', fontsize=20)

ax4 = fig.add_subplot(gs[1, 1])
# creating kdeplot
with sns.axes_style('dark'):
    sns.kdeplot(data['Danceability'], data['Energy'],
                cbar_ax='steelblue', gridsize=30, shade=True)
plt.xticks(fontweight='bold', fontsize=18)
plt.yticks(fontweight='bold', fontsize=18)
# adding title to the plot
plt.title('Danceability vs Energy of the Tracks',
          fontweight='bold', fontsize=20)

fig.savefig('22024560.png',dpi=300)
plt.show()

