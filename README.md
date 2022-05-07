# Character Creation Web App - Backend

A web app that allows the user to create a character for a role-playing game, save that character on the server, and use it in the future while they're playing the game.
The aim of creating this application is to develop skills in developing a full stack application from scratch as a passion project.

This is a REST driven backend server that provides the business logic and database persistence required for typical character creation.
The API is developed to be easily read and maintained and to be scalable in the long-term.

The frontend is found here: https://github.com/GeorgeHarland/character-creation-frontend

This project is a collaboration between:

Kris W - https://github.com/kristian-welsh

George H - https://github.com/GeorgeHarland

Forked from https://github.com/kristian-welsh/character-creation-backend

## Getting Started

These instructions will give you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

pip         21.3.1
python      3.9.7
flask       2.0.2
flask_cors  3.0.10
mongodb     5.0.6
pymongo     4.0.1
docker      20.10.12

### Installing

With docker:

docker compose up

Running without docker:

pip -r install requirements.txt
python -m flask run

Then you can start sending REST requests against localhost:5000

## Contributing

We would love for anyone to submit pull requests with improvements. Please try to match the styles we have kept to.
Subject to our review.

## License

This project is licensed under the Creative Commons License.

## Acknowledgments

We appreciate GitHub as a service to make development and collaboration easier.
Thank you to the contributers of our dependancies.
