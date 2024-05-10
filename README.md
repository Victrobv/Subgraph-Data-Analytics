# Subgraph-Data-Analytics
This project demonstrates how to utilize the subgrounds package to retrieve blockchain data from a Subgraph API and perform basic data analysis.

# Features

* Simplified workflow for querying Subgraph data with subgrounds.
* Example code snippets showcasing the process.
* Data visualization using pandas and matplotlib.

## Installation
This project requires the following Python packages:

* ```subgrounds```
* ```pandas```
* ```matplotlib```

You can install them using pip:

```
pip install subgrounds pandas matplotlib
```

## Usage
The provided code demonstrates the following steps:

* Import Libraries: Import necessary librarie
* Open Subgrounds Object: Create a ```Subgrounds``` object to interact with the Subgraph API.
* Load Subgraph: Specify the URL of the desired Subgraph to load its schema.
* Use Synthetic Fields: Create a ```SyntheticField``` to transform pre-queried data.
* Write Subgraph Query: Construct your query using Subgrounds Object syntax to retrieve specific data.
* Execute Query: Run the query against the Subgraph and obtain the results.
* Data Analysis and Visualization (Optional): Process and visualize the retrieved data using ```pandas``` and ```matplotlib```.
* Example notebooks are provided to illustrate each step.

## Disclaimer
This project is for educational purposes only and is not intended for commercial use.  No license is applied to the code.