# CSCI 1951a Data Science Final Project: Avocados and Millenials

This projects seeks to explore the trends in avocado consumption in the US,
in connection with millenials, a group classified as those born between
1980 and 1994.

## Hypothesis

We expect that cities in the United States with a higher population of millenials,
especially those with a high population of millenials with above-average
income, consume more avocados despite prices increases in recent years.

## Directory Structure

### Data

This directory contains our cleaned data, in csv files and sqlite databases. This
includes demographic data (ie. population, age, gender) and avocado consumption data.

The main database file used for analysis is avocado_project.db. This database
file contains four tables:

1. demographic - this contains the accumulated populations for 2016, 2017, and
2018 for each region, by age and sex. That is, for one row of the table, this gives
the total number (in 2016, 2017, and 2018) of people of that age and that gender
for the specific region.

2. hab2016 - this contains the accumulated avocado consumption statistics for
each region in 2016.

3. hab2017 - this contains the accumulated avocado consumption statistics for
each region in 2017.

4. hab2018 - this contains the accumulated avocado consumption statistics for
each region in 2018.

5. joined_data - this is the joined dataset that merges demographic and avocado data, by year and region; we used this for our analysis

### Data Spec

This directory contains screenshots of our data sample, as well as a more detailed
data spec explaining the origins of our data, methods of data cleaning, as well as
other information laying the foundation of our analysis.

### Cleaning

This directory contains the python files used to combine our datasets so that
analysis and statistical tests can be performed.

### Analysis

This directory contains the python files used to perform the analysis of our data.

## Environment & Dependencies
* sqlite database (instructions on Data Science course site)
* Jupyter notebook for analysis
    * Intall Jupyter here: https://jupyter.org/install
    * Tutorial: https://www.dataquest.io/blog/jupyter-notebook-tutorial/
* GitHub commands
    * After making change that you made on your local computer and want everyone else to see
        * git add -A
        * git commit -m “description of what changes you made”
        * git push

    * If someone else makes changes that you want on your local computer
        * git pull
    * If someone else makes a change that you need, but you have local changes
        * git stash
        * git pull
        * git stash pop
    * More detailed tutorial: https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6



