# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

As my project uses Jinja syntax, such as `{% for loops %}` and `{% url 'home' %}`  
it will not validate properly if I copy and paste into the HTML validator straight from my source files.

Usually in order to properly validate these types of files, it's recommended to
[validate by uri](https://validator.w3.org/#validate_by_uri) from the deployed Heroku pages.

Some of the pages on this site require a user to be logged-in and authenticated,
and will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have
access to login to the pages.

In order to properly validate my HTML pages with Jinja syntax for authenticated pages, I followed these steps:

- Navigate to the deployed pages which require authentication
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdjango-pp4-failte-bistro-dd00169a966c.herokuapp.com%2F) | ![screenshot](documentation/testing/home-no-errors.JPG) | Pass: No Errors |
| About | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdjango-pp4-failte-bistro-dd00169a966c.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/testing/about-no-errors.JPG) | Pass: No Errors |
| Menu | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdjango-pp4-failte-bistro-dd00169a966c.herokuapp.com%2Fmenu%2F) | ![screenshot](documentation/testing/menu-list-no-errors.JPG) | Pass: No Errors |
| Menu Detail | N/A | ![screenshot](documentation/testing/menu-detail-no-errors-direct-input.JPG) | Pass: No Errors |
| Reservation | N/A | ![screenshot](documentation/testing/reservations-no-error-direct-input.JPG) | Pass: No Errors |
| Booking | N/A | ![screenshot](documentation/testing/create-booking-no-errors-direct-input.JPG) | Pass: No Errors |
| Log In | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdjango-pp4-failte-bistro-dd00169a966c.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/testing/login-no-errors.JPG) | Pass: No Errors |
| Log Out | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdjango-pp4-failte-bistro-dd00169a966c.herokuapp.com%2F) | ![screenshot](documentation/testing/logout-no-errors.JPG) | Pass: No Errors |
| Sign Up | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fdjango-pp4-failte-bistro-dd00169a966c.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/testing/signup-no-errors.JPG) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | N/A | ![screenshot](documentation/testing/css-no-error.JPG) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Jshint URL | Screenshot |  
| --- | --- | --- |
| comments.js | N/A | ![screenshot](documentation/testing/comments-no-error.JPG) | 
| messages.js |  N/A | ![screenshot](documentation/testing/messages-no-error.JPG) | 

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py (about) | ![screenshot](documentation/testing/about-admin-no-error.JPG) | Pass: No Errors |
| apps.py (about) | ![screenshot](documentation/testing/about-apps-no-error.JPG) | Pass: No Errors |
| urls.py (about) | ![screenshot](documentation/testing/about-urls-no-error.JPG) | Pass: No Errors |
| views.py (about) | ![screenshot](documentation/testing/about-views-no-error.JPG) | Pass: No Errors |
| admin.py (booking) | ![screenshot](documentation/testing/booking-admin-no-error.JPG) | Pass: No Errors |
| apps.py (booking) | ![screenshot](documentation/testing/booking-apps-no-error.JPG) | Pass: No Errors |
| forms.py (booking) | ![screenshot](documentation/testing/booking-forms-no-error.JPG) | Pass: No Errors |
| models.py (booking) | ![screenshot](documentation/testing/booking-models-no-error.JPG) | Pass: No Errors |
| test_apps.py (booking) | ![screenshot](documentation/testing/booking-test-apps-no-error.JPG) | Pass: No Errors |
| test_forms.py (booking) | ![screenshot](documentation/testing/booking-test-forms-no-error.JPG) | Pass: No Errors |
| test_views.py (booking) | ![screenshot](documentation/testing/booking-test-views-no-error.JPG) | Pass: No Errors |
| urls.py (booking) | ![screenshot](documentation/testing/booking-urls-no-error.JPG) | Pass: No Errors |
| views.py (booking) | ![screenshot](documentation/testing/booking-views-no-error.JPG) | Pass: No Errors |
| apps.py (home) | ![screenshot](documentation/testing/home-apps-no-error.JPG) | Pass: No Errors |
| urls.py (home) | ![screenshot](documentation/testing/home-urls-no-error.JPG) | Pass: No Errors |
| views.py (home) | ![screenshot](documentation/testing/home-views-no-error.JPG) | Pass: No Errors |
| admin.py (menu) | ![screenshot](documentation/testing/menu-admin-no-error.JPG) | Pass: No Errors |
| apps.py (menu) | ![screenshot](documentation/testing/menu-apps-no-error.JPG) | Pass: No Errors |
| forms.py (menu) | ![screenshot](documentation/testing/menu-forms-no-error.JPG) | Pass: No Errors |
| models.py (menu) | ![screenshot](documentation/testing/menu-models-no-error.JPG) | Pass: No Errors |
| test_apps.py (menu) | ![screenshot](documentation/testing/menu-test-apps-no-error.JPG) | Pass: No Errors |
| test_forms.py (menu) | ![screenshot](documentation/testing/menu-test-forms-no-error.JPG) | Pass: No Errors |
| test_views.py (menu) | ![screenshot](documentation/testing/menu-test-views-no-error.JPG) | Pass: No Errors |
| urls.py (menu) | ![screenshot](documentation/testing/menu-urls-no-error.JPG) | Pass: No Errors |
| views.py (menu) | ![screenshot](documentation/testing/menu-views-no-error.JPG) | Pass: No Errors |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/menu-detail-content-desktop.JPG) ![screenshot](documentation/testing/menu-detail-textarea-desktop.JPG) ![screenshot](documentation/testing/menu-detail-comment-desktop.JPG) | Works as expected |
| Edge | ![screenshot](documentation/testing/edge-1.JPG) ![screenshot](documentation/testing/edge-2.JPG) ![screenshot](documentation/testing/edge-3.JPG) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/testing/menu-detail-comment-mobile.JPG) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/testing/menu-detail-comment-tablet.JPG) | Works as expected |
| Laptop | ![screenshot](documentation/testing/menu-detail-comment-laptop.JPG) | Works as expected |
| Desktop | ![screenshot](documentation/testing/menu-detail-comment-desktop.JPG) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | ![screenshot](documentation/testing/home-score-desktop.JPG) | Some minor warnings |
| Home | Mobile | ![screenshot](documentation/testing/home-score-mobile.JPG) | Some minor warnings |
| About | Desktop | ![screenshot](documentation/testing/about-score-desktop.JPG) | Some minor warnings |
| About | Mobile | ![screenshot](documentation/testing/about-score-mobile.JPG) | Some minor warnings |
| Menu | Desktop | ![screenshot](documentation/testing/menu-score-desktop.JPG) | Some minor warnings |
| Menu | Mobile | ![screenshot](documentation/testing/menu-score-mobile.JPG) | Some minor warnings |
| Menu Detail | Desktop | ![screenshot](documentation/testing/menu-detail-score-desktop.JPG) | Some minor warnings |
| Menu Detail | Mobile | ![screenshot](documentation/testing/menu-detail-score-mobile.JPG) | Some minor warnings |
| Reservation | Desktop | ![screenshot](documentation/testing/reservation-score-desktop.JPG) | Some minor warnings |
| Reservation | Mobile | ![screenshot](documentation/testing/reservation-score-mobile.JPG) | Some minor warnings |
| Booking | Desktop | ![screenshot](documentation/testing/booking-score-desktop.JPG) | Some minor warnings |
| Booking | Mobile | ![screenshot](documentation/testing/booking-score-mobile.JPG) | Some minor warnings |
| Sign Up | Desktop | ![screenshot](documentation/testing/signup-score-desktop.JPG) | Some minor warnings |
| Sign Up | Mobile | ![screenshot](documentation/testing/signup-score-mobile.JPG) | Some minor warnings |
| Sign In | Desktop | ![screenshot](documentation/testing/login-score-desktop.JPG) | Some minor warnings |
| Sign In | Mobile | ![screenshot](documentation/testing/login-score-mobile.JPG) | Some minor warnings |
| Sign Out | Desktop | ![screenshot](documentation/testing/logout-score-desktop.JPG) | Some minor warnings |
| Sign Out | Mobile | ![screenshot](documentation/testing/logout-score-mobile.JPG) | Some minor warnings |

