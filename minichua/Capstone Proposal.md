## Name: 
<!-- think of a name already -->
Minichua (placeholder for now. Japanese for miniature)

## Overview:
<!-- write this better -->
Minichua will be a searchable miniature figure database to help gamers and painters find the perfect mini on just one website. It will use Python with the BeautifulSoup library (for now) to scrape miniature maker's websites for data to create a searchable API. The website frontend will consist of HTML and CSS using (probably) the Bootstrap framework. Django and Vue will make up the backend.

## Features:
<!-- write this better -->
As a tabletop gamer and painter, I wanted to make an as-near-as-possibe exhaustive list of all miniature figures in production, because I find going to half a dozen websites to find the perfect mini to be a pain.

I want the user to be able to search for minis using descriptive tags and then be able to follow a link to the mini's manufacturer. 

To do that I'll need to:
- write code in Python to scrape sites for the mini data
- save that data to a CSV
- create an API to handle the data for each mini
- make the CSV work with an API
- create a template to create a page for each mini
- create a page to seach or filter for specific tags in the API
- create a results page that lists the filtered results and links to the mini's page
- add tags to several minis for testing


Users will also eventually be able to submit their own tags for an individual mini to be reviewed and added by an administrator.

To do that I'll need to:
- add login/logout/register/etc buttons the templates
- add user stuff
- figure out authentications
- add input field to mini page template for submiting tags
- something like a CSV with an entry for each tag submission
- create a admin view to view all tag submissions and buttons to deny or approve
- hook up those buttons to the main CSV

## Data model:
<!-- format better and clearer -->
My main data item will be something like 'Mini'. Since my data is generated by a scraping program written for a specific manufacturer's website, I will likely be storing data as a CSV for each manufacturer. 

The data I will be pulling from each manufacturer will include:
- mini's name
- description(if any)
- manufacturer
- image(s) link
- URL

The data I will then be adding for each mini is the various classes of descriptive tags such as: 
- gender
- class(mage,barbarian,thief etc)
- race(human,elf,lizardfolk)
- size(15mm,25mm,35mm etc)
- setting(fantasy,modern,sci-fi)
- weapon(sword, rapier, wand etc)
- armor/clothing
- game specific(Warhammer,D&D,Star Wars)
- prepainted(t/f)
- NSFW(t/f)
- single or pack mini(t/f)

For users, I will track the basics like username, email, and password, and the only other thing I plan on tracking initially is each user's tag submissions, mainly to track trolls.

## Schedule:
<!-- format better. also continue to work on -->
- Week 1:
    - Create web scrapers for at least two large miniature manufacturers to create CSVs with all initial data (will refer to python mini cap a lot)
- Week 2:
    - Convert CSVs to API
    - Make a Django/Vue web app to view a list of all minis with some search and filter functions (refer to js minicap a lot)
- Week 3:
    - Add a method for adding tags from a minis page
    - Get users and authentication going with ability for users to make tag submissions
- Week 4:
    - More site scrapers and more search options
    - Make a tool for easy tag submission approval and user tag tracking