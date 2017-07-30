FROM odoo:10
MAINTAINER Toolkit <dev@toolkt.com>

# Install dependencies fabric pysftp odoorpc xlswriter
USER root
RUN set -x; \
        apt-get update \
        && apt-get install -y --no-install-recommends \
        	fabric \
		&& pip install pysftp==0.2.8 odoorpc xlsxwriter

COPY ./odoo.conf /etc/odoo/
COPY ./addons/ /mnt/extra-addons