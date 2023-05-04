# NBA 2022-2023 Season - Players

<p align="center">
<img src = "https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54")>
<img src = "https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
<img src = "https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
</p>
<p align="center">

This is an API displaying player stats for the 2022-2023 NBA season.  
Endpoints include:  
- '/players' endpoint provides a bio for every player in the NBA 
- '/players/<id>' endpoint where users can search for a specific player by their player_id 
- '/offense' endpoint provides an overview of every player's offensive stats (shooting, assists etc) 
- '/defense' endpoint provides an overview of every player's defensive stats (e.g. steals, blocks, rebounds etc)

A Docker file has been included for deployment as well as a requirements file listing the dependencies that were necessary to build the application.
To test the API locally, run the following commands:  
- docker build -f api.Dockerfile . -t nba
- docker run -p 8080:8080 -t nba

At this point, the Flask application will be running in the Docker container and the user can find the API at 0.0.0.0:8080
