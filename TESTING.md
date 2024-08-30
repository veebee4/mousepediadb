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
| Understand the concept of the website and how to use it | A description of what the site is used for is present on the home page, the nav bar is intuitive and clear making it self explanatory | [Site Description](documentation/testing/site-description.png) |
| View existing records, if any are available | Some records have been entered by myself. The user can view these straight away on the home page, clicking on the image will direct them straight to the parks page, or it can be selected on the nav bar from any page. To view the ride and restaurant records the user can navigate using the top menu. A message will appear saying "No park/ride/restaurant records found" if no records are available | [Park Records Home Page](documentation/testing/park-record-home.png) [Nav Links](documentation/images/interactive-nav-links.png) [No Records Found](documentation/images/no-record-feedback.png) |
| Add records if they do not already exist | There is a clear and easy to read button at the top of the page saying "Add a park/ride/restaurant to your collection" | [Add Buttons](documentation/testing/add-buttons.png) |

### Returning Visitor

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
|`Returning Visitors`|
|  |  |  |
| Find existing Disney Park information easily | The user can navigate to the appropriate page; The park records are revealed and replace the park picture when the user clicks on the park card, Ride & Restaurant information can be found by clicking through the tabs on the cards | [Card Reveal](documentation/testing/card-reveal.png) [Tabs Ride Card](/documentation/testing/tabs-ride-card.png) |
| See which rides and restaurants are in each park | The tabs on the cards are clearly marked with appropriate titles, "Park" is the first one so the park that the record is allocated to will be the first piece of information displayed | See above |
| Edit existing records | When a user views the records on the Parks, Rides or Restaurants pages, the card displaying the record has a clearly marked edit button underneath all the information, pressing this button directs the user to a pre-populated form containing the existing information | See above image for Edit button on Ride record [Edit Park Button](/documentation/testing/edit-park.png) [Edit Restaurant Button](/documentation/testing/edit-rest.png) |
| Delete existing records | When a user views the records on the Parks, Rides or Restaurants pages, the card displaying the record has a clearly marked delete button underneath all the information, pressing this button will trigger a modal to confirm if they would like to delete the record and to let the user know that the action cannot be undone. The user is also informed when deleting a park only, that this will delete all ride/restaurant records associated with that park | Above images show delete button also |

---

### Full Testing

#### Home page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Graphic & Text Logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Carousel Clickable | Takes user to parks page | Clicked on each image of each park record | Park page is loaded | Pass |
| Footer links | Each link opens into a new tab | Click each link | Each website loads in a new tab | Pass |

#### Parks Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Graphic & Text Logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Footer links | Each link opens into a new tab | Click each link | Each website loads in a new tab | Pass |
| Add Park Button | Button loads new page with a form to enter park information | Clicked button | Button directs to add park page with form | Pass |
| Card Reveal Hint | Hint saying "Click Me!" Appears to encourage user to click to view park information | Hovered over card | A styled tooltip appears saying "Click Me!" | Pass |
| Park Card Information Reveal | When card is clicked on, the park information is revealed | Clicked on each card | The card reveal replaces the front image with all the park information added on the add park form | Pass |
| Park Card Reveal Close | On card reveal side, an 'X' appears in the top right corner to be able to close the information and return to the front of the card | Clicked on each card | The card reveal closes to reveal the front image again | Pass |
| Edit Button | Button loads new page with a form to edit park information | Clicked button | Button directs to edit park page with form | Pass |
| Delete Button | Button triggers a modal to ask user for confirmation to delete | Clicked button | Modal pops up in centre of the screen asking user "Are you sure you want to delete this park? This will also delete any associated ride/restaurant records! This action cannot be undone, all information will be lost!" with delete and cancel buttons | Pass |
| Delete Button on Modal | Button delete's park record and associated ride/restaurant records | Clicked button | Park record and any ride/restaurant records assigned to that park are also deleted. Shows user a flash message that confirms these records have been deleted | Pass |
| Cancel Button on Modal | Button closes modal and returns to park page | Clicked button | Modal disappears and user is back to park page | Pass |

