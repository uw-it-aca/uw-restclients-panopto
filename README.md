# REST client for the UW HRP Web Service
# UW-RestClients-Panopto

[![Build Status](https://api.travis-ci.org/uw-it-aca/uw-restclients-panopto.svg?branch=master)](https://travis-ci.org/uw-it-aca/uw-restclients-panopto)
[![Coverage Status](https://coveralls.io/repos/uw-it-aca/uw-restclients-panopto/badge.png?branch=master)](https://coveralls.io/r/uw-it-aca/uw-restclients-panopto?branch=master)

Installation:

    pip install UW-RestClients-Panopto

To use this client, you'll need these settings in your application or script:

   RESTCLIENTS_PANOPTO_HOST='https://...'  
   RESTCLIENTS_PANOPTO_AUTH_TOKEN='<authorization_token>'

Optional settings:

    # Customizable parameters for urllib3
    RESTCLIENTS_PANOPTO_TIMEOUT=60
    RESTCLIENTS_PANOPTO_POOL_SIZE=10
