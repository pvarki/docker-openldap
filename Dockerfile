FROM docker.io/bitnami/openldap:2.5.14

# Adds custom libopenldap.sh that:
# 1. Properly disables anonymous access
# 2. Adds memberof-support to openLDAP
# 3. Set default custom tree.ldif (if it needs to be customized we need to update the /opt/bitnami/scripts/openldap/entrypoint.s script)
COPY ./rootfs /
