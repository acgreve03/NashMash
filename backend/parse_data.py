import db

def parse_and_populate():
    with open("duuzudb.txt", "r", encoding="utf-8") as file:
        content = file.read()
        song_data = content.split("•")   #split by bullet point
        print(song_data[1])

        print(song_data[1].strip())

'''        for datum in song_data:
            datum = datum.strip()
            if not datum:
                continue'''

        

if __name__ == "__main__":
    parse_and_populate()

           



