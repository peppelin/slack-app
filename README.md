# Slack app IT
>Slack app for managing IT stuff

Small [Flask](http://flask.pocoo.org/) application built in dokcer and integrated in Slack. Using slash commands, you can query the API and request stuff.

![](resources/header.png)

## Requeriments
* Docker
* Docker compose
* Flask
* Python

## Installation

OS X & Linux:

```sh
git clone slack-app
cd slack-app
docker-compose up -d
```

## Description

```
.
├── app
│   ├── app.py
│   ├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```

In the root folder, there's the docker-compose.yml file and the Dockerfile to build the slack-app with Flask.
* Mounts the app volume inside the docker container
* Exposes the port *5000* for the flask app.
In the app folder, you'll find the main python scripts to run Flask API and the requirements.txt for pip installation.

## Usage example

Right now, you can run the */hi* slash command and append a text to get it back un bold.

![](images/slash.gif)

## Development setup

Be sure to have installed docker and docker-compose.
The images python:alpine are being used for builfing the app.

## Release History

* 0.0.1
    * Work in progress
    * Proof of concept to build the api, test connectivity and work with the POST arguments.

## Meta

Joan Gargallo – [@peppelin](https://twitter.com/peppelin) – peppelin@gmail.com

[https://github.com/peppelin](https://github.com/peppelin/)

## Contributing

1. Fork it (https://bitbucket.org/mediastream_ag/slackbot/src)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

# Useful information
* [Docker](https://www.docker.com/)
* [Slack slach commands](https://api.slack.com/slash-commands)
* [Slack apps](https://api.slack.com/slack-apps)
* [Flask API](http://flask.pocoo.org/docs/1.0/api/)
* [Flask tutorial](https://www.patricksoftwareblog.com/steps-for-starting-a-new-flask-project-using-python3/)

<!-- Markdown link & img dfn's -->
