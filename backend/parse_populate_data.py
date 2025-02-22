import re
from sqlalchemy.orm import Session
from models import SessionLocal, Song, init_db

# 1. Load your song data from a file
with open("duuzudb.txt", "r", encoding="utf-8") as f:
    song_lines = f.readlines()

current_key = None  # Store the last seen key section

def parse_song_data(line):
    global current_key

    # Check if line is a key section (e.g., [G#min])
    key_match = re.match(r"\[([\w#]+min|[\w#]+maj)\]", line)
    if key_match:
        current_key = key_match.group(1).strip()  # Update current key
        return None  # Skip processing this line further

    # Capture artist name, handling '•' at the beginning
    artist_match = re.search(r"•?\s*([\w\s&.,'-]+?)\s*[-–]", line)
    artist = artist_match.group(1).strip() if artist_match else "Unknown Artist"

    # Capture song title
    song_title_match = re.search(r"[-–](.+?)(?=\(|\||$)", line)
    song_title = song_title_match.group(1).strip() if song_title_match else "Unknown Title"

    # Capture BPM, handling various formats (~, /, -)
    bpm_match = re.search(r"\(~?(\d+\.?\d*)(?:[\/\-](\d+\.?\d*))?\)", line)
    if bpm_match:
        bpm_low = float(bpm_match.group(1))
        bpm_high = float(bpm_match.group(2)) if bpm_match.group(2) else bpm_low
    else:
        bpm_low, bpm_high = None, None  # Handle missing BPM

    # Use the last seen key, or default to "Unknown Key"
    song_key = current_key if current_key else "Unknown Key"

    return {
        "artist": artist,
        "song_title": song_title,
        "bpm_low": bpm_low,
        "bpm_high": bpm_high,
        "key": song_key
    }




# 3. Test Parsing & Log Results
parsed_songs = []
skipped_lines = []

for idx, line in enumerate(song_lines):
    line = line.strip()
    
    # Check for key section first
    if line.startswith("[") and line.endswith("]"):
        parse_song_data(line)  # Update the key but don't add to song list
        continue  # Skip to the next line

    parsed = parse_song_data(line)

    # Check if parsing failed (artist or title is unknown)
    if parsed and (parsed["artist"] == "Unknown Artist" or parsed["song_title"] == "Unknown Title"):
        skipped_lines.append((idx + 1, line))  # Save skipped line number and content
    elif parsed:
        parsed_songs.append(parsed)


# 4. Populate the database
session = SessionLocal()

#Function to insert one song 
def insert_song(artist, title, bpm_low, bpm_high, key):
    song = Song(
        artist=artist,
        title=title,
        bpm_low=bpm_low,
        bpm_high=bpm_high,
        key=key
    )

    session.add(song)

for song in parsed_songs:
    insert_song(song["artist"], song["song_title"], song["bpm_low"], song["bpm_high"], song["key"])

session.commit()
session.close()

print(f" Successfully inserted {len(parsed_songs)} songs into the database.")
print(f"Skipped {len(skipped_lines)} lines. Check 'skipped_lines.txt' for details.")

# Save skipped lines for debugging
with open("skipped_lines.txt", "w", encoding="utf-8") as f:
    for line_num, content in skipped_lines:
        f.write(f"Line {line_num}: {content}\n")

'''# 4. Output Results
# Save successful parses
with open("parsed_songs.txt", "w", encoding="utf-8") as f:
    for song in parsed_songs:
        f.write(f"{song['artist']} - {song['song_title']} | BPM: {song['bpm_low']}-{song['bpm_high']} | Key: {song['key']}\n")

# Save skipped lines for debugging
with open("skipped_lines.txt", "w", encoding="utf-8") as f:
    for line_num, content in skipped_lines:
        f.write(f"Line {line_num}: {content}\n")

print(f"✅ Successfully parsed {len(parsed_songs)} songs.")
print(f"⚠️ Skipped {len(skipped_lines)} lines. Check 'skipped_lines.txt' for details.")'''
