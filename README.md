# Milestone Project Four
<a href="https://imgur.com/Ew5GK6g"><img src="https://i.imgur.com/Ew5GK6g.jpg" title="source: imgur.com" /></a>
 - - - -

**Website:**
You can view the deployed website [here](https://milestone-four-andrew.herokuapp.com/)
 - - - -
- - - -

**1. Purpose of the project:**
 - - - -
This project is an e-commerce website created for educational purposes. The target audience is anyone who likes Hamburgers.

Simply put, this project came about because I like hamburgers, and have entertained the idea of a website/restaurant where someone could customise their burgers, and to broaden the concept of Hambirgers, away from the cheap/generic stuff like MacDonald's, and away from the pricey, not good value for money venues like [Byron Burger](https://www.byron.co.uk/). In other words, Subways, but for burgers, with a healthy dose of [Hans Im Gluck (awesome German burger chain.)](https://hansimglueck-burgergrill.de/)

I enjoy making and eating hamburgers, and this is the sort of establishment I would patronise.

The original plan was for a gamified burger creation, using Javascript, to mimic how in Subway you choose your base sub, then add whatever topping you want. Users would select a patty, then a bun. The complicatioon came in offering users the ability to select multiple patties, extra topping s etc - it quickly became obvious that there would be a huge amount of clicking, and the ensuing ordser would have been confusing to read, e.g. "3 patties, 1 blue cheese, 2 cheddar, brioche bun."

This could still work, but I shelved that in favour of a simpler, easier to understand and, most importantly, easier to implement set menu.

In a bricks and mortar establishment, it would work very well.


- - - - 
**2. User Goals/stories**
 - - - -
1. As a **Potential Employer** for a Coding Role, I want to view Andrew’s website, to see how he performs as a Full stack developer. I want to be able to navigate the website and compare it to others, of similar scope.
2. As a **Potential Employer** for a Coding Role, further to the above, I would be particularly interested in the use of Python and Django in this website.
3. As a **site user**, I want to easily register for an account, so that I can have a personal account and view my profile.
4. As a **site user**,  I want to have a profile, so that I can view my order history, delivery and payment details.
5. As a **site user**, I want to be able to view other reviews.
6. As a **site user**, I want to be able to create, update and delete my own reviews. 
7. As a **shopper**, I want to be able to view a list of burgers, so I can choose one/many.
8. As a **shopper**, I want to be able to view my shopping bag/cart, so I can keep track of my order and cost, and adjust quantities etc
9. As a **shopper**, I want to be able to view pay without any fuss, so I can check out quickly, and get my burgers
10. As a **shopper**, I want a record of orders placed
11. As a **shopper**, I want my payment info to be securely kept, so I do not need to worry about safety.
12. As a **shopper**, I want to be able to store interesting products in a wishlist, which I can view later and from which I can purchase items.
13. As an **store owner/super user** I want to be able to update and delete other peoples' reviews and profiles.
14. As an **store owner/super user** , I want to be able to add new products, so I can take advantage of market trends and holiday specials. E.G. there is a burger here called the Eirann, which I put in as a St.Patrick's day idea, but I like the sound of it so much I put it as the very first thing users see.
15. As an **store owner/super user** , I want to be able to edit/update products, for example using different images or adjusting the price.
16. As an **store owner/super user** , I want to be able to delete products, if they are not selling.
17. As an **store owner/super user** , I want to be able to access the database, so I can easily see what is (not) selling, and identify patterns/trends, e.g., many sales from a particular neighbourhood.
18. As an **store owner/super user** , I want to be able to keep the site secure by only allowing authorised users to access certain areas of the site.

 - - - - 
**3. Stakeholder Goals**
 - - - -

 * To lead the user to create a profile 
 * To lead the user to read and leave reviews.
 * To lead the user to read and leave a wishlist.
 * To lead the user to purchase items.

- - - - 
**4. Typography and colour scheme:**
 - - - -
*	Font - Lato. For the simple reason that it worked well in previous projects, so I saw no need to deviate.
*	Icons - very few icons were used here. I used font awesome for the icons.
*	Colours – I want the focus to be on the products, so I used black, white and yellow for the header and footer, and white throughout most of the website. On the Homepage, I used colours appropriate to the burgers being highlighted, e.g. grey (representing urban)
*	Images – I sourced the images from google images, [Unsplash](https://unsplash.com/s/photos/burger), [Pixabay][https://pixabay.com/images/search/burger/), [Pxhere](https://pxhere.com/en/photos?q=burger&search=) and [Pexels](https://www.pexels.com/search/burger/)

 - - - - 
**5.A Features:**
 - - - -
1. Feature - Header/Navbar basic - to consist of links to:
* the home page;
* the burger menu page; 
* Profile management[(Product Management (for Super User); Manage Profile (logged in users); Log out (logged in users); Review a Burger (logged in users), Read All Reviews (all users), Go to Wishlist, Register and Log in (new/logged out users)]; 
* the wishlist;
* the cart, with a display of the £ amount so far

The navbar is quite traditional, as the intent is to direct user attention to the products.

2. Feature - Footer – Link to Home Page, link to social media

3. Minimal Viable Project is :
    1. Navbar basic
    2. Homepage
    3. Store page
    4. User profile Page (once logged in)
    5. Reviews page (i.e. view all reviews)
    6. Register/Login/Logout functionality
    7. (Create /Read /Update/ Delete) own Reviews function
    8. Admin to be able to modify all reviews
    9. Checkout page with Stripe functioning
    10. User notification of order placed
    11. Order history
13. Future features/expanding the website :
    1. Expand with different burgers
    2. Add a blog feature, discussing, for example, how burger recipes are decided upon
    3. Add a comments feature to the blog
    4. Create a series of videos, to complement the blog, for use on Youtube, Facebook etc
    5. Host competitions themed around burgers
    6. Add an about us page
    7. Add a contact us form
    8. Add a page like pinterest or imgur, just for burger related (user submitted?) images
    9. the Homepage is made statically, with the text side having to match the appropriate image. This could be done in Django, with, possibly (?) 2 for loops, one to go through the images and the other to go throw the descriptions. Can 2 for loops that reference the same model work?
    10. A more fleshed out User Profile page, specifically with the user's reviews and wishlists viewable and editable directly from here, instead of the current links used. 
    11. A search function for the Admin to go through Users, Reviews, Products could be helpful, if the number of users increases significantly.
    12. Expand the wishlists so users can views those of other people.
    
 - - - - 
**5.B  Structure:**
 - - - -

 Here follows a brief overview of each app within the website, with detail on the html pages and models used.
1. Home App:
* HTML files:
  * home.html
    * This is the landing page. The effect here is a vertical slider, to provide some interactivityas opposed to a more traditional and static Homepage. USers can click up or down, changing the images and the descriptive text of a selection of Hamburgers.
* Models:
    none

    

2. Store App:
    * This main effort here is the store page, where users can select burgers and interact with review and wishlists.
* HTML files:
    * add_product.html:
        * allows super users to add new products to the database

    * edit_product.html:
        * allows super users to edit existing products in the database

    * product_detail.html:
        * allows all users to brung up more information on the chosen burger, and to add a chosen quantity to the cart, and to add the burger to the wishlist

    * review_create.html:
        * allows registered users to write a review

    * review_delete.html:
        * allows users to delete their reviews, and super users to delete any review

    * review_edit.html:
        * allows users to edit their reviews, and super users to edit any review

    * reviews.html:
        * a page to hold all existing reviews. If the user is the author of a review (or is a superuser) this is where they can edit/delete reviews

    * store.html:
        * a page to display the products, where users can click on the image to bring up the product detail. On this page, users can add a product to their wishlist

* Models:
    * Category:
        * stores the Product categories, which are for internal use, e.g. if something is a bun, a patty, cheese or a complete hamburger
    
    * Product:
        * holds the information of what comprises a product here, which gets accessed elsewhere, e.g. product name and image, which are shown in store.html

    * Review:
        * A model of the review, with information to be displayed, such as the product being reviewed, the review author etc. 

   

3. Cart:
    * The cart page acts as the nexus between the store app + pages and the checkout app + pages
* HTML files:
    
    * cart.html
        * allows users to view all items in their cart, and complete their purchase.NB there is also a template tag, labelled cart_tools.py, and a file labelled contexts.py, which are to allow cart functionality throughout the website
* Models:
    None

    

4. Checkout:
    * The checkout is intended to mimick a real life checkout in a supermarket, or a take away restaurant.

* HTML files:
    * checkout.html
        * this acts as a final stop for the user to confirm their purchase, input their credit/debit card details and their delivery details - this last gets saved to the profile if the user clicks the save info box.
    * checkout_success.html
        * This page confirms the order has been placed, and records the order number and details. The same information can be accessed from the profile
* Models:
    * Order
        * states the info needed to comprise an order, and is created when the user confirms their purchase
    * Order Line Item
        * specifies the products that form part of the order, i.e. which products are added to the shopping cart

5. Profile:
    * The Profile page holds default delivery information, which can be edited by the user, as well as their order history, and links to their wishlist and the reviews page. It can only be accessed by the logged in user, or the super user. I.E. User A cannot access User B's profile, unless User A happens to be a super user.

* HTML files:
    * profile.html
        * This holds the user profile
* Models:
    * User Profile
        * this stores information on each user. This info is accessed on the checkout form to pre-fill the delivery data

6. Wishlist:
    * The wishlist is intended to mimick what Amazon have, where by a user can save a product they wish to look at, maybe buy later, or to maintain several products for comparison purposes, which is something I often do on Amazon. The utility scales with the number of products. As the burger site expands, the utility here will increase. The functionality is similar to that of orders.

* HTML files:
    * wishlist.html
        * a page to hold the users wishlist. Currently, wishlists are only visible to their creators. In the future this could change.
* Models:
    * Wishlist
        * similar to the order model, this defines the wishlist in its entirety
    * WishlistItem
        * similar to the OrderLineItem, this defines which items are held in the wishlist.

- - - - 
**6. Wireframes:**
- - - -
The wireframes can be accessed from the "wireframes" folder, and also directly here:

 [Wireframes file](https://github.com/ANDREWAHN-UK/Milestone-Four/blob/main/ms4.bmpr)

 [Wireframes PDF](https://github.com/ANDREWAHN-UK/Milestone-Four/blob/main/ms4.pdf)

- - - - 
 **7. Technology.**
- - - -
Languages Used:
 * HTML5
 * CSS3
 * JavaScript
 * Python 3.8

Frameworks, Libraries & Programs Used:
1.	Bootstrap 5:
    *	Bootstrap was used to assist with the responsiveness and styling of the website.

2.	Django:
    *	Used to create the web app.

3.	Sqlite3 and Postgres:
    *	Used to create the database, initially through Django and then through Heroku.

4.	Jinja:
    *	Used for templating, for loops and conditionals within Django.

5.	Google Fonts:
    *	Google fonts were used to import the 'Lato' font into the style.css file which is used on all pages throughout the project.

6.	Font Awesome:
    *	Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

7.	jQuery:
    *	jQuery came with Bootstrap, used to make the cards work.

8.	GitPod
    *	Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

9.	GitHub:
    *	GitHub is used to store the projects code after being pushed from Git.

10.	Balsamiq:
    *	Balsamiq was used to create the wireframes during the design process.

11. Stripe:
    * Used to facilitate payments, and webhooks.

- - - - 
**8. Testing.**

Please refer to the separate [TESTING.md](https://github.com/ANDREWAHN-UK/Milestone-Four/blob/main/TESTING.md) file.
- - - - 
**9. Deployment.**
- - - - 
The website has been deployed on
  *	Heroku.

  9.1 Deploying to Heroku:

    1. You will need an account to sign up to [Heroku](https://www.heroku.com)
    2. Once logged in click the create new app button
    3. Select the region closest to you and give the APP a name. It is a good idea to name the App something similar to the Github repository which hosts the files.
    4. You will see a navbar on Heroku, starting with Overview, and ending with settings. Click the 3rd button, deploy, and in the middle of the page, where it says "deployment method," select "Connect to Github."
    5. Underneath that, with the tab labelled "Apps connected to GitHub," ensaure that your respository is selected.
    6. Take note of the tab below , labelled automatic deploys. Do NOT click this yet.
    7. First, go back to the navbar and click settings.
    8. Then click "Reveal Config Vars"
     9. Now fill in the fields, which need to be exactly as they are in your env.py file, minus the "". Be careful here. 
    10. Next, check your Procfile is set up correctly. It should read something like this: "web: python app.py"
    11. Now, referring back to step 6, click enable automatic deploys
    12. If done right, at the top right of the webpage, click "open app," and your website should deploy.

 9.2. Github.

 Github is the preferred version control and hosting website of the Coding Academy. For this project, it is not used to deploy the website, but to host it. Therefore, previous advice  and steps regarding creating a fork/backup apply, see below.

 **To create a fork/backup:**

GitHub does not currently allow you to directly fork your own repo, but there is a workaround:

  1.	make a note of the URL of your repo, e.g., "https://github.com/ANDREWAHN-UK/Milestone-Three"
  2.	at the very top right of the page, next to your login image and the bell icon, there is a + button, click this.
  3.	click "import repository”.
  4.	Where it says, "Your old repository’s clone URL," put in the URL of your repository, e.g., "https://github.com/ANDREWAHN-UK/Milestone-Three"
  5.	In the "repository name field" choose an appropriate name for your new repository
  6.	Click "begin import"
  7.	You now have a copy of your original repository, with all commit history and branches!

However, be aware that this is not a real fork, and so you cannot do pull requests back and forth.

Because this effectively clones the repo, I decided against using the actual clone feature, but information on that can be found [here:](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

- - - - 
  **10. Credits**
- - - - 
**Code:** 
Done by myself, with:
 * some work done by [Bootstrap,](https://getbootstrap.com/) most notably using grids and columns, and the built in card feature.
 * Inspiration from [Django For Beginners 4.0](https://djangoforbeginners.com/introduction/) specifically Chapter 12 (Emails,) Chapter 13 (Article App - used as the basis for the reviews) and Chapter 16 (Deployment).
 * [Code Institute,](https://learn.codeinstitute.net/login?next=/dashboard) namely the Boutique Ado Project leading up to Milestone 4. This formed the basis of the project.
 * Code from Brian Traversy at [Udemy,](https://www.udemy.com/course/50-projects-50-days) "Vertical Slider" project, which formed the homepage, albeit then heavily modifed for the site purposes.
 

**Content:**

All done by me, with ideas and inspiration for input fields and layout from the following:
 *	Code Institute slack community - seeing what people were doing -and importantly what they were NOT doing- for the 4th Project was a very useful steer in terms of understanding the scope
 *	[Dennis Ivy](https://dennisivy.teachable.com/p/django-beginners-course) for context on organising apps, and Django in general.
 *	[Django For Beginners 4.0](https://djangoforbeginners.com/introduction/) which was a beginner friendly way to understand Django. I very nearly switched to a blog app, but decided to save that for the future.
 *	[5 Guys Burgers](https://fiveguys.co.uk/menu/) for ideas on colour scheme and simplicity, consistency -they repear white and pink throughout the website
 * [The Cherry Cricket](https://cherrycricket.com/food-menu) for a simple and effective burger website, and which I will visit, one day!
 * [FreshGround Coffee](https://freshground.co.uk/our-coffee/) for ideas regarding a coffee website, which was something I considered.

**Media:**

 * [Unsplash](https://unsplash.com/s/photos/burger) for some of the images used.
 * [Google](https://www.google.com/)  for other images.
 * [Pixabay](https://pixabay.com/images/search/burger/) for some of the images used.
 * [Pxhere](https://pxhere.com/en/photos?q=burger&search=) for some of the images used.
 * [Pexels](https://www.pexels.com/search/burger/) for some of the images used.



**Acknowledgements:**
* Code Institute slack community
* Code Institute tutor support (whilst doing the build up lessons, I ran into some quite severe issues with using Python and Flask, that had I not fixed then, would have derailed the Project)
* Code Institute mentor (Rohit Sharma)
* [StackOverflow](https://stackoverflow.com/) - for various fixes