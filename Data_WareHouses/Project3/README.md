<h1>Introduction</h1>
<p>A music streaming service, called Sparkify, has become more popular. This not only grew their user base, but also their song database. Because of this growth, they would like to move their processes and data onto the cloud. The data for both song details and user activity are currently stored in JSON files.</p>
<p>The data collected is now increasing and it become more difficult for Sparkify to process and analyses the data in the current JSON format. For this We proposed a Solution to use AWS Redshift Data WareHouse.</p>
<h1>Project Details</h1>
<p>For this project, We will be moving two data sources from a public S3 buckets to AWS Redshift.</p>
<h2>S3 Buckets (Data Storage):</h2>
<p>Bucket 1 contains info about songs and artists</p>
<ul>
<li>SONG_DATA='s3://udacity-dend/song_data'
Bucket 2 contains has info about actions done by users (such as what song are listening, etc..)</li>
<li>LOG_DATA='s3://udacity-dend/log_data'
<strong>Note</strong> we will need a descriptor file (also a JSON) in order to extract the data from the folders. A descriptor file is needed since we do not have a common prefix in the folders.</li>
</ul>
<h2>AWS Redshift:</h2>
<p>We will be taking the data from the S3 buckets and loading into Redshift, which is a Data Warehouse with columnar storage. Moving the data to this cloud service will help retrieve data faster and store large amounts of it.</p>
<p>To improve our data structure, we will be using a STAR schema. This schema consists of one fact table referencing any number of dimension tables, which helps the Sparkify for solving simplified common business logic.</p>
<ul>
<li><strong>Fact Table:</strong> songplays: attributes referencing to the dimension tables</li>
<li><strong>Dimension Tables:</strong> users, songs, artists and time table</li>
</ul>
<h1>ETL Process</h1>
<p>For this project, we use SQL for the ETL and python as a bridge. The transformation and data normalization is done by Query, see the sql_queries.py for more details.</p>
<h1>Steps to run process</h1>
<ol>
<li>Start up a AWS Redshift Cluster</li>
</ol>
<ul>
<li>Make sure to setup the IAM role to AmazonS3ReadOnlyAccess.</li>
<li>Use dc2.large cluster with Atleast 4 nodes. </li>
</ul>
<ol start="2">
<li>
<p>Open up a terminal session or open start_script.ipynb</p>
</li>
<li>
<p>Run '%run create_tables.py'</p>
</li>
</ol>
<ul>
<li>This will create the tables, must be run first</li>
</ul>
<li>Run 'python etl.py'</li>
</ol>
<ul>
<li>This will run the ETL process</li>
</ul>
<h1>Project Structure</h1>
<ul>
<li>create_tables.py - Script will drop old tables (if exist) ad re-create new tables</li>
<li>etl.py - Script will executes the queries that extract JSON data from the S3 bucket and ingest them to Redshift</li>
<li>sql_queries.py - File that contains variables with SQL statement in String formats, partitioned by CREATE, DROP, COPY and INSERT statements</li>
<li>dhw.cfg - Configuration file used that contains info about Redshift, IAM and S3</li>
<li>start_script.ipynb - This notebook enables us to run Create Schema for the project and run ETL Process </li>
<li>analysis_queries.ipynb - This notebook enables us to check , whether Our ETL process runned properly and user and run their analysis queries whenever required</li>
</ul>
</article>