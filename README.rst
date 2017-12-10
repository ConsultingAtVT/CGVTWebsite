***********************************************
The Consulting Group at Virginia Tech's Website
***********************************************

.. contents::
    :local:
    :depth: 1
    :backlinks: none

========
Synopsis
========

This is the website for the Consulting Group at Virginia Tech, an undergraduate organization for students interested in business and management consulting careers. We believe in providing robust and transparent solutions to our clients, which is why we have open sourced our website.

The redesign of our site is still under active development, but we hope to be deploying our first production release soon. Our website acts as both the public-facing source of information about our organization as well as our internal CMS.

===========================
Configuring for Development
===========================

You need to make sure the following environment variables are set:

* ``DJANGO_SECRET_KEY``: Any random string.
* ``CGVT_LINKEDIN_API_CLIENT_ID``: You'll be given this if you're supposed to have it.
* ``CGVT_LINKEDIN_API_CLIENT_SECRET``: See previous.

Additionally, make sure you fill a file named ``valid-emails.json`` with a JSON array of strings which will contain the emails of whitelisted accounts. These emails must be linked with the corresponding LinkedIn accounts of the users you wish to test with.

Next, install `Python 3.5 <https://www.python.org/downloads/>`_ and install the dev dependencies::

    pip install -rrequirements-dev.txt

Additionally, you may need to install `the Visual C++ build tools <http://landinghub.visualstudio.com/visual-cpp-build-tools>`_.

Make sure you have `Node <https://nodejs.org/en/download/>`_ installed, and then install `less <http://lesscss.org/>`_ and `Gulp <http://gulpjs.com/>`_::

    npm install -g lessc gulp

Then, making sure you're in the top-level directory of the project, install the Semantic-UI source files::

    npm install semantic --save

If you ever want to build the Semantic-UI dist, just run::

    cd semantic
    gulp build

==========================
Configuring for Production
==========================

Check back here later on for a walkthrough on deploying a production instance of the site. Below is just a working copy of steps to follow that will be refined in the future.

Set the following environment variables:

* Set ``DISABLE_COLLECTSTATIC`` to 1 
* Set ``DJANGO_DEBUG_OFF`` to 1
* Set ``EMAIL_WHITELIST_GIST_URL`` appropriately

Make sure both Node.js and Python buildpacks are set if using Heroku.
