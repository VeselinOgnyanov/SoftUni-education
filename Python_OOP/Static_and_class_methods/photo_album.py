from math import ceil


class PhotoAlbum:
    LIMITED_PHOTOS = 4

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos = [[] for x in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages_needed = ceil(photos_count / PhotoAlbum.LIMITED_PHOTOS)
        return cls(pages_needed)

    def add_photo(self, label:str):
        for index in range(len(self.photos)):
            if len(self.photos[index]) < 4:
                self.photos[index].append(label)
                string_to_return = f"{label} photo added successfully on page {index + 1} "
                string_to_return += f"slot {len(self.photos[index])}"
                return string_to_return
        return "No more free slots"

    def display(self):
        list_to_print = ["[] " * len(row) for row in self.photos]
        string_to_print = "-----------"
        for row_element in list_to_print:
            stripped_element = row_element.rstrip()
            string_to_print +="\n" + stripped_element + "\n"
            string_to_print += "-----------"
        return string_to_print
