# dmpi-central
Del Monte Central Database


docker build -t toolkt/odoo:odoo_rancher .
docker push toolkt/odoo:odoo_rancher


RANCHER SETTINGS

HOST=postgres
USER=odoo
PASSWORD=odoo


sudo docker exec -i -t r-odoo10-dmpicentral-1-d39fbaee /bin/bash 
docker logs 

r-odoo10-dmpicentral-1-d39fbaee
r-odoo10-dmpicentral-1-261d5019


#Run with custom attributes


docker container restart 91d754e && docker logs -f 91d754e