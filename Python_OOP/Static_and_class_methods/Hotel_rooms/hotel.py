from room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def filtered_hotel_room(room_number, room_list):
        filtered_room = list(filter(lambda x: x.number == room_number, room_list))
        return filtered_room

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        result = self.filtered_hotel_room(room_number=room_number, room_list=self.rooms)
        current_room = result[0]
        taken_room = current_room.take_room(people)
        if taken_room:
            return taken_room
        self.guests += people

    def free_room(self, room_number):
        result = self.filtered_hotel_room(room_number=room_number, room_list=self.rooms)
        current_room = result[0]
        room_guests = current_room.guests

        freed_room = current_room.free_room()

        if freed_room:
            return freed_room
        self.guests -= room_guests

    def status(self):
        string_of_free_rooms_header = "Free rooms: "
        string_of_free_rooms = ", ".join([str(x.number) for x in self.rooms if not x.is_taken])
        string_to_append_free_rooms = string_of_free_rooms_header + string_of_free_rooms

        string_of_taken_rooms_header = "Taken rooms: "
        string_of_taken_rooms = ", ".join([str(x.number) for x in self.rooms if x.is_taken])
        string_to_append_taken_rooms = string_of_taken_rooms_header + string_of_taken_rooms

        list_to_convert = []
        list_to_convert.append(f"Hotel {self.name} has {self.guests} total guests")
        list_to_convert.append(string_to_append_free_rooms)
        list_to_convert.append(string_to_append_taken_rooms)

        return "\n".join(list_to_convert)




# Taken rooms: {numbers of all taken rooms separated by comma and space}"
