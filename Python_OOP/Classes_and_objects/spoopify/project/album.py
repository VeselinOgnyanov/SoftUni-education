class Album:
    def __init__(self, name: str) -> None:


The Album class should receive a name (string) upon initialization and might receive one or more songs.
It also has instance attributes: published (False by default) and songs (an empty list).
It has four methods:
    • add_song(song: Song)
        ◦ Adds the song to the album and returns "Song {song_name} has been added to the album {name}."
        ◦ If the song is single, returns "Cannot add {song_name}. It's a single"
        ◦ If the album is published, returns "Cannot add songs. Album is published."
        ◦ If the song is already added, return "Song is already in the album."
    • remove_song(song_name: str)
        ◦ Removes the song with the given name and returns "Removed song {song_name} from album {album_name}."
        ◦ If the song is not in the album, returns "Song is not in the album."
        ◦ If the album is published, returns "Cannot remove songs. Album is published."

    • publish()
        ◦ Publishes the album (set to True) and returns "Album {name} has been published."
        ◦ If the album is published, returns "Album {name} is already published."
    • details()
        ◦ Returns the information of the album, with the songs in it, in the format:
"Album {name}
 == {first_song_info}
 == {second_song_info}
 …
 == {n_song_info}"
