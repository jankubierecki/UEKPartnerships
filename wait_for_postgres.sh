until docker run --rm --link uekpartnership_postgres_1:pg --net postgres:10-alpine pg_isready -U postgres -h pg; do sleep 1; done
echo "postgres is ready"