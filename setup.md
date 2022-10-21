## Python installations
In all of the below, if commands aren't working, you can substitute `python` for `python3` and `pip` for `pip3` and see if that runs. That has the potential to land you in Python version jail (having multiple installations on your machine with different things installed in either), which can be hard to debug -- so try to be consistent about which kind of Python you're using!

If you already have pip installed, run
```
pip install flask
pip install requests
pip install python-dotenv
pip install Flask-SQLAlchemy
```

If you don't have pip and you're on a Mac, run
```
python3 -m ensurepip --upgrade
```

If you're on WSL and need pip, do
```
sudo apt-get update
sudo apt install python3-pip
```
then run the installations above.

If you're on Powershell, best of luck to you.