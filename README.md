# openLDAP for PVARKI

## Local testing

1. Run ```docker-compose -f docker-compose-local.yml up```

This sets bootstraps Keycloak, openLDAP and postgres automatically, and also configures Keycloak.

## Create users

1. Open http://keycloak:8080/admin/master/console/ in browser
2. Select realm RASENMAEHER
3. Add group
4. Create user

This data should be automatically be sync with LDAP.

## Testing

Execute inside openldap container with uid of created user:

```
ldapsearch -LL -Y EXTERNAL -H ldapi:/// "(uid=testuser)" -b dc=example,dc=org memberOf
```
