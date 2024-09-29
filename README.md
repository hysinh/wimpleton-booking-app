# Wimpleton House Booking Application
  ![screenshot of landing page](documentation/readme/screenshot_amiresponsive.webp)

  [View Live Project Here](https://wimpleton-booking-edd90b3067af.herokuapp.com/)

## Introduction
Wimpleton House Booking website is a full-stack web application created with HTML, CSS, JS, Python, the Django web framework and the Bootstrap library. This website application allows users to view a fictional Irish country estate that hires out it's buildings and grounds for special events. Visitors to the website are able to view the different venue hire options. Upon registering as a user of the website and logging in, users are then able to request to book a particular venue option for a specific date. This booking request reserves the chosen venue for the chosen date and prevents another user from booking the same venue for the same date. Users have access to a Booking Dashboard which allows them to view and manage their bookings.

## CONTENTS  
  
* [User Experience](#user-experience)
  * [User Stories](#user-stories) 
* [Data Model](#data-model)
  * [Design](#design)
  * [Flowchart](#flowchart)
* [Features](#features)
  * [Logo](#logo)
  * [Menu](#menu)
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

## User Experience
The goal of the Wimpleton House Booking website is to provide a business tool that allows the business to engage meaningfully with potential clients. The website offers information about the different Venue hire options for the estate and then allows visitors to register as users and create, view, edit, and delete booking requests with the estate.

Although some events may be one-off events like a wedding, the estate has a goal of creating ongoing relationships with event planners, businesses, corporations, and communities for events that potentially could be annual, bi-annual, quarterly, or even more frequent and facilitates clients managing their bookings and review past booking records.
- ### Visitor Goal
  As a user, I want to easily view potential venue hire options at the Wimpleton House estate, to create a booking, and to view and manage all my bookings.
- ### User Stories
  1. As a vistor, I can access the main, public pages and navigate easily through the website.
  2. As a visitor, I can easily review the venue hire options available at the Wimpleton house.
  3. As a visitor, I can easily register as a user to the website.
  4. As a user, I can log into the website to access my account.
  5. As a user, I can see that I am logged into the website on the navbar.
  6. As a user, I can easily access the Booking Dashboard and view my current and expired bookings.
  7. As a user, I can easily book a specific venue for a specific date either via the Booking dashboard or directly from the Venue Hire page.
  8. As a logged in user, I can securely end by session by logging out.
  9. As a visitor, I can see customized error pages for 404 and 500 errors so that I can understand what happened and take the appropriate action.

- ### Site Admin Stories
  1. As a site owner/administrator, I can create a user account for a client.
  2. As a site owner/administrator, I can create, read, update, and delete Venue options and descriptions.
  3. As a site owner/administrator, I can create, read, update, and delete Bookings for clients.
  4. As a site owner/administrator, I can read, update, and delete existing Bookings for a client.
  5. As a site owner/administrator, I can approve a booking, which in theory, initializes the next step for the client for the booking (i.e. initialises an event consultation, contract creation, and deposit payment).
  6. As a site owner/administrator, I can view messages sent through the email contact form via the website.


## Agile Methodology
The Agile Methodology was the project management approach used for this project. I attempted to break the project into phases and followed a cycle of planning, executing, and evaluating.
### Kanban Board 
  Something about kanban boards

### UI Design
  I created some rough wireframes when first planning the website. I had three basic variations with consideration to reponsive design for the mobile, tablet, and desktop layouts.

  <details >
  <summary>Design Mockups</summary>  

  ![wireframes](link)
  </details>


## Features
### Navbar - top navigation
The navbar incorporates the logo and a responsive navbar that collapses to a hamburger when a device is less than a tablet. The navigation options provide the user with all of their potential navigation options including registering as a user or logging into the user dashboard to create and/or manage bookings.
<details >
<summary>Public navbar</summary>  

![navbar](documentation/readme/features/screenshot_navbar_laptop.png)
</details>
<details>
<summary>Registered user navbar (logged in)</summary>

![navbar - logged in](link)
</details>
 

### Home Page
The Home page provides a featured image of Wimpleton House as well as brief details about the venue hire opportunities at the Wimpleton.
<details>
<summary>Home Page</summary>

![home page](link)
</details>


### Venue Hire Page
The Venue Hire page features details about each of the venue hire options available at the Wimpleton Hosue. A visitor also can click on a button that directs them to the Booking form if they are logged in or to the sign in page if they are not already signed in or registered as a user. There are additional buttons at the end of each venue description that once clicked directs the user to the Booking form with that particular venue preselected in the booking form. Each of the venue images and descriptions are generated dynamically from the venues saved in the database.
<details>
<summary>Venue Hire page</summary>

![venue hire page](link)
</details>

### About Page
The About page provides basic information about Wimpleton House and emphasises it's versatility as a venue for hire for special events. Following the Wimpleton House details, there is a gallery that features images of various special events that were hosted previously at the Wimpleton House.
<details>
<summary>About page</summary>

![about page](link)
</details>

### Contact Page
The Contact page features basic contact information for the Wimplton House including address and telephone details. The page also includes a google maps embedded into the page. The Contact page also features a email contact form that allows the vistor to ask questions or to send a message to the Wimpleton House staff by completing the form. The information is stored in the database and the messages accessible to staff members via the Admin panel.
<details>
<summary>Contact Page</summary>

![contact page](link)
</details>



### Compare Mortgages
<details>
<summary></summary>

![screenshot of footer](docs/documentation/screenshot_compare_mortgages.png)
</details>
When the user has saved a minimum of two Mortgages, they can view a mortgage comparison table that displays the morgage name, principal amounts, APR, loan length, monthly payments, and lifetime interest. If the user has saved a minimum of two Mortgages, a red error message displays alerting them of the problem. The user can then select an option that allows them to create and save a Mortgage in the session. 

### Overpayments
<details >
<summary></summary>  

![screenshot overpayments](docs/documentation/screenshot_overpayments.png)
</details>  
There are two options in the Overpayments feature: 1) Additional Monthly Principal overpayments and 2) A Lump Principal Payment. Once this feature is selected, the user is required to choose which type of Overpayment they would like to calculate.

- ### Additional Monthly Principal Overpayment
  <details >
  <summary></summary>  

  ![screenshot monthly overpayments](docs/documentation/screenshot_overpayments_monthly.png)
  </details>  
  The user is prompted to input basic mortgage details as well as an amount for the extra monthly payments. This input is then used to calculate a Mortgage profile and prints both the profile and an amortization schedule based on the new calculations. The user is given the option to save this mortgage to their mortgages when the calculations are completed.

- ### Lump Principal Overpayment
  <details >
  <summary></summary>  

  ![screenshot lump overpayments](docs/documentation/screenshot_overpayments_lump.png)
  </details>  
  The user is prompted to input basic mortgage details as well as an amount for the lump payment to be applied to the Principal balance. This input is then used to calculate a Mortgage profile and prints both the original profile inputed and then an updated Mortgage profile. The user is given the option to save this updated mortgage to their mortgages when the calculations are completed.


### Amortization Schedule
<details >
<summary></summary>  

![screenshot amortization](docs/documentation/screenshot_amortization.png)
</details>  
This option requires at least one saved Mortgage profile. If there is an insufficient number of Mortgage profiles, the user is alerted with a red error message and redirected back to the Main menu options. If there is at least one Mortgage profile, it is printed in a list and the user is asked to input a Mortgage Profile selection. Once selected, the amortization schedule is calculated and printed to the terminal. The user can either choose another Mortgage profile to view or can exit to the main menu. 


### Mortgage Data Analysis
<details >
<summary></summary>  

![screenshot amortization](docs\documentation\screenshot_mortgage_data_analysis.png)
</details>  
When this option is selected, the data stores in a Google Sheet is retrieved and the average is calculated for each of the following catergories and printed for the user to view and compare inputed averages of all users to their own mortgage needs.
  - Average Principal Amount
  - Average APR
  - Average Loan Length
  - Average Monthly Payment
  - Average Lifetime Interest

### Exit Program
<details >
<summary></summary>  

![screenshot exit](docs/documentation/screenshot_exit.png)
</details> 
Should the user which to exit the Mortgage Comparison Tool, they can select option 6 from the Main menu. When this option is selected, the terminal is cleared and a Thank you message is printed before the program is terminated. 

### Future Development
- For future development, I wanted to implement a table of data analysis of the aggregate mortgage data inputed by users to provide insight into the type of mortgages that user want to compare. Examples of potential insights would be average mortgage principal amount, average length of the mortgage, and average APR. 
- I noticed that other students implemented custom heroku terminal shell for deployment. I thought this was interesting and would like to implement this should I have more time to develop this further.
- At the moment, the user is limited to 10 characters when naming their mortgage. This limit could be raised, but I would need additional time to ensure that that the printed output would be limited to a certain character length so that it doesn't not disrupt the layout of the comparison table.
- During testing, it was revealed that when users save Mortgage profiles after applying Extra Monthly Principal payments, the mortgage profile that is saved is based on the original Mortgage inputs and is not updated with the new loan length and lifetime interest on the loan. For a future feature, I would like to be able to recalculate the updated length of the loan and the lifetime loan interest. With these updated values, users could then save this updated mortgage profile into their session to use to compare against other saved mortgages.


## Technologies
  ### Languages Used
  - Python3

  ### Technologies and Programs Used
  - GitHub - used to save and store all the files for this website
  - GitPod and VSCode - was used as the IDE to develop and test the code for this website in both the cloud and locally.
  - Git - provided the version control
  - Heroku - provided the cloud deployment environment shell and Command Line Interface (CLI)
  - Google Docs - used for notes and documentation
  - Google Sheets - provided the spreadsheet application for storing the data generated by user inputs
  - draw.io - used for flowchart creation
  - PEP8 Code Institute Python Linter - tested the validity of python code (https://pep8ci.herokuapp.com/)

  ### Python Libraries
  The following libraries in this program.
  - Colorama -  producing colored terminal text
  - pyfiglet -  takes ASCII text and renders it in ASCII art fonts
  - Tabulate - displays lists in a table
  - Termcolor - Allows printing in color
  - gspread - Python API for Google Sheets.
  - googleauth - Google authentication library for Python


  ### Deployment
  GitHub and Heroku was used to deploy this website using the Gitpod Code Institute template which preloads any required dependencies. The following steps were taken:

  
  1. Log into GitHub account. 
  2. Navigate to the project repository: [Memory-game]((https://github.com/hysinh/mortgage-comparison-tool)
  3. Navigate to the CODE link on the navigation across the top.
  3. Then, navigate to the green CODE button on the right side and click.
  4. Select the Local tab and click on the copy icon to make a copy of the repository.
  5. Log into Heroku.com account.
  6. Navigate to the "New" button on the top right.
  7. Click on "New" and then click on "Create a new app".
  8. On the next page, create a unique App name for your deployment and choose a region. Then, click on the "Create app" button.
  9. Once your app has been created, it directs you to a new screen.
  10. Navigate across the top of the screen and click on the "Settings" tab.
  11. Navigate down the page and click on the "Reveal Config Vars" button.
  12. For the first key, type in "CREDS" and then copy and paste the entirety of the creds.json file into the value box.
  13. For the second key, type in "PORT" and then type in "8000" in its corresponding value.
  14. Under Buildpacks, add the <b>python</b> buildpack first. Then, add the <b>nodejs</b> buildpack. The buildpacks must be added in that order.
  15. After this is complete, navigate to the Deploy tab from the menu across the top of the page. Click on "GitHub" under Deployment method and provide the required access when prompted.
  16. Choose Automatic or Manual deployment.
  17. Click "Deploy" when ready to deploy.


  #### How to clone the Mortgage Comparison Tool & make changes:
  1. Open the [Mortgage-Comparison-tool repository](https://github.com/hysinh/mortgage-comparison-tool) on GitHub.
  2. Navigate to the CODE link on the navigation across the top.
  3. Then, navigate to the green CODE button on the right side and click.
  4. Select the Local tab and click on the copy icon to make a copy of the repository.
  5. Then navigate back to your main GitHub dashboard and then create a new repository with your desired name.
  6. On the next page, navigate to the bottom of the page and select Import code under "Import code from another repository".
  7. In the next window, paste the copied link of the [Memory-game repository](https://github.com/hysinh/mortgage-comparison-tool) into the line.
  8. Then, click Begin Import to import the repository code.
  9. Make changes and/or deploy as desired.
  10. This program requires the use of a Google sheets file with a Google Drive and Google Sheets API to setup as is.


  ## Testing

  ### Validator Testing
  This application was developed with Python3. No HTML, CSS, or Javascript was used. 
  - #### Python3 Validation
    I used the Code Institute PEP8 Python Linter for code validation.
    <details >
    <summary>Python Validation</summary>  

    ![screenshot of PEP8 Python code validation](docs\documentation\screenshot_pep8_validation.png)
    </details>



  ### Manual Testing
  Manual testing was performed on the website checking for print errors, content errors, and any errors in the flow of the application or in it's calculations.

  #### Browsers
  1. Microsoft Edge
  2. Google Chrome
  3. Opera

  #### The results of testing are as follows:
  | Page | Test | Pass/Fail |
  | ---- | ---- | --------- |
  | Intro/Logo  | Does the Logo page load and allow the user to progress to the Main Menu? | Pass |
  | Main Menu  | Does the Main menu display correctly | Pass |
  | Main Menu  | Is the input validation for the Main Menu working correctly? | Pass |
  | Main Menu  | If the user selects an option from the Main Menu, does it direct the user to that option correctly? | Pass |
  | Add Mortgage  | On the Add Mortgage page, does it allow the user to create a Mortgage profile? | Pass |
  | Add Mortgage  | Is the input validation on the Add Mortgage page working? | Pass |
  | Add Mortgage  | Is a Mortgage profile added correctly if the user selects this option? | Pass |
  | Add Mortgage  | Is the Google Sheet updated with the data of the new Mortgage profile created regardless of whether the Mortgage profile is saved for the session? | Pass |
  | Add Mortgage  | Once Add Mortgage options are completed, is the user directed back to the Main Menu options? | Pass |
  | View Mortgage  | Does the page display an error message if there are no saved Mortgage profiles and directed back to the Main Menu? | Pass |
  | View Mortgage  | Does the page display all of the saved Mortgage Profiles and their name to the user? | Pass |
  | View Mortgage  | Is the user able to select a Mortgage Profile to view? | Pass |
  | View Mortgage  | Does an error message display if the user enters an invalid Mortgage option? | Pass |
  | View Mortgage  | Does the page display all of the saved Mortgage Profiles and their name to the user? | Pass |
  | View Mortgage  | When the user enters a valid Mortgage option, is the Mortgage profile displayed on the terminal? | Pass |
  | View Mortgage  | Is the user able to view another Mortgage and is given the option to exit this page and return to Main Menu? | Pass |
  | Compare Mortgages  | Does the page display an error message if there are less than 2 Mortgage profiles saved and directed back to the Main Menu? | Pass |
  | Compare Mortgages  | Does the page display all of the saved Mortgage Profiles and their name to the user? | Pass |
  | Compare Mortgages  | If there are 2 or more saved Mortgage profiles saved, does a comparison table print to the terminal? | Pass |
  | Compare Mortgages  | Is the user directed back to the Main Menu after the comparison table display is completed? | Pass |
  | Overpayments  | Is the user given an option to explore Extra Monthly Principal payments or Lump Principal Payments? | Pass |
  | Overpayments  | Is the user given an error message if they choose an invalid option? | Pass |
  | Overpayments  | Is the user able to exit the menu and return to the Main Menu? | Pass |
  | Extra Monthly Principal Overpayments  | Is the user able to enter Mortgage profile with extra monthly principal payments? | Pass |
  | Extra Monthly Principal Overpayments  | Are all user inputs validated with an error message printed? | Pass |
  | Extra Monthly Principal Overpayments  | Once the data is accepted, is the Mortgage profile displayed with an updated Amortization schedule? | Pass |
  | Extra Monthly Principal Overpayments  | Is the user able to save their Mortgage profile if desired? Does a confirmation display | Pass |
  | Extra Monthly Principal Overpayments  | Is the user redirected to the Main menu? | Pass |
  | Extra Lump Overpayments  | Is the user able to enter Mortgage profile with extra monthly principal payments? | Pass |
  | Extra Lump Overpayments | Are all user inputs validated with an error message printed? | Pass |
  | Extra Lump Overpayments | Once the data is accepted, is the Mortgage profile displayed with an updated Amortization schedule? | Pass |
  | Extra Lump Overpayments | Is the user able to save their Mortgage profile if desired? Does a confirmation display| Pass |
  | Extra Lump Overpayments  | Is the user redirected to the Main menu? | Pass |
  | Amortization Schedule  | Does the page display an error message if there are no saved Mortgage profiles and directed back to the Main Menu? | Pass |
  | Amortization Schedule  | Does the page display all of the saved Mortgage Profiles and their name to the user? | Pass |
  | Amortization Schedule  | Is the user able to select a Mortgage Profile to amortize? | Pass |
  | Amortization Schedule  | Does an error message display if the user enters an invalid Mortgage option? | Pass |
  | Amortization Schedule  | Does an amortization schedule print for the selected Mortgage Profile | Pass |
  | Amortization Schedule  | Is the user able to view another Mortgage and is given the option to exit this page and return to Main Menu? | Pass |
  | Exit Program  | Does the terminal clear and an exit message print when this option is selected? | Pass |
  | 0 Menu Option  | Does the terminal clear and the Main menu print with a prompted to input a Menu option? | Pass |



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
