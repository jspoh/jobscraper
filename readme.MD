# Jobscraper

Hello, thanks for using jobscraper!

This program takes the front page results from top job searching websites such as:
- sg.indeed.com 
- jobstreet.com.sg 
- sg.jobsdb.com 
- sg.linkedin.com 
- jobscentral.com.sg 

and displays information such as: 
- Job title 
- Salary 
- Location 
- Job type 
- Date posted 
- Link to the original job post so that you may apply 

so that you don't have to navigate through different websites for the results. Of course, some
employers may not have posted certain information such as salary, location or job type so some
information fields may be unavailable.

Some webpages are also dynamic javascript built which may complicate things as the program only
captures the html document on load. Javascript elements which are loaded in after that will not be
registered. This may cause problems such as missing information fields.
However, restarting the program may work but the more reliable option would be to simply
search for the job title in the job portal or by visiting the link provided.

jobscraper_v2.py writes all information gathered onto a .txt document for easy reference. Here's a screenshot of the output

<img src='lib/result.PNG' alt="Image of jobscraper_v2.py's output in a .txt file">
