// Playlist //

playlist = {
    "SAD!": {
        "artist": "xxxtentacion",
        "genre": "Hip-Hop"
    }
}


def add_song(title, artist, genre):
    if title in playlist:
        print(f"The song '{title}' by {artist} is already in the playlist.")
    else:
        playlist[title] = {
            'artist': artist,
            'genre': genre
        }
        print(f"The song '{title}' has been added to the playlist.")



def view_playlist():
    if playlist:
        for title, details in playlist.items():
            print(f"Title: {title}, Artist: {details['artist']}, Genre: {details['genre']}")
    else:
        print("The playlist is empty.")



def update_song(title, artist=None, genre=None):
    if title in playlist:
        if artist:
            playlist[title]['artist'] = artist
        if genre:
            playlist[title]['genre'] = genre
        print(f"Updated '{title}' successfully.")
    else:
        print(f"Song titled '{title}' not found in the playlist.")




def delete_song(title):
    if title in playlist:
        del playlist[title]
        print(f"Deleted '{title}' from the playlist.")
    else:
        print(f"Song titled '{title}' not found in the playlist.")






# Testing 

# Adding new songs
add_song("Fluorescent Adolescent", "Arctic Monkeys", "Indie Rock")
add_song("Dog Days Are Over", "Florence + The Machine", "Indie Rock")
add_song("Smells Like Teen Spirit", "Nirvana", "Grunge")
add_song("Juice", "Snoop Dogg", "Rap")
add_song("Comprendo", "Morad", " Spanish Rap")
add_song("bande organisee", "Jul", "French Rap")

# Viewing the playlist
view_playlist()

# Updating a song's info
update_song("Juice", genre="Old Rap")

# Viewing the playlist after the update
view_playlist()

# Deleting a song from the playlist
delete_song("Juice")

# Viewing the playlist after deletion
view_playlist()
