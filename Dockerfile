FROM docker.io/bitnamilegacy/openldap:2.5.14

# Install debian updates
USER root
RUN apt-get update && apt-get upgrade -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
USER 1001

# Adds custom libopenldap.sh that:
# 1. Properly disables anonymous access
# 2. Adds memberof-support to openLDAP
# 3. Set default custom tree.ldif (if it needs to be customized we need to update the /opt/bitnami/scripts/openldap/entrypoint.s script)
COPY ./rootfs /
