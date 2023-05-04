# Geolocational Data Analyser
> Classify Various Residential Places using REST API and Machine Learning

[![Python Version][python-image]][python-url]
![REST API][rest-api-image]
![Build Status][travis-image]

This Python Notebook aims to Classify various Residential places on any coordinate (Eg : Delhi) using K-Means Machine Learning Algorithm, Minisom and HERE REST API

![](header.png)

## Installation

Windows and Mac OS X and Linux :

```sh
pip install numpy
pip install matplotlib
pip install folium
pip install jupyter-notebook
pip install scikit-learn
```

## Usage example

To run this all you need is a foursquare API Key which can
be found [Here](https://developer.here.com/)

## Development setup

To Setup the Notebook Install the Above Dependencies and setup your API Credentials as per HERE REST Documentation

## Release History
* 0.0.6
   * Change the Datasource for very accurate clustering

* 0.0.5
   * Change the Algorithm for very accurate clustering (Minisom)

* 0.0.4
   * Fit Data using PCA to Plot much better clusters
   
* 0.0.3
    * Added PCA for variance analysis

* 0.0.2
    * Added Popups in Folium for a better idea of locations
    
* 0.0.1
    * Basic Skeleton is Ready, Need to add for Location as per User Input

## Meta

[PerfectoZ](https://github.com/PerfectoZ) – [Email](mandeepsinghtaneja_it20b10_47@dtu.ac.in) – [LinkedIn](https://linkedin.com/in/mandeep-taneja)


## Contributing

1. [Fork it](<https://github.com/PerfectoZ/Geolocational-Data-Analysis/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some New Feature'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[python-image]: https://img.shields.io/badge/Python-3.10.x-blue?style=flat-square
[python-url]: https://npmjs.org/package/datadog-metrics
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[rest-api-image]: https://img.shields.io/badge/REST%20API-V3-orange?style=flat-square
