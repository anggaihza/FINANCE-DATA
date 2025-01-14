from datetime import datetime

date_format = "%d=%m-%Y"

def get_date(promp, allow_default=False):
    date_str = input(promp)
    if(allow_default and not date_str):
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strftime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter dd-mm-yyyy.")
        return get_date(promp, allow_default)

def get_amount():
    pass

def get_category():
    pass

def get_description():
    pass