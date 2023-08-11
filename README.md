## HOW TO RUN PROJECT

- build project `docker-compose up -d --build`
- create super user `docker exec -it test_app python3 manage.py createsuperuser`
- and app is available in http://0.0.0.0:8005/
- http://0.0.0.0:8005/api/docs/ - API documentation
- http://0.0.0.0:8005/api/products/ - products list
- http://0.0.0.0:8005/api/products/export/ - getting an excel file
- http://0.0.0.0:8005/api/login/ - user authorization
- http://0.0.0.0:8005/api/register/ - user registration
- http://0.0.0.0:8005/api/token/refresh/ - refresh token
