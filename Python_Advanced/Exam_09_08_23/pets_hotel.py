def accommodate_new_pets(capacity, allowed_weight, *args):
    pet_type_dict = {}
    max_weight_limit = allowed_weight
    accommodated_pets = 0
    string_to_print = ""
    pets_for_hotel = 0

    for pet_type, current_weight in args:
        if current_weight > max_weight_limit:
            continue
        if accommodated_pets == capacity:
            break
        pets_for_hotel += 1
        if pet_type not in pet_type_dict:
            pet_type_dict[pet_type] = 0
        pet_type_dict[pet_type] += 1
        accommodated_pets += 1

    sorted_pet_dict = dict(sorted(pet_type_dict.items(), key=lambda x: x[0]))

    if pets_for_hotel > capacity:
        string_to_print += "You did not manage to accommodate all pets!" + "\n"
    else:
        string_to_print += f"All pets are accommodated! Available capacity: {capacity - accommodated_pets}." + "\n"

    string_to_print += "Accommodated pets:" + "\n"
    for pet, count in sorted_pet_dict.items():
        string_to_print += f"{pet}: {count}" + "\n"

    return string_to_print

