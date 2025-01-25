def does_name_exist(first_names, last_names, full_name):
    if first_names and last_names and full_name:
        for fname in first_names:
            for lname in last_names:
                if ((fname + ' ' + lname) == full_name) or ((lname + ' ' + fname) == full_name):
                    print(fname+ ' '+ lname)
                    print(full_name)
                    return True
        else :
            print(fname+ ' '+ lname)
            print(full_name)
            return False       
