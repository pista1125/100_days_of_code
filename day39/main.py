import requests
from data_manager import DataManager

sheet_data = DataManager()

headers = {
    'accept': 'application/json',
    'apikey': 'a4WoTyNzP6TC4XomHLbrjLp8yi8tm6rn',
}

params = {
    'fly_from': 'FRA',
    'fly_to': 'PRG',
    'date_from': '23/11/2023',
    'date_to': '03/12/2023',
    'return_from': '23/11/2023',
    'return_to': '06/12/2023',
    'nights_in_dst_from': '2',
    'nights_in_dst_to': '3',
    'max_fly_duration': '20',
    'ret_from_diff_city': 'true',
    'ret_to_diff_city': 'true',
    'one_for_city': '0',
    'one_per_date': '0',
    'adults': '2',
    'children': '2',
    'selected_cabins': 'C',
    'mix_with_cabins': 'M',
    'adult_hold_bag': '1,0',
    'adult_hand_bag': '1,1',
    'child_hold_bag': '2,1',
    'child_hand_bag': '1,1',
    'only_working_days': 'false',
    'only_weekends': 'false',
    'partner_market': 'us',
    'max_stopovers': '2',
    'max_sector_stopovers': '2',
    'vehicle_type': 'aircraft',
    'limit': '500',
}

#response = requests.get(url='https://api.tequila.kiwi.com/v2/search', params=params, headers=headers)

#print(response.text)

#sheet_data.get_data()
sheet_data.edit_data()

