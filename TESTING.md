# Wimpleton House Booking Application
  Back to [README](https://github.com/hysinh/wimpleton-booking-app/blob/main/README.md)

## Testing Overview
## CONTENTS  
  
* [Testing](#testing)
  * [Manual Testing](#manual-testing)
  * [Bugs and Fixes](#bugs-and-fixes)
  * [Unfixed Bugs](#unfixed-bugs)

  
---   

## User Story Testing

## Testing
### Validator Testing
This application was developed with HTML, CSS, Javascript, and Python using the Django Web Framework.
  - #### HTML Validation
    The [W3C HTML validator](https://validator.w3.org/) was used for the HTML validation. I copied the page source of the fully rendered page into the validator for testing.
    #### Public Pages
    <details >
    <summary>Home page (base.html and index.html)</summary>  

    ![Hpme page](documentation/testing/html/screenshot_html_validation_indexpage.png)
    </details>
    <details >
    <summary>Venue Hire page (venue_hire.html)</summary>  

    ![Venue Hire page](documentation/testing/html/screenshot_html_validation_venuehirepage.png)
    </details>
    <details>
    <summary>About page (about.html)</summary>  

    ![About page](documentation/testing/html/screenshot_html_validation_aboutpage.png)
    </details>
    <details>
    <summary>Contact page (contact.html)</summary>  

    ![Contact page](documentation/testing/html/screenshot_html_validation_contactpage.png)
    </details>
    <details>
    <summary>Register page (signup.html) - ERRORS Detail - See bug in Table</summary>  

    ![Register page](documentation/testing/html/screenshot_html_signup_errors1.png)
    </details>
    <details>
    <summary>Register page (signup.html) - ERRORS Detail 2 - See bug in Table</summary>  

    ![Register page](documentation/testing/html/screenshot_html_signup_errors2.png)
    </details>
    <details>
    <summary>Login page (signin.html)</summary>  

    ![Login page](documentation/testing/html/screenshot_html_signin.png)
    </details>
    

    #### Registered User Pages (Logged in)
    <details >
    <summary>Booking Dashboard page (booking_dashboard.html)</summary>  

    ![Booking Dashboard page](documentation/testing/html/screenshot_html_validation_bookingdashboard.png)
    </details>
    <details >
    <summary>Request Booking page (request_booking.html)</summary>  

    ![Request Booking page](documentation/testing/html/screenshot_html_validation_bookingrequestpage.png)
    </details>
    <details >
    <summary>Edit Booking page (edit_booking.html)</summary>  

    ![Edit Booking page](documentation/testing/html/screenshot_html_validation_editbooking.png)
    </details>
    <details>
    <summary>Signout page (signout.html)</summary>  

    ![Signout page](documentation/testing/html/screenshot_html_validation_signout.png)
    </details>
    
    #### Custom Error Pages
    <details >
    <summary>404 Error Page (404.html)</summary>  

    ![404 Error page](documentation/testing/html/screenshot_html_404page.png)
    </details>
    <details >
    <summary>500 Error page (500.html)</summary>  

    ![500 page](documentation/testing/html/screenshot_html_404page.png)
    </details>
    
  - #### CSS Validation
    I used the [W3C Jigsaw](https://jigsaw.w3.org/css-validator/) for CSS validation.
    <details >
    <summary>CSS Validation</summary>  

    ![screenshot of CSS validation](documentation/testing/css/screenshot_css_validation.png)
    </details>
  - #### Javascript Validation
    I used the [Jshint Linter](https://jshint.com/) for Javascript code validation.
    <details >
    <summary>Javascript Validation</summary>  

    ![screenshot of Javascript code validation](documentation/testing/js/screenshot_javascript_validation.png)
    </details>
  - #### Python Validation
    I used the [Code Institute PEP8 Python Linter](https://pep8ci.herokuapp.com/) for code validation. Unresolved bugs are noted in the bug table.
    #### Wimpleton Project
    <details><summary>urls.py</summary>

    ![urls.py](documentation/testing/python/screenshot_python_wimpleton_urls.png)
    </details>
    <details><summary>settings.py</summary>

    ![urls.py](documentation/testing/python/screenshot_python_wimpleton_settings.png)
    </details>

    #### Booking App
    <details><summary>urls.py</summary>

    ![urls.py](documentation/testing/python/screenshot_python_booking_urls.png)
    </details>
    <details><summary>views.py</summary>

    ![views.py](documentation/testing/python/screenshot_python_booking_views.png)
    </details>
    <details><summary>models.py</summary>

    ![models.py](documentation/testing/python/screenshot_python_booking_models.png)
    </details>
    <details><summary>forms.py</summary>

    ![forms.py](documentation/testing/python/screenshot_python_booking_forms.png)
    </details>
    <details><summary>admin.py</summary>

    ![admin.py](documentation/testing/python/screenshot_python_booking_admin.png)
    </details>
    <details><summary>test_forms.py</summary>

    ![test_forms.py](documentation/testing/python/screenshot_python_booking_test_forms.png)
    </details>
    <details><summary>test_views.py</summary>

    ![test_views.py](documentation/testing/python/screenshot_python_booking_test_views.png)
    </details>

  ### Search Engine Optimization
  This application was developed with HTML, CSS, Javascript, and Python using the Django Web Framework.
  - #### HTML Validation
    The [W3C HTML validator](https://validator.w3.org/) was used for the HTML validation. I copied the page source of the fully rendered page into the validator for testing.
    #### Public Pages
    <details >
    <summary>Home page (base.html and index.html)</summary>  

    ![Hpme page](documentation/testing/html/screenshot_html_validation_indexpage.png)
    </details>

  ### Unit Testing
  I was able to successfully execute unit testing on the booking form and the email contact form. 

  #### Unit Tests Run
  - Forms: Test EmailForm .is_valid()
  - Forms: Test EmailForm if no data
  - Forms: Test BookingForm .is_valid()
  - Forms: Test BookingForm if not data

  <details><summary>Unit Testing Results</summary>
  
  ![unit testing](documentation/testing/unit_test/screenshot_unit_test.png)
  </details>



  ### Manual Testing
  Manual testing was performed on the website checking to ensure pages rendered correctly, input forms worked correctly, and a user was able to create, view, edit, and delete their bookings.

  #### Browsers
  1. Microsoft Edge
  2. Google Chrome
  3. Opera

  #### The results of testing are as follows:
  | Page | Test | Pass/Fail |
  | ---- | ---- | --------- |
  | Home page | Does the Home page load correctly? | Yes |
  | Home page (base.html) | Do all the navigation links work? | Yes |
  | | Do all the footer links work? | Yes |
  | | Is the user able to see a notification in the navbar that they are currently logged in? | Yes |
  | Venue Hire page | Does the Venue Hire page render correctly? | Yes |
  | | Do all the venues render correctly? | Yes |
  | | Does the generic booking link take you the booking form page (or Sign in page if not signed in? | Yes |
  | | Do each of the booking links at the bottom of each venue link correctly to the Booking form page and set the initial value for the venue in the form? | Yes |
  | About page | Does the About page render correctly? | Yes |
  | Contact page | Does the Contact page render correctly? | Yes |
  | | Does the Contact Email Contact form work correctly? | Yes |
  | | Does the Contact Email Contact form display error and confirmation messages appropriately? | Yes |
  | Venue Bookings page | Does the Venue Booking page correctly render the Booking Dashboard | Yes |
  | | Do approved, pending approval, and expired bookings display in the correct sections? | Yes |
  | | Does the Request a booking button work correctly? | Yes |
  | | Do the edit and delete bookings buttons work correctly? | Yes |
  | Request Booking page | Does the Request Booking page render correctly? | ? |
  | | Does the Request Booking form work correctly and allow a user to request a booking? | Yes |
  | | Do the form error messages display correctly? | Yes |
  | | Does a successful request redirect correctly to the booking dashboard and display a success message? | Yes |
  | | Does the event date input validated and display the correct error handling? | Yes |
  | | Does the number of guests input validated and display the correct error handling? | Yes |
  | Edit Booking page | Does the Edit booking page render correctly? | Yes |
  | | Does the Edit booking page allow the user to edit a specific existing booking? | Yes |
  | | Is the input validated and display an error messages when not valid? | Yes |
  | Delete Booking button | Does the Delete booking button open a Deletion modal correctly? | Yes |
  | | Does the Delete booking button allow the user to delete a selected booking associated that user? | Yes |
  | Register page | Does the Register user page render correctly? | Yes |
  | Register page | Does the Register user page allow a visitor to register as a user? | Yes |
  | Sign out page | Does the Sign out page render correctly? | Yes |
  | Sign out page  | Does the sign out page allow a user to sign out? | Yes |
  | 404 Error page | Does the 404 error page render correctly when visitor attempts to navigate to a page that doesn't exist? | Yes |
  | 500 Error page | Does the 500 error page render correctly when there is a server error | Yes |
  | Admin panel | Can only access the admin panel if any authorised user? | Yes |
  

  #### Bugs and Fixes
  | Bug | Page | Fix |
  | --- | ---- | --- |
  | Error message in Edit Booking form is displaying incorrect message | Edit booking page | Updated error message to be more appropriate |
  | 500 Error message has wrong copy | 500 Error page | Updated error message to be more appropriate |
  | Parse error | styles.css | Remove errant character |
  | Family Name for font family | style.css | Add quotes around family name |
  | One undefined variable | bookings.js | Add "globals bootstrap" to top of code to remove warning |

  
  ### Unfixed Bugs
  - Although there were some spots where I could have found a better solution, there were no bugs that I was able to find that I could not resolve unless otherwise noted.
  
  ### Unresolved Linter Code Errors

  | Bug | Line | Unresolved Reason |
  | --- | ---- | --- |
  | There were a few places that were greater than the 79 character length max | settings.py - line 129 | Was unable to resolve as caused more errors when shortened |
  | There were a few places that were greater than the 79 character length max | views.py | Could not reduce error strings further and was unable to break up the line without causing further problems |

  

