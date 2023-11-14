from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Song) -> None:
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        for current_instance in self.songs:
            if current_instance.name == song.name:
                return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        song_to_be_removed = list(filter(lambda x: (x.name == song_name), self.songs))
        if song_to_be_removed:
            string_to_print = f"Removed song {song_name} from album {self.name}."
            self.songs.remove(song_to_be_removed[0])
            return string_to_print
        else:
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = [current_song.get_info() for current_song in self.songs]
        str_to_print = "\n".join(f"== {element}" for element in info) + "\n"
        return str_to_print