#### Add A Park Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Graphic & Text Logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Footer links | Each link opens into a new tab | Click each link | Each website loads in a new tab | Pass |
| Text Inputs | Field not allowed to be left empty or with whitespace added | Enter five spaces | Form accepts whitespaces as long as it meet the minimum character allowance and adds the record | Fail |
| Date & Time Pickers | Clicking on line of input triggers the date/time picker | Clicked on line | Date/Time picker opens | Pass |
| Number Inputs | Inputting a negative number shows an error message | Entered -1 on form | Error appears stating "Value must be greater than or equal to 0" | Pass |
| Add Park Submit Button | Changes colour when hovered over | Hovered on button | Colour changes to lighter blue | Pass |
| Add Park Submit Button | Submits valid entered information on form, adds to database and takes user to parks page | Entered all form information and clicked on Add Park button | User taken to parks page where the record is added and displayed on a card | Pass |

#### Edit A Park Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Graphic & Text Logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Footer links | Each link opens into a new tab | Click each link | Each website loads in a new tab | Pass |
| Pre-populated fields | All fields pre-populated with existing information | Clicked edit on park record, form loads | All fields in form are pre-populated except for the entertainment field | Fail |
| Text Inputs | Field not allowed to be left empty or with whitespace added | Enter five spaces | Form accepts whitespaces as long as it meet the minimum character allowance and updates record | Fail |
| Date & Time Pickers | Clicking on line of input triggers the date/time picker | Clicked on line | Date/Time picker opens | Pass |
| Number Inputs | Inputting a negative number shows an error message | Entered -1 on form | Error appears stating "Value must be greater than or equal to 0" | Pass |
| Submit Edit Button | Changes colour when hovered over | Hovered on button | Colour changes to lighter blue | Pass |
| Submit Edit Button | Submits valid entered information on form, updates database and takes user to parks page | Checked all form information and edited each input, and clicked on Submit Edit button | User taken to parks page where the record is updated and new information visible on park card | Pass |

#### Ride Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Graphic & Text Logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Footer links | Each link opens into a new tab | Click each link | Each website loads in a new tab | Pass |
| Add Ride Button | Button loads new page with a form to enter ride information | Clicked button | Button directs to add ride page with form | Pass |
| Card Tabs | Each tab displays appropriate information when clicked on | Clicked each tab | Correct information shown below tabs | Pass |
| Edit Button | Button loads new page with a form to edit ride information | Clicked button | Button directs to edit ride page with form | Pass |
| Delete Button | Button triggers a modal to ask user for confirmation to delete | Clicked button | Modal pops up in centre of the screen asking user "Are you sure you want to delete this ride? This action cannot be undone, all information will be lost!" with delete and cancel button | Pass |
| Delete Button on Modal | Button delete's ride record | Clicked button | Ride record deleted. Shows user a flash message that confirms the record has been deleted | Pass |
| Cancel Button on Modal | Button closes modal and returns to ride page | Clicked button | Modal disappears and user is back to ride page | Pass |

#### Add A Ride Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Graphic & Text Logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Footer links | Each link opens into a new tab | Click each link | Each website loads in a new tab | Pass |
| Park dropdown list | Displays all added park records in a drop down list | Clicked on dropdown | List of existing park records shown | Pass |
| Text Inputs | Field not allowed to be left empty or with whitespace added | Enter five spaces | Form accepts whitespaces (except on Ride location input) as long as it meet the minimum character allowance and adds record | Fail |
| Add Ride Button | Changes colour when hovered over | Hovered on button | Colour changes to lighter blue | Pass |
| Add Ride Button | Submits valid entered information on form, adds record to database and takes user to ride page | Added all form information and clicked on Add Ride button | User taken to ride page where the record is added and displayed on a card | Pass |

