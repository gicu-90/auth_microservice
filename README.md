Stack:
    DRF, Nginx, Gunicorn, Docker

Docker comands:
    docker-compose up auth_app
    docker-compose run auth_app /prj/drfapp/source/manage.py migrate
    docker-compose run auth_app sh

Tutorials related:
    https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
    https://hasansajedi.medium.com/microservice-app-with-drf-part2-1c94cb0c5c05

Description:
    DRF auth microservice
    
    auth/login/ - takes 'email' 'password' and return jtw 'refresh', 'access'
    
    auth/login/refresh/ - takes 'refresh' token and returns a new jtw 'refresh', 'access' 
    
    auth/register/ - takes 'email' 'password' and return jtw 'refresh', 'access'

    in both jwt refresh and access are encoded user data
