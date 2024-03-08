# Use the official PostgreSQL image as the base image
FROM postgres:16

COPY docker/postgres/init.sql /docker-entrypoint-initdb.d/

CMD ["sh", "-c", "docker-entrypoint.sh postgres && psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -f /docker-entrypoint-initdb.d/init.sql" ]