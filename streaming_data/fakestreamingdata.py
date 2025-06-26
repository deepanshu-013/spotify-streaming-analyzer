import pandas as pd
import random
from datetime import datetime, timedelta

artists = ['Eminem', 'Drake', 'Linkin Park', 'The Weeknd', 'Taylor Swift']
tracks = {
    'Eminem': ['Lose Yourself', 'Mockingbird'],
    'Drake': ['God\'s Plan', 'One Dance'],
    'Linkin Park': ['Numb', 'In the End'],
    'The Weeknd': ['Blinding Lights', 'Starboy'],
    'Taylor Swift': ['Love Story', 'Blank Space']
}

data = []
start = datetime(2024, 5, 1)

for _ in range(200):
    artist = random.choice(artists)
    track = random.choice(tracks[artist])
    time = start + timedelta(minutes=random.randint(0, 40000))
    ms = random.randint(60000, 240000)
    data.append([time.strftime("%Y-%m-%d %H:%M"), artist, track, ms])

df = pd.DataFrame(data, columns=["endTime", "artistName", "trackName", "msPlayed"])
df.to_csv("fake_spotify_streaming.csv", index=False) 
