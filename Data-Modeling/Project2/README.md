<div class="Box-body p-5">
        <article class="markdown-body entry-content" itemprop="text"><p><b>Project: Data Modeling with Cassandra</b></p>
<p><b>Introduction:</b></p>
<p>Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. It is very difficult to query the data to generate the results, since the data stored in directory of CSV files on user activity on the app. My role is to create an Apache Cassandra database to make queries and analysis easy.</p>
<p><b>Project Overview:</b></p>
<p>In this project, I would be applying Data Modeling with Apache Cassandra and complete an ETL pipeline using Python. I am provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.</p>
<p><b>Provided Datasets:</b></p>
<p>For this project, I'll be working with one dataset: event_data. This is directory of CSV files partitioned by date. Here are structure of directory of two files in the dataset:
event_data/2018-11-08-events.csv
event_data/2018-11-09-events.csv</p>
<p><b>Project Template:</b></p>
<p>This project template includes one Jupyter Notebook file, in which:
•	We will create an intermediate denormalized dataset  in event_datafile_new.csv file.
•	We will create tables according to the queries that will be performed on them.
•	We will load the data into tables we create in Apache Cassandra and run queries for analysis</p>
<p><b>Project Steps:</b></p>
<p>Below are steps We can follow to complete each component of this project.</p>
<p><b>Modelling Apache Cassandra Database:</b></p>
<ol>
<li>We have to Design tables to answer the queries outlined in the project template</li>
<li>Write Apache Cassandra CREATE KEYSPACE and SET KEYSPACE statements</li>
<li>We have to Develop  CREATE statement for each of the tables to address each question</li>
<li>Load the data with INSERT statement for each of the tables</li>
<li>Test by running the proper select statements with the correct WHERE clause</li>
</ol>
<p><b>Build ETL Pipeline:</b></p>
<ol>
<li>Implement the logic in the notebook template to iterate through each event file in event_data to process and create a new CSV file in Python</li>
<li>Include Apache Cassandra CREATE and INSERT three statements to load processed records into relevant tables in our data model</li>
<li>Test by running three SELECT statements after running the queries on your database</li>
<li>Finally, drop the tables and shutdown the cluster</li>
</ol>
<p><b>Files:</b></p>
<p><b>Event_datafile_new.csv:</b> This is the final combination of all the files which are in the folder event_data</p>
<p><b>Event_Data Folder:</b> Each event file is present separately, so all the files would be combined into one into event_datafile_new.csv</p>
<p><b>Project_1B_Project_Template.ipynb:</b> This was template file provided to fill in the details and write the python script</p>
<p><b>Project_1B.ipynb:</b> This is the final file provided in which all the queries have been written with importing the files, generating a new csv file and loading all csv files into one. All verifying the results whether all tables had been loaded accordingly as per requirement</p>

</article>
      </div>