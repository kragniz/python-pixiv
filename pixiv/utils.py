def copy_dict_items_to_object(obj, dic, items):
    for name in items:
        obj.__dict__[name] = dic.get(name)
