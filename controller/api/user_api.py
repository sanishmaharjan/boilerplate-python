from controller.api import api_blueprint as controller
from utils import common


@controller.route('/users', methods=['GET'])
def get_users():
    return common.json_response({'name': 'sanish'})
