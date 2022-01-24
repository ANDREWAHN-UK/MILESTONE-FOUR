This is the testing section of the readme, placed in a separate file:
- - - -
**8. Testing:**
- - - -

*8.1 Code Validation*
- - - - 

1. I used https://validator.w3.org to validate the html. 

The html validator returned the errors:
  * "The element button must not appear as a descendant of the a element."  which I corrected.
  *	"The type attribute is unnecessary for JavaScript resources.". - corrected
  * "The element button must not appear as a descendant of the a element." & "The element a must not appear as a descendant of the button element." - This was on the homepage, so I adjusted the a tags to look like button, then adjust the viewports again.
  * "Stray start tag div." - on Home.html. I could not find any stray tag.
  * "Element li not allowed as child of element nav in this context." - redid the offending bottom navbar

2. I used https://jigsaw.w3.org/css-validator/ to validate the CSS:

  * The CSS returned some errors to do with bootstrap.min.css and swiper-bundle.css, none with Style.css"

3. On the recommendation of my tutor, I used https://jshint.com/ to validate the JavaScript:

With jshint, it informed me of the following:
  * 	in cart_quantity.js:
      * 	"'template literal syntax' is only available in ES6 (use 'esversion: 6')."  --> nothing changed.
  
  * in homepage.js:
      * "'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz)." --> nothing changed.
      * "Missing semicolon." - on several lines.  --> Added the semi colons.
      * "	'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6')." --> nothing changed.
      * "'template literal syntax' is only available in ES6 (use 'esversion: 6')." --> nothing changed.
      * "	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz)." --> nothing changed.
  
  * in stripe_elements.js:
      * "'template literal syntax' is only available in ES6 (use 'esversion: 6')." --> nothing changed.

