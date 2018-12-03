from controller import controller_blueprint as controller


@controller.route('/home', methods=['GET'])
def home():
    return 'This is home page'
