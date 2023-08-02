def kwargs_length(**dict_to_measure):
    return len(dict_to_measure)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
