# AnsibleGUI
sudo apt install python3.10-venv
sudo python3 -m venv runner
source runner/bin/activate
sudo chown -R igor:igor runner/
pip3 install django
cd runans
python manage.py migrate
python3 manage.py runserver 0.0.0.0:8000