## Manual Testing

| Page | Test | Outcome |
| -- | -- | -- |
| Nav Bar | All Nav Bar Links directs to correct page when clicked | Pass |
| Footer | All social links direct to corresponding site when clicked | Pass |
| Footer | All social links open in new tab | Pass |
| Home | When user is not authenticated when booking a table they are directed to sign in page or sign up page via a sign up link | Pass |
| Home | When user is authenticated when booking a table they are directed to the booking form. | Pass |
| Menu | When user is authenticated they can click on a menu dish and are directed to the menu detail page | Pass |
| Menu | When user is not authenticated they can click on a menu dish and are directed to the menu detail page | Pass |
| Menu Detail | When user is not authenticated they can not love a menu dish on the menu detail page and the heart counter remains unchanged | Pass |
| Menu Detail | When user is not authenticated they can not like a comment on the menu detail page and the like counter remains unchanged | Pass |
| Menu Detail | When user is not authenticated they must login or sign up to leave a comment on the menu detail page | Pass |
| Menu Detail | When user is not authenticated they must login or sign up to create, edit and or delete their own comment(s) on the menu detail page | Pass |
| Menu Detail | When user is authenticated they can create, edit and or delete their own comment(s) on the menu detail page | Pass |
| Menu Detail | When user is authenticated and they create their own comment(s) on the menu detail page the comment counter value increments | Pass |
| Menu Detail | Comment delete modal asks for confirmation before deletion | Pass |
| Menu Detail | When user is authenticated and they delete their own comment(s) on the menu detail page the comment counter value decreases | Pass |
| Menu Detail | When user is authenticated and they edit their own comment(s) on the menu detail page the comment counter value is unchanged | Pass |
| Menu Detail | When user is authenticated they can love a menu dish on the menu detail page and the heart counter value increments | Pass |
| Menu Detail | When user is authenticated they can unlove a menu dish on the menu detail page and the heart counter value decreases | Pass |
| Menu Detail | When user is authenticated they can like a comment on the menu detail page and the like counter value increments | Pass |
| Menu Detail | When user is authenticated they can unlike a comment on the menu detail page and the like counter value decreases | Pass |
| Reservations | When user is not authenticated they can not view the reservations page | Pass |
| Reservations | When user is authenticated they can view the reservations page | Pass |
| Reservations | When user is authenticated they can create, read, edit and delete reservations | Pass |
| Reservations | Reservation modal asks for confirmation before deletion | Pass |
| Authentication | User can create an account | Pass |
| Authentication | User can login to their account | Pass |
| Authentication | User can logout to their account | Pass |
| Authentication | Admin has has more privileges than a User | Pass |
| Authentication | Admin can post to the menu detail page. A user can not. | Pass |
| Authentication | Admin can delete post to the menu detail page. A user can not. | Pass |
| Authentication | Admin can review and approve comments on the menu detail page. A user can not. | Pass |
| Authentication | Admin can review and delete comments on the menu detail page. A user can not. | Pass |
| Comment Form | Form wont submit with empty content field | Pass |
| Reservation Form | Form wont submit with empty any fields | Pass |
| Reservation Form | Form wont submit with any non number characters in the contact number field | Pass |
|Reservation Form| Form does not let you book in the past | Pass |
|Reservation Form | Validation wont accept two identical bookings | Pass |

## Automated Testing

I have conducted a series of automated tests on my application. In total there are twenty tests.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal:

`python3 manage.py test`

![screenshot](documentation/testing/automated_tests.JPG)

## Bugs

**Fixed Bugs**

When submitting the reservation form the user / admin received a feedback message informing them of an invalid data type submission. On review of the reservation model, the GUESTS tuple had strings in the tuples and these were assigned to choices in the integer field of the number of guests. To resolve this error integers were coded instead of strings in the GUESTS tuple of tuples.

**Open Issues**



## Unfixed Bugs

There is a known bug in the menu list page. When there are three dishes in the starters row and admin posts a fourth dish, this new post pushes an earlier post to the next row and it takes up the entirety of the new row making it larger than the other posts.
This bug may be propagated to the main and desserts rows.

There is a known bug in the menu list page. In the menu_list.html file the three for loop counters are not all divisable by three. To get all the posts displaying in a row. Different values were used for the for loops.

[ Back To Top ](#testing)