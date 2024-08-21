# Mousepedia

![Welcome to Mousepedia](documentation/images/welcome-to-mousepedia.png)

### All things Disney...

![Responsive Screenshot]()

Mousepedia was created for my 3rd Milestone project for Code Institute's Level 5 Diploma in Web Application Development.

Link to deployed site - []()

## CONTENTS

- [Mousepedia](#mousepedia)
  - [CONTENTS](#contents)
  - [Site Objectives](#site-objectives)
- [User Experience/UX](#user-experienceux)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
    - [New Visitor Goals](#new-visitor-goals)
    - [Existing Visitor Goals](#existing-visitor-goals)
- [Design Choices](#design-choices)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Logo and Favicon](#logo-and-favicon)
  - [Wireframes](#wireframes)
  - [Flow Diagram](#flow-diagram)
  - [Database Plan](#database-plan)
- [Features](#features)
  - [Registration](#registration)
  - [Future Features](#future-features)
  - [Features Not Included](#features-not-included)
- [Technologies Used](#technologies-used)
- [Programming Languages, Frameworks and Libraries Used](#programming-languages-frameworks-and-libraries-used)
- [Agile](#agile)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [User](#user)
  - [Bugs](#bugs)
  - [Lighthouse](#lighthouse)
  - [Validation Testing](#validation-testing)
    - [HTML \& CSS](#html--css)
  - [Python Testing](#python-testing)
  - [Deployment](#deployment)
    - [Github Deployment](#github-deployment)
    - [Creating a Fork or Copying](#creating-a-fork-or-copying)
    - [Clone](#clone)
    - [Repository deployment via Heroku](#repository-deployment-via-heroku)
    - [Deployment of the app](#deployment-of-the-app)
  - [Credits](#credits)
  - [Media](#media)
  - [Acknowledgments and Thanks](#acknowledgments-and-thanks)

___

## Site Objectives

Design and create a database that holds records for detailing Disney Theme Parks, rides and restaurants, and displays these records on the frontend.

- ### Create a clear, readable and intuitive front end display

  I wanted the point of the website to be easily understood from the home page and for the user to be able to easily navigate the website where they can add, edit and delete the records that they have entered onto the database.

- ### Make use of available backend functionality

  The use of the backend framework allows users to create, edit and delete records of their choosing.

- ### Store data on an external cloud database

  I used Code Institute's Postgres database server to store the PostgreSQL database for this project.

___

# User Experience/UX

## Target Audience

- The target audience for Mousepedia is Disney fans who are planning a trip to the Disney parks in Florida, or if they purely want to collect and organise information about the Disney parks.

## User Stories

### New Visitor Goals

<h4>As a first time user, I want to be able to:</h4>
- Understand the concept of the website and how to use it.
- Create an account.

### Returning Visitor Goals

<h4>As a returning user, I want to be able to:</h4>
- Login to my account.
- To create, edit and delete records.
- Find the existing Disney park information easily.
- See which rides and restaurants are in each park.

___

# Design Choices

## Colour Scheme

The colour scheme used for this project was based on the colors from the Disney Parks website, but in conjunction with the choice provided by the Materialize framework. This provides the user with some familiarity whilst providing enough contrast between the website elements and text.

For the background of all pages, I created a gradient using the below:


## Typography

For the main logo featured on the navbar, I used the google font 'Graduate' and for the body of the page, I used Englebert.

## Logo and Favicon



## Wireframes


## Flow Diagram

Here is a diagram showing the possible flow through the site.

![Site Flow Diagram]()

## Database Plan

The database plan is fairly simple, but it shows the information that is stored within the database, the type of data and if it is logged as a Primary or Foreign key where applicable.

![Database plan]()

# Features


## Future Features

- 
- 

## Features Not Included

- 

___

# Technologies Used

Here are the technologies used to build this project:

- [Gitpod](https://www.gitpod.io/) To build and create this project
- [Github](https://github.com) To host and store the data for the site.
- [PEP8 Validator](https://pep8ci.herokuapp.com/) Used to check python code for errors
- []() Used to store PostgreSQL database.
- [Heroku](https://id.heroku.com/) Used to deploy the project

# Programming Languages, Frameworks and Libraries Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


# Testing

<!-- As each section or Function/Model was built during this project, I was testing for functionality and styling issues that may have arisen (see table below), which were corrected or fixed before continuing. I also had friends test the site by signing up, adding and deleting comments using various devices on varying platforms (IOS, Android, Mobile, Tablet etc) and reporting back any issues they encountered with functionality or styling. -->

## Manual Testing


## Bugs



## Lighthouse


## Validation Testing

### HTML & CSS



## Python Testing

<!-- Python pep8 validation was done via [Code Institute's Python Linter](https://pep8ci.herokuapp.com/)

The only errors recieved here were where some lines of text exceeded the limit of 79 characters, but these have now been rectified.

Python Files Tested:

- models
- forms
- views
- urls -->

___

## Deployment

### Github Deployment

<!-- The website was stored using GitHub for storage of data and version control. To do this I did the following;

After each addition, change or removal of code, in the terminal within your IDE (I used codeanywhere for this project) type:

- git add .
- git commit -m "meaningful commit message"
- git push

The files are now available to view within your github repository. -->

### Creating a Fork or Copying

To clone/fork/copy the repository you click on the fork tab which is situated next to unwatch tab in the top right corner of the page

### Clone

To create a clone you do the following;

1. Click on the code tab, left of the Gitpod tab
2. To the right of the repository name, click the clipboard icon
3. In the IED open GitBash
4. Change the working directory to the location you prefer
5. Add Git Clone with the copy of the repository name
6. Clone has been created

### Repository deployment via Heroku

- On the [Heroku Dashboard](https://dashboard.heroku.com) page, click New and then select Create New App from the drop-down menu.
- When the next page loads insert the App name and Choose a region. Then click 'Create app'
- In the settings tab click on Reveal Config Vars and add the key Port and the value 8000. The credentials for this app were:

1. Cloudinary URL
2. Postgres Database URL
3. Port (8000)

- Below this click Add buildpack and choose python and nodejs in that order.

### Deployment of the app

- Click on the Deploy tab and select Github-Connect to Github.
- Enter the repository name and click Search.
- Choose the repository that holds the correct files and click Connect.
- A choice is offered between manual or automatic deployment whereby the app is updated when changes are pushed to GitHub.
- Once the deployment method has been chosen the app will be built and can be launched by clicking the Open app button which should appear below the build information window, alternatively, there is another button located in the top right of the page.

___

## Credits

This project was created using the Code Institute walkthrough taskmanager project. From this base I customised the layout and styling with Materialize and custom CSS. 




<!-- Once complete, the readme file was passed through a spelling and grammar check via [Grammarly](https://www.grammarly.com/) -->

___

## Media

All other content and images are my own.

___

## Acknowledgments and Thanks


