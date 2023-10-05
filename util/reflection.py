def populate_object(obj, data_dictionary):
    fields = data_dictionary.keys()

    for field in fields:
        if getattr(obj, field):
            setattr(obj, field, data_dictionary[field])
