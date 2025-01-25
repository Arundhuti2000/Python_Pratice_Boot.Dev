# def find_last_name(names_dict, first_name):
#     for current_first_name, last_name in names_dict.items():
#         if current_first_name == first_name:
#             return last_name

def find_last_name(names_dict, first_name):
    if first_name in names_dict and first_name:
        last_name = names_dict[first_name]
        return last_name
    return
    