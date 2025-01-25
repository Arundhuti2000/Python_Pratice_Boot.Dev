def count_names(list_of_lists, target_name):
    count=0
    if list_of_lists and target_name:
        for influencer in list_of_lists:
            for username in influencer:
                if target_name in username:
                    count+=1
    return count
     