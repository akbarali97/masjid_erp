venv:
	python -m venv venv

install:
	. ./venv/bin/activate && python -m pip install -r requirements.txt

run:
	. ./venv/bin/activate && odoo/odoo-bin -c odoo.conf