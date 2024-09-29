# Wimpleton House Booking Application
  Back to [README](https://github.com/hysinh/wimpleton-booking-app/blob/main/README.md)

## Testing Overview
## CONTENTS  
  
* [User Story Testing](#user-story-testing)
* [Validator Testing](#validator-testing)
  * [HTML Validation](#html-validation)
  * [CSS Validation](#css-validation)
  * [Javascript Validation](#javascript-validation)
  * [Python Validation](#python-validation)
* [Unit Testing](#unit-testing)
* [Error Handling](#error-handling)
* [Manual Testing](#manual-testing)
  * [Input Validation](#input-validation)
  * [Add Mortgages](#add-mortgages)
  * [View Mortgages](#view-mortgages)
  * [Compare Mortgages](#compare-mortgages)  
  * [Overpayments](#overpayments)
  * [Amortization Schedule](#amortization-schedule)
  * [Mortgage Data Analysis](#mortgage-data-analysis)
  * [Exit Program](#exit-program)
* [Future Features](#future-features)
* [Technologies](#technologies)
  * [Languages Used](#languages-used)
  * [Technologies and Programs Used](#technologies-and-programs-used)
  * [Deployment](#deployment)
* [Testing](#testing)
  * [Python3 Validation](#python3-validation)
  * [Manual Testing](#manual-testing)
  * [Bugs and Fixes](#bugs-and-fixes)
  * [Unfixed Bugs](#unfixed-bugs)
* [Credits](#credits) 

  
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
  | Home page | Does the Home page load correctly? | ? |
  | Home page (base.html) | Do all the navigation links work? | ? |
  | Home page (base.html) | Do all the footer links work? | ? |
  | Home page (base.html) | Is the user able to see a notification in the navbar that they are currently logged in? | Yes |
  | Venue Hire page | Does the Venue Hire page render correctly? | ? |
  | Venue Hire page | Do all the venues render correctly? | ? |
  | Venue Hire page | Does the generic booking link take you the booking form page? | ? |
  | Venue Hire page | Do each of the booking links at the bottom of each venue link correctly to the Booking form page and set the initial value for the venue in the form? | ? |
  | About page | Does the About page render correctly? | ? |
  | Contact page | Does the Contact page render correctly? | ? |
  | Venue Bookings page | Does the Venue Booking page correctly render the Booking Dashboard | ? |
  | Venue Bookings page | Do approved, pending approval, and expired bookings display in the correct sections? | ? |
  | Venue Bookings page | Does the Request a booking button work correctly? | ? |
  | Venue Bookings page | Do the edit and delete bookings buttons work correctly? | ? |
  | Request Booking page | Does the Request Booking page render correctly? | ? |
  | | Does the Request Booking form work correctly and allow a user to request a booking? | ? |
  | | Do the form error messages display correctly? | ? |
  | | Does a successful request redirect correctly to the booking dashboard and display a success message? | ? |
  | | Does the event date input validated and display the correct error handling? | ? |
  | | Does the event date input validated and display the correct error handling? | ? |
  | | Does the number of guests input validated and display the correct error handling? | ? |
  | Edit Booking page | Does the Edit booking page render correctly? | ? |
  | Edit Booking page | Does the Edit booking page allow the user to edit a specific existing booking? | ? |
  | Delete Booking button | Does the Delete booking button open a Deletion modal correctly? | ? |
  | Delete Booking button | Does the Delete booking button allow the user to delete a selected booking associated that user? | ? |
  | Register page | Does the Register user page render correctly? | ? |
  | Register page | Does the Register user page allow a visitor to register as a user? | ? |
  | Sign out page | Does the Sign out page render correctly? | ? |
  | Sign out page  | Does the sign out page allow a user to sign out? | ? |
  | 404 Error page | Does the 404 error page render correctly when visitor attempts to navigate to a page that doesn't exist? | ? |
  | 500 Error page | Does the 500 error page render correctly when there is a server error | ? |
  | Admin panel | Can only access the admin panel if any authorised user? | Yes |
  | Admin | Does the 500 error page render correctly when there is a server error | ? |
  



  #### Bugs and Fixes
  | Bug | Page | Fix |
  | --- | ---- | --- |
  | Confirmation message for saved mortgage option not printing to terminal after saving a mortgage | Extra Monthly Principal Payments | Removed code that ends loop to resolve. |
  | Confirmation message for saved mortgage option not printing to terminal after saving a mortgage | Extra Lump Principal Payments | Removed code that ends loop to resolve. |
  | Unclear for users what to do if Main Menu is no longer visible. | All Pages | Add text above menu prompt that instructs user to enter 0 to go to the Main menu. |
  | Table needs to display Mortgage name rather than Mortgage key | Compare Mortgages | Updates Mortgage class method that generates values for comparison table so that mortgage name displays instead of mortgage ID/key |
  | Table needs to display Mortgage name rather than Mortgage key | Amortization Schedule | Replace print statement with mortgage name variable rather than Mortgage key |
  | Unexpected indentation | Main Menu Prompt| Removes backslash from string |

  
  ### Unfixed Bugs
  - Although I have included a function that clears the terminal, I noticed that anything above the terminal screen does not clear and is still available to view if you scroll up. This is potentially confusing but I was not able to resolve it. My mentor said that it is common for older terminals to push content upward and not truly clear the screen.
  - When viewed through a mobile device, the terminal goes off screen. I will need to research this to see if this is something that is resolvable.
  
  ### Unresolved Linter Code Errors

  | Bug | Line | Unresolved Reason |
  | --- | ---- | --- |
  | Line length | 111 | I tried several different places to attempt to break up the lines to stay <79 but it resulted in poor print outcomes. |
  | Line length | 121 | I tried to delete the extra spaces in the formula but it caused "missing white space around operator" errors. |

  

## Credits
### Content
- ASCII Art https://stackoverflow.com/questions/9632995/how-to-easily-print-ascii-art-text
- https://pypi.org/project/pyfiglet/
- http://www.figlet.org/examples.html
- Clearing the console https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
- Input validation
https://www.copahost.com/blog/input-python/#:~:text=For%20example%2C%20if%20you%20want,%22)
- Mortgage calculator formulas https://en.wikipedia.org/wiki/Mortgage_calculator,
- Mortgage calculator https://www.ccpc.ie/consumers/money-tools/extra-mortgage-payments-calculator/
- Mortgage calculator https://www.ccpc.ie/consumers/money-tools/mortgage-calculator/
- https://automatetheboringstuff.com/2e/chapter8/
- Python dictionaries https://www.codecademy.com/learn/dscp-python-fundamentals/modules/dscp-python-dictionaries/cheatsheet
- Python dictionaries https://www.freecodecamp.org/news/add-to-dict-in-python/
- Python dictionaries https://www.w3schools.com/python/python_dictionaries_nested.asp
- Python dictionaries https://www.digitalocean.com/community/tutorials/python-add-to-dictionary
- Tabulate https://pypi.org/project/tabulate/
- Amoritization https://www.investopedia.com/terms/a/amortization.asp
- Amoritization https://discuss.python.org/t/calculation-of-mortgage-amortization/20687/3
- Amoritization https://sidhanthk9.medium.com/how-to-code-an-amortization-schedule-in-python-e2d2b417c61a
- Color https://pypi.org/project/termcolor/
https://sparkbyexamples.com/pandas/print-pandas-dataframe-without-index/#:~:text=Use%20hide_index(),Python%203.7%20or%20the%20latest.
- https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
- https://www.geeksforgeeks.org/clear-screen-python/
- W3Schools Python https://www.w3schools.com/python
- https://www.python.org/
