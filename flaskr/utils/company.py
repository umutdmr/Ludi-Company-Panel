from datetime import datetime,timedelta
import json


def load_data(file_path, key):
    with open(file_path) as file:
        data = json.load(file)[key]
        return data
    
def get_user_number_company_data(simulations_file, simulations_key, users_file, users_key):

    simulations = load_data(simulations_file, simulations_key)
    users = load_data(users_file, users_key)
    
    sim_to_com_mapping = {simulation['simulation_id']: simulation['company_name'] for simulation in simulations}
    
    result = dict()
    for user in users:
        company_name = sim_to_com_mapping[user["simulation_id"]]
        if company_name in result:
            result[company_name] += 1
        else:
            result[company_name] = 1
    return result

def get_user_numbers_data(users_file, users_key):

    users = load_data(users_file, users_key)
    print(len(users))
    base_date = datetime(1899, 12, 30) 

    signup_dates = [base_date + timedelta(days=user['signup_datetime']) for user in users]
    
    signup_dates.sort()
    formatted_dates = [date.strftime('%Y-%m-%d') for date in signup_dates]
    
    dates_counts = dict()
    cumulative_count = 0
    for date in formatted_dates:
        cumulative_count += 1
        dates_counts[date] = cumulative_count
    result = {"dates": list(dates_counts.keys()), "counts": list(dates_counts.values())}

    return result
        