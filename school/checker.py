def clean_city_data(city):
    return ''.join(char for char in city if not char.isdigit())
