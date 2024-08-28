# Mousepedia - Testing

![Mousepedia shown on a variety of screen sizes]()

Visit the deployed website: [Mousepedia](https://mousepediadb-0e4030391623.herokuapp.com/)

# CONTENTS

* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
    * [First Time Visitor](#first-time-visitor)
    * [Returning Visitor](#returning-visitor)
  * [Full Testing](#full-testing)
    * [Home Page](#home-page)
    * [Parks](#parks)
    * [Rides](#rides)
    * [Restaurants](#restaurants)
    * [Add Park](#add-park)
    * [Add Ride](#add-ride)
    * [Add Restaurant](#add-restaurant)
    * [Edit Park](#edit-park)
    * [Edit Ride](#edit-ride)
    * [Edit Restaurant](#edit-restaurant)
* [AUTOMATED TESTING](#automated-testing)
    * [W3C Validator](#w3c-validator)
    * [JavaScript Validator](#javascript-validator)
    * [Chrome DevTools Audit Report](#chrome-devtools-audit-report)
* [BUGS](#bugs)
    * [Solved Bugs](#solved-bugs)
    * [Known Bugs](#no-bugs)


<!-- As each section or Function/Model was built during this project, I was testing for functionality and styling issues that may have arisen (see table below), which were corrected or fixed before continuing. I also had friends test the site by signing up, adding and deleting comments using various devices on varying platforms (IOS, Android, Mobile, Tablet etc) and reporting back any issues they encountered with functionality or styling.   I carried out testing throughout the project, by using Chrome developer tools I was able to troubleshoot as the project was being built.
  All pages have been viewed in the Chrome developer tools to ensure each page is responsive on different device and screen sizes. -->

## Manual Testing

### Testing User Stories

### New Visitor

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| `First Time Visitors` |
|  |  |  |
| Understand the concept of the website and how to use it | A description of what the site is used for is present on the home page, the nav bar is intuitive and clear making it self explanatory | :--- |
| View existing records, if any are available | Some records have been entered by myself. The user can view these straight away on the home page, clicking on the image will direct them straight to the parks page, or it can be selected on the nav bar from any page. To view the ride and restaurant records the user can navigate using the top menu. A message will appear saying "No park/ride/restaurant records found" if no records are available | :--- |
| Add records if they do not already exist | There is a clear and easy to read button at the top of the page saying "Add a park/ride/restaurant to your collection" | :--- |

### Returning Visitor

|`Returning Visitors`|
|  |  |  |
| Find existing Disney Park information easily | The user can navigate to the appropriate page; The park records are revealed and replace the park picture when the user clicks on the park card, Ride & Restaurant information can be found by clicking through the tabs on the cards | :--- |
| See which rides and restaurants are in each park | The tabs on the cards are clearly marked with appropriate titles, "Park" is the first one so the park that the record is allocated to will be the first piece of information displayed | :--- |
| Edit existing records | When a user views the records on the Parks, Rides or Restaurants pages, the card displaying the record has a clearly marked edit button underneath all the information, pressing this button directs the user to a pre-populated form containing the existing information | :--- |
| Delete existing records | When a user views the records on the Parks, Rides or Restaurants pages, the card displaying the record has a clearly marked delete button underneath all the information, pressing this button will trigger a modal to confirm if they would like to delete the record and to let the user know that the action cannot be undone. The user is also informed when deleting a park only, that this will delete all ride/restaurant records associated with that park | :--- |

---

### Full Testing

#### Home page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Mini Logo's | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Book In Button | Takes user to booking in page | Clicked on booking in button | Booking in page is loaded | Pass |
| Book In Button Hover Effect | Button turns to a darker shade of teal when user hovers over it | Hover over booking in button | Button shows correct colour when hovering over it | Pass |
| Laser By Stephania Logo/Button | Opens Laser by Stephania booking page in a new tab | Clicked on logo/button | A new tab opens and loads the correct page | Pass |
| Social Media Icons | Opens a new tab to each social media account for the studio | Clicked on each icon | A new tab opens and loads the correct pages | Pass |

#### Ride Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Mini Logo's | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Book In Button | Takes user to booking in page | Clicked on booking in button | Booking in page is loaded | Pass |
| Book In Button Hover Effect | Button turns to a darker shade of teal when user hovers over it | Hover over booking in button | Button shows correct colour when hovering over it | Pass |
| Laser By Stephania Logo/Button | Opens Laser by Stephania booking page in a new tab | Clicked on logo/button | A new tab opens and loads the correct page | Pass |
| Social Media Icons | Opens a new tab to each social media account for the studio | Clicked on each icon | A new tab opens and loads the correct pages | Pass |

#### Restaurant Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Mini Logo's | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Book In Button | Takes user to booking in page | Clicked on booking in button | Booking in page is loaded | Pass |
| Book In Button Hover Effect | Button turns to a darker shade of teal when user hovers over it | Hover over booking in button | Button shows correct colour when hovering over it | Pass |
| Laser By Stephania Logo/Button | Opens Laser by Stephania booking page in a new tab | Clicked on logo/button | A new tab opens and loads the correct page | Pass |
| Social Media Icons | Opens a new tab to each social media account for the studio | Clicked on each icon | A new tab opens and loads the correct pages | Pass |


## Validation Testing

### HTML & CSS
[W3C](https://validator.w3.org/) was used to validate all HTML & CSS code.

* home.html - Passed - [Result]()
* parks.html - Passed - [Result]()
* rides.html - Passed - [Result]()
* restaurants.html - Passed - [Result]()
* add_park.html - Passed - [Result]()
* add_ride.html - Passed - [Result]()
* add_restaurant.html - Passed - [Result]()
* edit_park.html - Passed - [Result]()
* edit_ride.html - Passed - [Result]()
* edit_restaurant.html - Passed - [Result]()
* style.css - Passed - [Result]()  

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the Javascript within the project - Passed with no warnings/errors.
![JavaScript Validator Results]()

## Python Testing

<!-- Python pep8 validation was done via [Code Institute's Python Linter](https://pep8ci.herokuapp.com/)

The only errors recieved here were where some lines of text exceeded the limit of 79 characters, but these have now been rectified.

Python Files Tested:

- models
- forms
- views
- urls -->

## Lighthouse
  The Google Page-speed Services/Lighthouse was used to assess the accessibiity of the project to ensure the site met expected accessible standards on desktop and mobile. From this result, I can see that the performance on my website could be better and this could be improved upon on future releases - the project scored highly in all other areas.

  ![Lighthouse Result]()

- #### Browser Testing

  - The Website has been tested on Google Chrome, Safari, and Microsoft Edge.
  - The website was tested on my iPhone 14 mobile and 27" Microsoft PC devices. All other responsive testing was completed online.
  - Testing has been completed to ensure that all pages were linking correctly and external links opened in a new tab.

## Bugs

### Solved Bugs

### Known Bugs