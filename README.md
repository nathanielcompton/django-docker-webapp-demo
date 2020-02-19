# Motley Fool Developer Interview Project
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Black Formatter](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![Codecov](https://img.shields.io/codecov/c/github/nathanielcompton/motley-devinterviewcompton)
![M.F. Interview Project](https://github.com/nathanielcompton/motley-devinterviewcompton/workflows/M.F.%20Interview%20Project/badge.svg)

This project contains my submission as part of The Motley Fool Developer Interview.
It showcases a number of important concepts that Python/Django engineers should stay
aware of.

## Technical Stack

This API service implements a few key libraries for demonstration of various related skill sets:

  - [Python 3.8]
  - [Django] - A lightweight WSGI web application framework for Python
  - [Black] - An uncompromising Python code formatter
  - [Pytest] - Small, scalable testing for Python
  - [Poetry] - Python packaging made easy
  - [Github Actions] - Version control and test-build-deploy pipeline automation
  - [Docker] - Containerization for faster, consistent and more reliable development

## Quickstart
This project requires [Python 3.8] and [Docker] to run.

```sh
# First, ensure the entrypoint script is executable.
$ chmod +x ./docker-entrypoint.sh
# Next, build Docker images and spin up containers.
$ docker-compose up -d --build
# Then, run initial Django migrations. This step is needed only as models change.
$ docker-compose exec web python manage.py migrate
```

To verify a successful build with Docker, navigate to: http://localhost:8000/sanity

Django can easily be interacted with through Docker as well.
```sh
docker-compose exec web [STANDARD_DJANGO_COMMAND] [OPTIONS]
```

Bringing down containers is done simply with:

```sh
$ docker-compose down -v
```

The combination of `docker-compose.yml` and the `Dockerfile` takes care of most of
the heavy lifting with installation, and in a reproducible and predictable manner:
  - Pulling appropriate Docker images from DockerHub
  - Setting up a PostgreSQL database, and connecting it to the Python environment
  - Installing all libraries and Python dependencies

With Python, the ability to quickly restart and rebuild a healthy
development environment without the hassle of traditional (and historically frustrating)
virtual environment management.

Verify a successful build by navigating to ``localhost:8000/sanity``.

## Code Formatting, Configuration Management and Cleanliness
I included the [Black] formatting tool to maintain a high-degree of code format
standardization. Using a tool like this takes the guess work out of keeping code up to
[PEP8/Flake8][PEP8] standards, and instead allows engineers to focus on deeper issues.

I also made sure to include samples of proper settings/configuration management:
  - `.env.dev` file to manage environment-level variables
  - Django's `settings.py` structure for application-level configuration
  - Other variables localized to as limited of a scope as possible
  - `.gitignore`, `.dockerignore`, Pytest ignored directories, etc.
  - `pyproject.toml` can be used by a number of Python package managers (Poetry, Pipenv,
    etc.) although it isn't needed for this demo.

## Testing and CI/CD
To run tests in the Docker container, call:
```sh
docker-compose exec web pytest
```

I set up the initial Pytest scaffolding to demonstrate proper test configuration.
Given more time, I would aim for test coverage > 75%.

## Evaluation Criteria: Notes
I spent the bulk of my work time showcasing my ability to both design and implement
clean, well-thought out code. Every file has at least some level of documentation, for
example. Many files have in-line `TODO` comments and thoughts regarding future
improvements.

- ```Front-end structure - Use of partials, CSS and JS structure.```
  - This was a great refresher course in using the Django's builtin templating language.
  - Data is dynamically generated on the `Home` and `Article` pages, both from calls to
  the PostgreSQL database (with Django O.R.M.)
- ```Django Framework usage.```
  - I hope my work both on this project and with this project and the
  "Python-API-Demo" Flask project I submitted with initially are able to show my command
  of Python and its various frameworks.
- ```URL Structure.```
  - The original URL structure appears to be ``publish_date`` and a ``headline`` "slug."
    - e.g. ``/investing/YYYY/MM/DD/slug-headline-here``
    - Django has a handy ``slugify()`` tool to properly convert ``headline`` data.
    - I chose to use the `Article.uuid` for demostration purposes/time constraints. I
    understand the added value of having articles sortable and searchable by datetime,
    author, tags, etc.
- ```Any database use.```
  - I created an entire working database layer from the given `*.json` files.
  - I created Django models (with migration) that map to the data in the `*.json` files.
  - I also created data-specific migration files to serve as an "E.T.L." script, and
  populate tables with the given data. This allows for the dynamic nature of both the
  `Home` and `Article` pages.
- ```Possible areas for future additions, improvement, or optimization.```
  - I left a number of in-line comments and docstrings explaining how I would like to
  improve and optimize moving forward. Here are a few additional bullet points:
    - Better and more useful database/model constraints
    - Completing AJAX / JS implementation in Django templates
    - Implementing currently unused data (tags, instruments, etc.)
    - Pagination of results as appropriate
    - Implementing users with authentication/authorization permissions
    - Securing and limiting API endpoint access as appropriate
    - Integration of things like: notifications, communication channels, etc.
    - CI/CD automation retries
    - Better mobile support
- ```Anything you did to make make the application your own.```
  - Lots of time spent on architecture and organization
  - Also, please visit the "THROWBACK" Easter egg website


## Final Thoughts
I had a genuinely pleasant time working on this project, and I definitely will continue
working as time permits. I am also extremely excited about the opportunity to work with
a solid team like Motley Fool. I see the opportunity as both a way for my to take
advantage of my current skills, and to get meaningful feedback and mentorship from
others with much more experience and knowledge. Thank you for your time!


License
----

[GNU GPLv3](LICENSE)


[//]: # (These are reference links are hidden during Markdown file build.)


   [Python 3.8]: <https://www.python.org/downloads/release/python-380/>
   [Django]: <https://www.djangoproject.com/>
   [Black]: <https://black.readthedocs.io/en/stable/>
   [Pytest]: <https://docs.pytest.org/en/latest/>
   [Pyenv]: <https://github.com/pyenv/pyenv>
   [Poetry]: <https://python-poetry.org/>
   [OAS v3.0]: <https://www.openapis.org/>
   [Github Actions]: <https://github.com/features/actions>
   [Docker]: <https://www.docker.com/>
   [PEP8]: <https://www.python.org/dev/peps/pep-0008/>
