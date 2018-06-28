# Twitter Streaming

Display tweets with Basemap and Tweepy

Dependencies :

Install the Below Dependencies to run the Job.

conda install -c conda-forge tweepy

conda install matplotlib numpy pandas shapely scipy pysal Fiona descartes basemap

Authentication File has to be in the Same Folder where the Python Files reside.

The Job is Classified into two Parts :



- To Download the Data From twitter :

Use the below script to download the data from twitter :

python3 twitter_stream.py



- To Plot the Data on BaseMap :

Use the below script to plot the data on BaseMap. Please run the Below script in iPython or Jupyter Notebook for Visualization.

python3 twitter_basemap.py
