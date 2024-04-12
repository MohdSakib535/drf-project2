def clean_city_data(city):
    if not city:
        return ""
    return ''.join(char for char in city if not char.isdigit())



def clean_name_data(city):
    if not city:
        return ""
    return ''.join(char for char in city if  char.isalpha())




def clean_roll_data(city):
    if not city:
        return ""
    return ''.join(char for char in city if  char.isdigit())