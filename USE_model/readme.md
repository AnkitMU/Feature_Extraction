# Feature Extraction from UML Class Diagrams

## Overview
This project is designed to extract features such as classes, attributes, operations, and associations from UML class diagrams represented in XMI format. The extracted data is then converted into a format compatible with the USE tool for further model analysis.

## Features
- Extracts classes and their attributes (with data types)
- Extracts operations (methods) within classes
- Extracts associations between classes and their multiplicities
- Outputs the extracted data in a USE tool-compatible format

## Prerequisites
- Python 3.x
- An XML file (`model.xmi`) containing the UML class diagram in XMI format

## Installation
Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/AnkitMU/Feature_Extraction.git
cd Feature_Extraction
