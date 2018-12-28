from controller import controller_blueprint as controller


@controller.route('/home', methods=['GET'])
def home():
    return 'This is home page'


@controller.route('/exception', methods=['GET'])
def exception():
    raise Exception("This is a demo exception")
