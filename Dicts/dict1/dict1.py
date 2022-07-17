def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """

    return dict(zip(keys,values))
    #pass  # implement me

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """

    res = {**d1, **d2}
    return res

    #pass  # implement me

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    create_dict = {i: d1 for i in lst}
    return (create_dict)

    #pass  # implement me

def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    create_dict = {key: value for key, value in datadict.items() if key in keylist}
    return(create_dict)

    #pass  # implement me

def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for key in keylist:
        datadict.pop(key)
    return (datadict)

    #pass

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return key in datadict.values()

    #pass

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    return(min(ddd, key=lambda key: ddd[key]))

    #pass

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """

    return (max(ddd, key=lambda key: ddd[key]))
    #pass