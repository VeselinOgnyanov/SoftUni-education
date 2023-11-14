from project.album import Album
from project.song import Song


class Band():
    def __init__(self, name: str) -> None:
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        filtered_album = list(filter(lambda x: (x.name == album.name), self.albums))
        if filtered_album:
            if filtered_album[0] in self.albums:
                return f"Band {self.name} already has {filtered_album[0].name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        filtered_album = list(filter(lambda x: (x.name == album_name), self.albums))
        if filtered_album[0] in self.albums:
            if filtered_album[0].published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(filtered_album)
            return f"Album {album_name} has been removed."
        else:
            return f"Album {filtered_album[0].name} is not found."

    def details(self):
        info = [x.details() for x in self.albums]
        str_to_print = ""
        str_to_print += self.name + "\n"
        str_to_print += "\n".join(f"{element}" for element in info)
        return str_to_print



# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
