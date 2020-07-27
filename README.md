# django_on_docker
Django Development with Docker Compose

# Development

# Build the images and run the containers:

#Give permission to entrypoint.sh file
chmod +x app/entrypoint.sh

#Start containers in detached mode (as a daemon)
docker-compose up -d --build

#Run the migrations
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py collectstatic

# Command to check the volume
docker volume inspect django_on_docker_postgres_data

#Command to check the default django table
docker-compose exec db psql --username=addr_book --dbname=addr_book_dev

#List running containers
docker ps

#Stops running containers
docker stop a56f91ddccb2

#remove the volumes along with the containers
docker-compose down -v

Test it out at http://localhost:8000. The "app" folder is mounted into the container and your code changes apply automatically.

# Production

# Uses gunicorn + nginx.
#Build the images and run the containers:
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml logs -f
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
docker-compose exec db psql --username=addr_book --dbname=addr_book_prod

Test it out at http://localhost:1337. To apply changes, the image must be re-built.