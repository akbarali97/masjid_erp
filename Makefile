venv:
	python -m venv venv

install:
	. ./venv/bin/activate && python -m pip install -r requirements.txt

run:
	. ./venv/bin/activate && odoo/odoo-bin -c odoo.conf

upgrade:
	. ./venv/bin/activate && odoo/odoo-bin -c odoo.conf -u masjid_membership --stop-after-init