def capitalize_camel_case(string):
    return "".join([item.capitalize() for item in string.split('_')])
