from controller.api import api_blueprint as controller
from utils import common
from base_model import Session
from services import ActorService


@controller.route('/actors', methods=['GET'])
def get_users():
    return common.json_response({'name': 'sanish'})


@controller.route('/actor/<id>', methods=['GET'])
def get_user(id):
    session = Session()
    actor = ActorService.get_by_id(id, session)
    return common.json_response(actor)
