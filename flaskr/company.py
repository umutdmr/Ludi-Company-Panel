from flask import Blueprint, render_template # type: ignore
from flaskr.utils.company import get_user_number_company_data, get_user_numbers_data 

company_bp = Blueprint('company', __name__, url_prefix="/")

simulations_file = "flaskr/data/simulations.json"
simulations_key = "simulations"

users_file = "flaskr/data/users.json"
users_key = "users"

@company_bp.route("/")
def home_page():
    company_data = get_user_number_company_data(simulations_file, simulations_key, users_file, users_key)
    signup_data = get_user_numbers_data(users_file, users_key)
    return render_template('index.html', company_response=company_data, users_response=signup_data)

