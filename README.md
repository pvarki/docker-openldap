# openLDAP with PVARKI defaults

## Local testing

1. Run ```docker-compose -f docker-compose-local.yml up```

Execute inside openldap container with uid of created user:

```
ldapsearch -LL -Y EXTERNAL -H ldapi:/// "(uid=testuser)" -b dc=example,dc=org memberOf
```
