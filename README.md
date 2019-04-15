# Nansen Legacy forena and Python 3 code for the sample log


Author: [paalge](https://github.com/paalge) (Pål Ellingsen)\
README updated: 2019-03-08 by Pål Ellingsen


This repository contains the web code for Forena (http://forenasolutions.org/) in Drupal to run the sample log for the Nansen Legacy on the SIOS page. It contains both the sql queries under sql and the frx files for generating the reports. 
These folders should be symlinked into the respective folders under the Forena page. 

The export folder contains a script in Python 3 for exporting the postgresql search to a csv file. It requires cgi on the server.