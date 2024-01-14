# class Car:
#     def __init__(self, max_speed: int) -> None:
#         self.max_speed = max_speed

#     def drive(self):
#         print("driving max speed" + str(self.max_speed))

#     @property
#     def max_speed(self):
#         return self.__max_speed

#     @max_speed.setter
#     def max_speed(self, value):
#         if value >= 447:
#             value = 447
#         self.__max_speed = value


# red_car = Car(200)
# red_car.drive()
# red_car.max_speed = 512

class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, value):
        if  len(value) > 15 or len(value) < 5:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @password.setter
    def password(self, value):
        has_digit = False
        has_upper_case = False
        above_eight_chars = False
        list_of_digits = [e for e in value if e.isdigit()]
        list_of_upper_case = [e for e in value if e.isupper()]

        if len(value) >= 8:
            above_eight_chars = True
        if len(list_of_digits) >= 1:
            has_digit = True
        if len(list_of_upper_case) >= 1:
            has_upper_case = True

        if has_digit and has_upper_case and above_eight_chars:
            self.__password = value
            return

        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")


# class Profile:
#     def __init__(self, username):
#         self.__username = username

# class SubProfile(Profile):
#     def __init__(self, username, extra_info):
#         super().__init__(username)
#         self.extra_info = extra_info

# # Create instances
# profile = Profile("JohnDoe")
# sub_profile = SubProfile("JaneDoe", "Some extra info")

# # Attempt to accidentally override '__username' in SubProfile
# sub_profile.__username = "NewUsername"

# # Resulting output
# print(profile._Profile__username)      # Output: JohnDoe
# print(sub_profile._Profile__username)  # Output: JaneDoe
