from app import app

if __name__ == '__main__':
    app.debug = True
    #app.run(host='138.68.109.220', port = '5000')
    #asi podemos acceder al servidor de forma externa
    app.run(host='0.0.0.0')