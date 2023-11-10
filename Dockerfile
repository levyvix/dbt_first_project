# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_DB=database
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin

# Expose the default PostgreSQL port
EXPOSE 5432

# Create a volume to persist data outside the container
VOLUME ["/var/lib/postgresql/data"]

# Set the working directory to the default PostgreSQL data directory
WORKDIR /var/lib/postgresql/data
