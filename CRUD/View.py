from . import Operation

def read_console():
    data_file = Operation.read()
    index = "No"
    song = "Song"
    artist = "Artist"
    album = "Album"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {song:30} | {artist:30} | {album:30}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        created_at = data_break[1]
        artist = data_break[2]
        album = data_break[3]
        song = data_break[4]
        print(f"{index+1:4} | {song:.30} | {artist:.30} | {album:.30}", end=""+"\n")

    # Footeer
    print("="*100+"\n")

def create_console():
    print("\n\n"+"="*100)
    print("add song\n")
    song = input("Song\t: ")
    artist = input("Artist\t: ")
    album = input("Album\t: ")
    
    Operation.create(song, artist, album)
    print("\nYour new data")
    read_console()

def update_console():
    read_console()
    while(True):
        print("choose the song number")
        song_number = int(input("Song number: "))
        song_data = Operation.read(index=song_number)

        if song_data:
            break
        else:
            print("number not found")

    data_break = song_data.split(',')
    pk = data_break[0]
    created_at = data_break[1]
    artist = data_break[2]
    album = data_break[3]
    song = data_break[4][:-1]
    
    while(True):
        print("\n"+"="*100)
        print("choose the data")
        print(f"1. Song\t: {song:.30}")
        print(f"2. Artist\t: {artist:.30}")
        print(f"3. Album\t: {album:.30}")

        user_option = input("Choose data[1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": song = input("song\t: ")
            case "2": artist = input("artist\t: ")
            case "3": album = input("album\t: ")
        
        is_done = input("Done update (y/n)?")
        if is_done == "y" or is_done == "Y":
            break

    Operation.update(song_number, pk, created_at, artist, album, song)

def delete_console():
    read_console()

    while(True):
        print("choose the song number")
        song_number = int(input("Song number: "))
        song_data = Operation.read(index=song_number)

        if song_data:
            data_break = song_data.split(',')
            pk = data_break[0]
            created_at = data_break[1]
            artist = data_break[2]
            album = data_break[3]
            song = data_break[4][:-1]

            print("\n"+"="*100)
            print("choose the data to delete")
            print(f"1. Song\t: {song:.30}")
            print(f"2. Artist\t: {artist:.30}")
            print(f"3. Album\t: {album:.30}")
            is_done = input("do you want to delete? (y/n)?")
            if is_done == "y" or is_done == "Y":
                Operation.delete(song_number)
                break
        else:
            print("number not found")
        
    print("Data success deleted")