4. I used http://pep8online.com/ to validate the Python code.
    * I got the same errors, repeated several times, usually about lines being too long, for example as shown [here.](https://imgur.com/ZdTBeIz")
5. Google Light House Audit result:
- - - -

Poor performace. The full [report](https://googlechrome.github.io/lighthouse/viewer/?psiurl=http%3A%2F%2Fmilestone-four-andrew.herokuapp.com%2F&strategy=mobile&category=performance&category=accessibility&category=best-practices&category=seo&category=pwa&utm_source=lh-chrome-ext) attributes this to Stripe, and also recommends using different formatting for the images. NB, if you click report, wait a few seconds for Lighthouse to work.
![Imgur](https://i.imgur.com/KEX49Pc.jpg)

- - - -
*8.2 Test cases/ Testing the user goals/stories (section 2):* 
- - - -
Please note that I have chosen to list the screenshots in stead of displaying them, in order to improve legibility of this section.
1. Potential Employer Goals (Readme Section 2.1, 2.2):

* Upon entering the site, users are greeted with a visually attractive and interactive homepage, which establishes the purpose of the site and has a call to action:
      * (register or sign in)
      * go the menu
      The Homepage changes greets a user if they are already signed in.
* The navbar reinforces these options, and introduces new ones from the drop down profile button, and the wishlist next to it

* From the [gitpod workspace](https://pink-slug-4n0r9b0e.ws-eu27.gitpod.io/) potential employers are welcome to view the django Project and applications.

- - - -
[Full screen (1920*1080) homepage](https://i.imgur.com/XCO18Fo.jpg)
- - - -
[Homepage with an iPhone XR](https://i.imgur.com/CHBVEsX.jpg)
- - - -

2. Shoppers:
- - - -
- - - -
* [(Readme Section 2.3) Registration. Full screen (1920*1080)](https://i.imgur.com/aFJYD3M.jpg)

* [(Readme Section 2.3) Registration. iPhone XR](https://i.imgur.com/EYlKzJN.jpg)
- - - -
- - - -
* [(Readme Section 2.4, 2.5) Profile with record of orders placed. Full screen (1920*1080)](https://i.imgur.com/OlczaMG.jpg) Navigate to Profile
* [(Readme Section 2.4, 2.5) Profile with record of orders placed. Full screen (1920*1080)](https://i.imgur.com/TOzuUyq.jpg) View Profile
----
* [(Readme Section 2.4, 2.5)Profile with record of orders placed. iPhone XR](https://i.imgur.com/XoiMYNp.jpg) Navigate to Profile
* [(Readme Section 2.4, 2.5)Profile with record of orders placed. iPhone XR](https://i.imgur.com/I12Cni7.jpg) View Profile
- - - -
- - - -
 
* [(Readme Section 2.6, 2.7) View reviews and CRUD own reviews. Full screen (1920*1080)](https://i.imgur.com/e6qUxrQ.jpg) access the reviews
* [(Readme Section 2.6, 2.7) View reviews and CRUD own reviews. Full screen (1920*1080)](https://i.imgur.com/2rTRjWz.jpg) view all reviews, option to edit or delete
* [(Readme Section 2.6, 2.7) View reviews and CRUD own reviews. Full screen (1920*1080)](https://i.imgur.com/QTWTIm0.jpg) edit a review
- - - -
* [(Readme Section 2.6, 2.7) View reviews and CRUD own reviews. iPhone XR](https://i.imgur.com/8dGRdME.jpg) access the reviews
* [(Readme Section 2.6, 2.7) View reviews and CRUD own reviews. iPhone XR](https://i.imgur.com/5c9Ogsp.jpg) view all reviews, option to edit or delete
* [(Readme Section 2.6, 2.7) View reviews and CRUD own reviews. iPhone XR](https://i.imgur.com/l6BxxEk.jpg) edit a review

- - - -
- - - -
* [(Readme Section 2.8) View the store. Full screen (1920*1080)](https://i.imgur.com/kl0Axmy.jpg) store general
* [(Readme Section 2.8) View the store. Full screen (1920*1080)](https://i.imgur.com/kImdWcR.jpg) detailed view of product
- - - -
* [(Readme Section 2.8) View the store. iPhone XR](https://i.imgur.com/DHkwEaN.jpg) store general
* [(Readme Section 2.8) View the store. iPhone XR](https://i.imgur.com/l1OoDsH.jpg) detailed view of product
- - - -
- - - -
* [(Readme Section 2.9) View the cart. Full screen (1920*1080)](https://i.imgur.com/EAsNsvs.jpg)

* [(Readme Section 2.9) View the cart. iPhone XR](https://i.imgur.com/JvzPOab.jpg)
- - - -
- - - -
* [(Readme Section 2.10, 2.11) Pay easily, and have payment details secure. Full screen (1920*1080)](https://i.imgur.com/cuTsFMV.jpg)

* [(Readme Section 2.10, 2.11) Pay easily, and have payment details secure. iPhone XR](https://i.imgur.com/tChhZvv.jpg)
- - - -
- - - -
* [(Readme Section 2.12) Wishlist. Full screen (1920*1080)](https://i.imgur.com/xXkfCK8.jpg) go to wishlist - done from Profile and navbar
* [(Readme Section 2.12) Wishlist. Full screen (1920*1080)](https://i.imgur.com/fWKoDzK.jpg) add to wishlist - done from the store and product detail pages
* [(Readme Section 2.12) Wishlist. Full screen (1920*1080)](https://i.imgur.com/AeCUdtt.jpg) what the wishlist looks like  
* [(Readme Section 2.12) Wishlist. Full screen (1920*1080)](https://i.imgur.com/rJXwy5W.jpg) remove an item from the wishlist
- - - -
* [(Readme Section 2.12) Wishlist. iPhone XR](https://i.imgur.com/LusRr9u.jpg) go to wishlist - done from Profile and navbar
* [(Readme Section 2.12) Wishlist. iPhone XR](https://i.imgur.com/Svy9drD.jpg) add to wishlist - done from the store and product detail pages
* [(Readme Section 2.12) Wishlist. iPhone XR](https://i.imgur.com/apFP3mO.jpg) what the wishlist looks like  
* [(Readme Section 2.12) Wishlist. iPhone XR](https://i.imgur.com/21O2rvL.jpg) remove an item from the wishlist
- - - -


3.Admin/Super users
- - - -

4. Admin user:
When logged in as Admin/ superuser, the user can add, edit, delete products, and edit/delete all reviews
(Readme Section 2.13 --> 2.18)

- - - -
* [(Readme Section 2.13) CRUD Reviews (1920*1080)](https://i.imgur.com/RE4E8rb.jpg) Admin can edit/delete any review
* [(Readme Section 2.13) CRUD Reviews. iPhone XR](https://i.imgur.com/J9KyHtl.jpg) Admin can edit/delete any review
- - - -
- - - -
* [(Readme Section 2.14-->2.16) CRUD Products (1920*1080)](https://i.imgur.com/c34RxXY.jpg) Go to Add Product (Manage Products)
* [(Readme Section 2.14-->2.16) CRUD Products (1920*1080)](https://i.imgur.com/p0JBQrr.jpg) Add Product Form
* [(Readme Section 2.14-->2.16) CRUD Products (1920*1080)](https://i.imgur.com/KDWQmCL.jpg) Admin can edit/delete any product
- - - -
* [(Readme Section 2.14-->2.16) CRUD Products. iPhone XR](https://i.imgur.com/hA5T3CD.jpg) Go to Add Product (Manage Products)
* [(Readme Section 2.14-->2.16) CRUD Products. iPhone XR](https://i.imgur.com/Qxt0yga.jpg) Add Product Form
* [(Readme Section 2.14-->2.16) CRUD Products. iPhone XR](https://i.imgur.com/PFpV7TR.jpg) Admin can edit/delete any product
- - - -
- - - -
(Readme Section 2.18): Security
- - - -
All pages were tested to ensure access rights. First, as a non-admin, e.g. User A, check that can add, edit, delete own reviews, then that a non-logged in/User B cannot target User's A content. Then check, by using the raw urls, that the website redirects the user.
- - - -
*8.3 Bugs and Bug Fixing:* 
- - - -
There were numerous challenges using so much Django.
1.	App would not deploy on Heroku.
    * **Fix:** The config vars need to be exact. Errant commas or quotation marks stop the process working.
    * **Fix:** Care needs to bew taken linking to services such as AWS, whitenoise, pyscopg2 etc.
   


2.	Admin would not work in Django 4.0 as needed csrf token.
    * **Fix:** add `CSRF_TRUSTED_ORIGINS = ['https://*.GITPOD.IO','https://*.127.0.0.1']` in settings.py, to tell Django to allow anything from Gitpod.


3.	Getting a javascript file to access a Django variable
    * **Fix:** [Quora](https://www.quora.com/How-does-one-access-Django-template-variables-in-JavaScript) put the Django variable inside a script tag and place that in the html file that loads the js.


4.	Could not get js function to update cart loading
    * **Fix:** Solution – wrap it inside window.onload = function () NB - I moved away from this method in the end as the code was starting to look messy.


6.	js function to update cart threw up csrf tokens.
    * **Fix:** Solution [here](https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax) NB - I moved away from this method in the end as the code was starting to look messy.


7.	JS function would not post the update cart form using fetch.
    * **Fix:** It turned out the offending error was an extraneous /. Instead of var url = 'update_item/' I had var url = '/update_item/' which caused it to get a Django 404 error. 
NB, I abandoned this method of updating the cart, in favour of the method presented by Code Institute in their videos.



8.	Javascript in postload block would not load.
    * **Fix:** the post load block needs to sit inside the endblock that signifies the end of the page, and not like in the CI videos.


9.	In base.html, the CI code used to call the toasts `<script type="text/javascript">$('.toast').toast('show');</script>`
 would not work.
    * **Fix:** Use this instead:
` <script type="text/javascript"> `
     `$(document).ready(function() {`
        `$(".toast").toast('show');`
    `});`
</script>



10. Linking stripe variables to a settings variable, itself linked to the gitpod environment variables, stopped stripe from working. In other words, doing the actions of CI video Stripe – Part 4 and 5.
    * **Fix:** At the top of the checkout view, instead of:
   ` stripe_public_key = settings.STRIPE_PUBLIC_KEY `
    `stripe_secret_key = settings.STRIPE_SECRET_KEY `
use:
`stripe_public_key = "the actual key from Stripe"`
`stripe_secret_key = ' the actual key from Stripe '`


11. Toasts would not close when clicking the x button.
    * **Fix:** instead of :
  ` <button type="button" class="ml-2 mb-1 close text-dark" data-dismiss="toast" aria-label="Close"><span aria-hidden="true">&times;</span></button> `
Use 
` <button type="button" class="btn-close close-toast" data-bs-dismiss="toast" aria-label="Close"></button> `

This was due to CI code being in Bootstrap 4 but me using Bootstrap 5.


12. Test webhooks from Stripe were not working.
    * **Fix:** Gitpod server (8000) needs to be set to public. Solution found on Slack.

13. Use of webhooks broke the functionality of the website, specifically being able to post orders.
    * **Fix:** Revert git commits to last known working configurations, use print and console logs, and lots of internet sleuthing, to get website working again

14. Heroku deployment did not use my static files.
    * **Fix:** I used Django-Heroku at first, and then AWS.

15. If a user selected multiple items in the store page and then clicked add to  wishlist, multiple copies of the item would be added to the wishlist, and when deleting from the wishlist, the app would throw an error, as get was supposed to find one, but instead found x items.
    * **Fix:** As admin, delete the offending instances. Then, in wishlist views.py, add quantity=1 to the following:
`product = Product.objects.get(pk=product_id, quantity=1)`

in the views add_to_wishlist, remove_from_wishlist


16. Heroku applied a database update which locked me out of my local database, and I could not run a local server.
    * **Fix:** The internet says to [update the pg_hba.conf file](https://www.postgresql.org/docs/9.5/auth-pg-hba-conf.html) however this is stored by Heroku, and I could not access it. I had all functionality in my project except reviews by this point, so I simply rebuilt the project in a new repo. As most of the code was similar, it was a case of revising things and updating/tidying up. It took a bit of time, but avoided nasty errors and edge cases.

17. Related to the last, Heroku applied another update, during which their database was read only, but I had a model registered, which I could then not update, putting the project at a dead end.
    * **Fix:** As above – start anew

18. Emails were not configuring properly.
    * **Fix:** As was in new project at this point (due to Heroku database issues) I consulted [Django for Beginners](https://djangoforbeginners.com/introduction/) and secured my env variables as discussed in chapter 16, then set up my emails as discussed in chapter 12, using [SendGrid](https://sendgrid.com/)I then tested this by signing my partner up to the website, and checking to see if the verification email worked. Upon confirmation I then had to log in as the superuser and set her email as verified, as the website was not yet live.  I used a second email account of mine to set up a new user, and test the email that way on the live (i.e. Heroku app) website, and it worked, as shown. ![below](https://i.imgur.com/teyjVZ5.jpg) Also, please note I consulted tutor support to try and fix this, but after they confirmed all the variables were correct, still no joy.

    Please note the dates because of the next error:

19. Heroku applied another database update, and this stopped the deployed app from doing anything with emails. The local server still worked.
    * **Fix:** Due to timie constrainsts, I opted out of rebuilding the website, and instead set allauth to not require emails verifications.

20. No email confirmations of orders.
    * **Fix:** As emails not working, not much to do here. However, users still have the order history in their profile.

21. Using a database variable threw up the following error: 
        "connection to server at "ec2-63-34-223-144.eu-west-1.compute.amazonaws.com" (63.34.223.144), port 5432 failed: FATAL:  no pg_hba.conf entry for host "34.76.72.103", user "ruierkmjrmkfsf", database "d2lop4oummigm", SSL off."
    * **Fix:** Given the effort already expended wrestling with Heroku, I instead chose to leave the database as a string in settings.py. This was the only way to get it to work.

22. Could not delete orders in the admin panel.
    * **Fix:** In the Orders model, line 58 checkout/models.py:
`self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] `
add: "or 0" to the end, so it reads:
`self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0`

23. Setting debug to false or `DEBUG = os.environ.get('DEVELOPMENT')` ruins the local server display, I assume because the static files were affected by the AWS settings on line 217 + in settings.py
    * **Fix:** Leave it on true for now, put a giant note on desk to set to false for Project Deployment

24. Order totals not showing up on deployed website. See below:
- - - -
Placing an order on Heroku:
![Imgur](https://i.imgur.com/L72mo9D.jpg)
- - - -
Order confirmation on Heroku.
![Imgur](https://i.imgur.com/Qlaf9lr.jpg)
- - - -
Placing an order on the local server:
- - - -
![Imgur](https://i.imgur.com/WORiJcR.jpg)
- - - -
Order confirmation on the local server:
- - - -
![Imgur](https://i.imgur.com/4N8suNI.jpg)
- - - - 
Both orders are being registered, and they also register on Stripe
- - - -
![Imgur](https://i.imgur.com/UabgXtn.jpg)
    * **Fix:** As best as I, and Slack, can tell, this is an issue with signals. However, I have not been able to isolate it.
- - - -
*8.4 Supported screens and browsers:* 
- - - -

There are screenshots, available in the screenshots folder, that show the website working at Fullscreen, and also at example mobile (iPhone 8) viewports.

As there are several screenshots, rather than link them individually, I have linked the containing folder:

[Screenshots](https://github.com/ANDREWAHN-UK/Milestone-Three/tree/main/static/screenshots)

Additional testing on the view ports was done using [Multi Device Mockup Generator](https://techsini.com/multi-mockup/).

I used Opera, Edge, Firefox and Chrome, and tested these, along with general usability, using the dev tools there.

Dev tools in Chrome are accessed by *right click + inspect + toggle device toolbar + select various devices*.

In Opera *right click + inspect + toggle device toolbar + select various devices.*

In Firefox, *right click + responsive design mode (ctrl+shift+m) + select various devices.* NB that Firefox displays this all at the bottom, not the right side like the others.

In Edge *right click + inspect + toggle device emulation + select various devices.*

The procedure for testing was as follows:

1.	In style.css set up media queries for the viewports, in descending order (i.e. starting with 991px --> 767px --> 600px -->480px --> 425px -->280px)

2.	introduce a new element, or change, e.g. a "Review Button."

3.	style it for the desktop, using dev tools and style.css.

4.	when happy with this, use dev tools for the various viewports (e.g. iPad Pro.)

5. If the screen looks ok, leave alone. If not, adjust those elements using the media queries discvussed in Point 1.

6.	Repeat for each element and page, e.g. styling the height and width of containers, as discussed in 8.3.4.

6.	Save changes via GitHub commit and push.

7.	Open up website on mobile device. I have an Oppo X2 Lite and Kindle Fire, my sister has an iPhone 8 and my partner a Galaxy A21.

Further testing was done with friends and family, and by submitting the code for peer review on slack, using fresh eyes to test the UX, most notably ease of navigation between pages, and visibility of text against coloured backgrounds.

Results of this testing led to a **considerable** number of viewport adjustments, the majority of which was adjusting the behaviours of the various containers, as discussed in 8.3.4.