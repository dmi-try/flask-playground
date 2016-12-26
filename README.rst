===============================
Flask Playground
===============================


.. image:: https://img.shields.io/pypi/v/flask_playground.svg
        :target: https://pypi.python.org/pypi/flask_playground

.. image:: https://img.shields.io/travis/dmi-try/flask_playground.svg
        :target: https://travis-ci.org/dmi-try/flask_playground

.. image:: https://readthedocs.org/projects/flask-playground/badge/?version=latest
        :target: https://flask-playground.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/dmi-try/flask_playground/shield.svg
     :target: https://pyup.io/repos/github/dmi-try/flask_playground/
     :alt: Updates


Simple Flask app


Flask Sandbox
=============

Small application for playing with Flask, Bootstrap and rich javascript.

Run with virtualenv (any OS)
============================

Install python 2.7 and virtualenv

Prepare virtualenv
```bash
$ virtualenv env
...
$ env/bin/pip install -r requirements.txt
...
```

Run server

```
$ env/python app.py
```

Build and run with Docker (Linux)
=================================

Build the image using the following command

```bash
$ docker build -t flask-playground:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 flask-playground
```

The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`


* Free software: Apache Software License 2.0
* Documentation: https://flask-playground.readthedocs.io.


Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

