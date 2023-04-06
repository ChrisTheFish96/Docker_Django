# Docker_Django

## Description
This is a dockerized Django application with Sphinx documentation on the main application.

## Table of Contents
1. Prerequisites
1. Download and installation
1. Running in venv and Docker
1. Credits

## Prerequisites
* Docker
* virtualenv
   * Enable `pip install virtualenv`

## Download and installation
1. Clone this repository
1. Delete the .git folder
  * `rm -rf .git/`
1. Create a virtual environment and activate it
  * `virtualenv venv`
  * `source venv/Scripts/activate`
1. Change the SECURITY KEY within settings.py to include your SECURITY KEY
  ![settings screenshot](https://user-images.githubusercontent.com/125367266/230436180-d162aea2-9a9a-499b-b74f-c1fb3310d3e4.JPG)
1 Build a docker image
  * `docker build --tag <image_name>:latest `
  * This will install all nessecary packages from the requirements.txt file included in clone
1. Create and run the Docker Container
  * `docker run --name <container_name> -d -p 8000:8000 <image_name>:latest`
  * The site should then be available on your local host on port 8000
  * 
## Credits
This project was created by Christopher Barnard (ChrisTheFish96)
