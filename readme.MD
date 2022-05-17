# Jobscraper

Hello, thanks for using jobscraper!

This program takes the front page results from top job searching websites such as:
- sg.indeed.com
- jobstreet.com.sg
- sg.jobsdb.com
- sg.linkedin.com
- jobscentral.com.sg

so that you don't have to navigate through different websites for the results.

Some webpages are dynamic javascript built which may complicate things as the program only captures the html document
on load. Javascript elements which are loaded in after that will not be registered. This may cause problems such as 
'Company name unavailable' or 'Link unavailable'. However, restarting the program may work sometimes but the more 
reliable option would be to simply search for the job title in the job portal. Other unavailable information might 
be available on the link provided.

jobscraper_v2.py writes all information gathered onto a .txt document for easy reference. Here's a screenshot of the output

<img src='lib/main.PNG' alt="Image of jobscraper_v2.py's output in a .txt file">