#### Edit A Ride Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Graphic & Text Logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Footer links | Each link opens into a new tab | Click each link | Each website loads in a new tab | Pass |
| Pre-populated fields | All fields pre-populated with existing information | Clicked edit on ride record, form loads | All fields in form are pre-populated except for the description field | Fail |
| Text Inputs | Field not allowed to be left empty or with whitespace added | Enter five spaces | Form accepts whitespaces as long as it meet the minimum character allowance and updates record | Fail |
| Submit Edit Button | Changes colour when hovered over | Hovered on button | Colour changes to lighter blue | Pass |
| Submit Edit Button | Submits valid entered information on form, updates database and takes user to ride page | Checked all form information and edited each input, and clicked on Submit Edit button | User taken to ride page where the record is updated and new information visible on ride card | Pass |

#### Restaurant Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Graphic & Text Logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Footer links | Each link opens into a new tab | Click each link | Each website loads in a new tab | Pass |
| Add Restaurant Button | Button loads new page with a form to enter restaurant information | Clicked button | Button directs to add restaurant page with form | Pass |
| Card Tabs | Each tab displays appropriate information when clicked on | Clicked each tab | Correct information shown below tabs | Pass |
| Edit Button | Button loads new page with a form to edit restaurant information | Clicked button | Button directs to edit restaurant page with form | Pass |
| Delete Button | Button triggers a modal to ask user for confirmation to delete | Clicked button | Modal pops up in centre of the screen asking user "Are you sure you want to delete this restaurant? This action cannot be undone, all information will be lost!" with delete and cancel button | Pass |
| Delete Button on Modal | Button delete's restaurant record | Clicked button | Restaurant record deleted. Shows user a flash message that confirms the record has been deleted | Pass |
| Cancel Button on Modal | Button closes modal and returns to restaurant page | Clicked button | Modal disappears and user is back to restaurant page | Pass |

#### Add A Restaurant Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Graphic & Text Logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Footer links | Each link opens into a new tab | Click each link | Each website loads in a new tab | Pass |
| Park dropdown list | Displays all added park records in a drop down list | Clicked on dropdown | List of existing park records shown | Pass |
| Text Inputs | Field not allowed to be left empty or with whitespace added | Enter five spaces | Form accepts whitespaces (except on Restaurant name and location input) as long as it meet the minimum character allowance and adds record | Fail |
| Checkbox Inputs | Not ticking a box shows an error | Leave checkboxes blank | Form adds record | Fail |
| Add Restaurant Button | Changes colour when hovered over | Hovered on button | Colour changes to lighter blue | Pass |
| Add Restaurant Button | Submits valid entered information on form, adds record to database and takes user to restaurant page | Added all form information and clicked on Add Restaurant button | User taken to restaurant page where the record is added and displayed on a card | Pass |

#### Edit A Restaurant Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Site Graphic & Text Logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Footer links | Each link opens into a new tab | Click each link | Each website loads in a new tab | Pass |
| Pre-populated fields | All fields pre-populated with existing information | Clicked edit on restaurant record, form loads | All fields in form are pre-populated except for the description, dine in/quick service checkboxes and food type fields | Fail |
| Text Inputs | Field not allowed to be left empty or with whitespace added | Enter five spaces | Form accepts whitespaces as long as it meet the minimum character allowance and updates record | Fail |
| Submit Edit Button | Changes colour when hovered over | Hovered on button | Colour changes to lighter blue | Pass |
| Submit Edit Button | Submits valid entered information on form, updates database and takes user to restaurant page | Checked all form information and edited each input, and clicked on Submit Edit button | User taken to restaurant page where the record is updated and new information visible on restaurant card | Pass |

#### 404 Error Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| 404 Error Page | Loads if a user tries to go to a page that does not exist | Typed an incorrect page at the end of the website address | 404 page loads | Pass |
| Site Graphic & Text Logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Navigation Links | Links direct user to appropriate page | Clicked each link | Each link takes user to correct page | Pass |
| Footer links | Each link opens into a new tab | Click each link | Each website loads in a new tab | Pass |

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