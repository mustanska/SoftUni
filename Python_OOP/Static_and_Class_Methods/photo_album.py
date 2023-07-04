from math import ceil
from typing import List


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(pages)]
        self.current_page_index = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str) -> str:
        try:
            if len(self.photos[self.current_page_index]) == 4:
                self.current_page_index += 1

            self.photos[self.current_page_index].append(label)

            return f"{label} photo added successfully on page {self.current_page_index + 1} " \
                   f"slot {len(self.photos[self.current_page_index])}"

        except IndexError:
            return "No more free slots"

    def display(self):
        result = f"{'-' * 11}\n"

        for photo in self.photos:
            result += f"{' '.join(['[]' for _ in photo])}\n"
            result += f"{'-' * 11}\n"

        return result


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
