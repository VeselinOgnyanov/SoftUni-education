def movie_organizer(*args):
    all_movie_dict = {}
    string_to_print = ""
    for current_tuple in args:
        movie_name = current_tuple[0]
        movie_category = current_tuple[1]
        if movie_category not in all_movie_dict:
            all_movie_dict[movie_category] = []
        all_movie_dict[movie_category].append(movie_name)

    all_movie_dict = dict(sorted(all_movie_dict.items(), key= lambda k: (-len(k[1]), k[0], k[1])))

    for key, value in all_movie_dict.items():
        key_length = len(all_movie_dict[key])
        string_to_print += f"{key} - {key_length}" + "\n"
        sorted_movie = sorted(value)
        for el in sorted_movie:
            string_to_print += f"* {el}" + "\n"
    return string_to_print


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
