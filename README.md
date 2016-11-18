# Gitmojime
Check your [Gitmoji](https://github.com/carloscuesta/gitmoji)'s compliance!

## Dev

Install and create venv
```sh
pip3 install virtualenv
virtualenv -p python3 venv
```

Start the virtualenv
```sh
source venv/bin/activate
```

Install requirements
```sh
pip install -r requirements.txt
```

To run the application
```sh
export FLASK_APP=app.py
export FLASK_DEBUG=1 # to reload when source change
flask run
```

