# isMyWebsiteMobileFriendly

Python script that, given an XML sitemap, checks if all the pages are mobile friendly.


In order to run this script you need to: 

1. Install the client library
```
$ pip install --upgrade google-api-python-client
```

2. Create a project in the Google API Console and create an API key. Replace {YOUR_KEY} in the scipt by the key you just created.

3. Generate a .xml sitemap of your website that you save as *sitemap.xml* in the same folder as the scipt file.

The results of the script are saved in a file called *site.csv*
