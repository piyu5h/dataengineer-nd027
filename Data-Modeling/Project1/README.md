<article class="markdown-body entry-content" itemprop="text"><p><b>Introduction</b></p>
<p>A startup called <b>Sparkify</b> want to analyze the data they have been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to.</p>
<p>The aim is to create a Postgres Database Schema and ETL pipeline to optimize queries for song play analysis.</p>
<p><b>Project Description </b></p>
<p>In this project, We have to model data with Postgres and build and ETL pipeline using Python to perform optimized queries on song play analysis. On the database side, We have to define fact and dimension tables to use  Star Schema and ETL pipeline should be created to transfer data from files located in two local directories into these tables in Postgres using Python and SQL</p>
<p><b>Schema for Song Play Analysis</b></p>
<p><b>Fact Table</b></p>
<p><b> SongPlay </b> stores the log data associated with song plays</p>
<p><b>Dimension Tables</b></p>
<p><b> User </b> in the application</p>
<p><b> Song </b> in music database</p>
<p><b> Artist </b> in music database</p>
<p><b> Time: </b> timestamps of records in songplays broken down into specific units</p>
<p><b>Project Design</b></p>
<p>Database Design is very beneficial for analytic queries, we can get the most information by joining tables and extract required information.</p>
<p>ETL Design is simplified just have to read json files and parse using pandas and to store the tables into specific columns with proper validation</p>
<p><b>Database Script</b></p>
<p>Writing "python create_tables.py" command in terminal, it is easier to create and recreate tables on each run</p>
<p><b>Jupyter Notebook</b></p>
<p>etl.ipynb, a Jupyter notebook is given for verifying each command and data as well and then using those statements and copying into etl.py and running it into terminal using "python etl.py" and then running test.ipynb to see whether data has been loaded in all the tables</p>
<p><b>Relevant Files Provided </b></p>
<p><b>test.ipnb </b>displays the first few rows of each table to let you check your database</p>
<p><b>create_tables.py </b>Create new database on every run , It will drop and create tables on every run</p>
<p><b>etl.ipynb </b>read and processes a single file from song_data and log_data and loads into your tables in Jupyter notebook</p>
<p><b>etl.ipynb </b>read and processes a single file from song_data and log_data and loads into your tables in ET</p>
<p><b>sql_queries.py </b>containg all sql queries that will be used in this project</p>
</article>