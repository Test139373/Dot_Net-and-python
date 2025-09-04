from app import app
import config

app.secret_key = config.SECRET_KEY
app.debug = config.DEBUG

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)