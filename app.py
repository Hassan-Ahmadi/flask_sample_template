from . import create_app

if __name__ == '__main__':
    app = create_app(config_name='production')
    # app = create_app(config_name='development')

    app.run(host='0.0.0.0', port=5001)

    # if any model file changed and migration was needed do following steps (in projects base path):
    # - if migrations folder does not exists:
    # 0. python3 -m flask db init
    # then:
    # 1. python3 -m flask db migrate
    # 2. python3 -m flask db upgrade
    # ** consider adding migrations folder to version control to track its modifications
