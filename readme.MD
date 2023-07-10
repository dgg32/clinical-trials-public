

# Introduction
  

This repository contains code and data for my article "[Clinical Trials as Graphs and Vectors](https://dgg32.medium.com/learn-japanese-onomatopoeia-with-neo4j-a7306c7933ec)". 

1. The script json_exploration are for data download and formatting.

2. The data folder for_neo4j contains the TSV ready for Neo4j import.

3. The neo4j_test.hwf is an Apache Hop workflow file. It will connects to your Neo4j, copy the formatted TSV files to the Import folder and import them. For details, please refer to my article.
  

# Prerequisite

Neo4j Desktop or AuraDB

Gemini Cloud account

OpenAI account

Apache Hop

Qdrant free tier
  

# Run
1. Download the clinical research data from clinicaltrials.gov in JSON. Run json_exploration.ipynb to format the data. The data ctg-studies(5).json is also included.
  
2. Create an empty Neo4j database in Neo4j Desktop. Run Apache Hop and set up the workflow. Import the data.

3. Import the data into Aura/Gemini Cloud via dump or TSV files.



## Authors

  

*  **Sixing Huang** - *Concept and Coding*

  

## License

  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
