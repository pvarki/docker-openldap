FROM docker.io/bitnami/openldap:2.5.14

# Adds custom libopenldap.sh that:
# 1. properly disables anonymous access
# 2. Adds memberof-support to openLDAP
COPY rootfs /
