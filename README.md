<div align='center'>

# **Surf Matters**

</div>

<p align="center">
    <img width="600" height="400" src="media/surf_matters_readme.jpg">
</p>

## **About**

Surf Matters is an e-commerce store, specialising in Surf Boards and Wetsuits and Surf Lessons.
The site was built with a friend in mind to showcase what an e-commerce store would look like for them as
they are looking to open a surf shop shortly.

Users are able to browse the products, sort by various categories and filter categories into certain products
and subcategory of products. A product details page enable users to view further information on individual products
and add them to their shopping bag to purchase.

There is also a blog page where users can browse submitted articles and leave comments, users are encouraged
to submit articles themselves via email.

Users are able to register for a new account, and once registered they can login and view their default delivery 
information and previous order history.

The deployed website can be viewed here -[Surf Matters](https://adamp-surf-matters.herokuapp.com/)

## **UX**

The website was designed to be responsive and easy to use and navigate. I designed a home page with an image carousel
of various surfing images, with buton links to the products, surf lessons and blog.

The site is easy to navigate, users can use the menu links in the navigation bar at the top of the page,
and each page has a consistent layout to it with the header and footer replicatred across the site. 
this gives users a familiar feel to each page when navigating the site.

I chose black and white as the main colours for the site as the surfing, product and blog images
are quite colourful due to the nature of their content.

### _**Site Goals**_

The overall aim of the site is to enable users to access the online store for the Surf Matters
surf shop. It is designed to be somewhere that Surf Matters can showcase their products online and 
also sell other services they offer to a far wider audience than the just the people who visit their
shop. 

The inclusion of a blog is designed to give the store a community feel, users are encouraged to email in an 
article for the site owner to approve before posting.

### _**Target Audience**_ 

The website is aimed at but not restricted to the following users :

* People wanting to buy surf products.
* People wanting to learn to surf.
* Site owner to increase sales and manage products.
* People wanting to find surf shops local to them.

### _**User Stories**_

| User Story ID | As A/AN            | I want to be able to...                      | So that I can..                                                                |
|---------------|--------------------|----------------------------------------------|--------------------------------------------------------------------------------|
|               |                    | **Viewing and navigation**                   |                                                                                |
| 1             | Shopper            | View all products.                           | Select what I would like to purchase.                                          |
| 2             | Shopper            | View individual product details.             | See the price, product description and any other information about the product.|
| 3             | Shopper            | Add items to a shopping bag.                 | Review what I want to purchase.                                                |
| 4             | Shopper            | View the total of my purchases.              | Avoid over spending.                                                           |
|               |                    | **Registration and User Accounts**           |                                                                                |
| 5             | Site User          | Register for an account.                     | Have a profile with saved details such as delivery address and previous orders.|
| 6             | Site User          | Login and logout.                            | Access my personal information.                                                |
| 7             | Site user          | Receive email comfirmation after registering.| Check that my account registration was a success.                              |
| 8             | Site User          | Recover my password if I forget it.          | Maintain access to my account.                                                 |
|               |                    | **Purchasing and checkout**                  |                                                                                |
| 9             | Shopper            | Select the size and quantity of a product.   | Make sure I purchase the correct product for me.                               |
| 10            | Shopper            | View items in my bag before purchase.        | Check the cost and items that I want to buy.                                   |
| 11            | Shopper            | Amend or delete items in my bag.             | Make changes if I change my mind about certain purchases.                      |
| 12            | Shopper            | Securely make a payment.                     | Be confident my personal details are not shared with anyone.                   |
|               |                    | **Sorting and searching**                    |                                                                                |
| 13            | Shopper            | Sort the list of products.                   | Find the best price or best rated product.                                     |
| 14            | Shopper            | View products by category.                   | View specific products that I am in interested in.                             |
| 15            | Shopper            | Search for a product by name.                | Find a specific product I am interested in.                                    |
|               |                    | **Admin and Product Management**             |                                                                                |
| 16            | Site / Store Owner | Add a product.                               | Increase the product range I am selling.                                       |
| 17            | Site / Store Owner | Edit a product.                              | Change product prices, descriptions etc.                                       |
| 18            | Site / Store Owner | Delete a product.                            | Remove products that are no longer available.                                  |
|               |                    | **Blogs**                                    |                                                                                |
| 19            | Site User          | Read blog articles.                          | Read about a subject of interest to me.                                        |
| 20            | Site User          | Comment on a blog article.                   | Let the author know how I felt about their post.                               |


## _**Database Schema**_

The databases are stored in [sqlite3](https://docs.python.org/3/library/sqlite3.html) in development, and [heroku postgres](https://www.heroku.com/postgres) in
production. A number of different models are used throughout the site as detailed in the database schema below.

<br>
<p align="center">
    <img width="700" height="500" src="media/Surf_Matters_DB_Schema.png">
</p>
<br>

#### Product model

The product model holds all the information relating to products sold in the store, it has two froeign keys, those being
category and subcategory, and is also a Foreign Key to the OrderLineItem model.

| Field       | Type                |
|-------------|---------------------|
| category    | models.ForeignKey   |
| subcategory | models.ForeignKey   |
| sku         | models.Charfield    |
| name        | models.Charfield    |
| description | models.TextField    |
| has_sizes   | models.BooleanField |
| price       | models.DecimalField |
| rating      | models.DecimalField |
| image       | models.ImageField   |

#### Category and Subcategory models

The Category and Subcategory models are identical, both contain two fields. A name field which is used in the back end. The 
other field is a friendly_name which is used to display the name to the end user.

| Field         | Type             |
|---------------|------------------|
| name          | models.Charfield |
| friendly_name | models.Charfield |

#### Order model

The order model is created in the checkout app, and is used to handle all orders across the site. It takes
the user_profile as a Foreign key to bring across registered users stored details.

| Field            | Type                 |
|------------------|----------------------|
| order_number     | models.CharField     |
| user_profile     | models.ForeignKey    |
| full_name        | models.CharField     |
| email            | models.EmailField    |
| phone_number     | models.CharField     |
| street_address_1 | models.CharField     |
| street_address_2 | models.CharField     |
| town_or_city     | models.CharField     |
| county           | models.CharField     |
| post_code        | models.CharField     |
| country          | models.CountryField  |
| date             | models.DateTimeField |
| delivery_cost    | models.DecimalField  |
| order_total      | models.DecimalField  |
| grand_total      | models.DecimalField  |
| original_bag     | models.TextField     |
| stripe_pid       | models.CharField     |

#### OrderLineItem model

The order line item model is used to create an order line for each product in the shopping bag. It takes in the order as a 
Foreign Key this enable us to access orders and make certain calls on them. It also takes in product as a Foreign Key, which
gives it access to all the associated fields of that model.


| Field          | Type                |
|----------------|---------------------|
| order          | models.ForeignKey   |
| product        | models.ForeignKey   |
| product_size   | models.CharField    |
| quantity       | models.IntegerField |
| lineitem_total | models.DecimalField |

#### UserProfile model

The UserProfile model is used to store a customers default delivery information, and also to provide a record of their
order history. It has **user** as a OneToOneField which specifies that each user can only have one profile,
and each profile can be attached to one user.

| Field                    | Type                 |
|--------------------------|----------------------|
| user                     | models.OneToOneField |
| default_phone_number     | models.CharField     |
| default_street_address_1 | models.CharField     |
| default_street_address_2 | models.CharField     |
| default_town_or_city     | models.CharField     |
| default_county           | models.CharField     |
| default_country          | models.CountryField  |
| default_postcode         | models.CharField     |

#### Blog model

The blog model holds all the data for the individual blogs. The slug field is used to create a URL
for each individual blog item.


| Field   | Type                 |
|---------|----------------------|
| title   | models.Charfield     |
| slug    | models.SlugField     |
| opening | models.TextField     |
| body    | models.TextField     |
| date    | models.DateTimeField |
| image   | models.ImageField    |
| author  | models.Charfield     |


#### Comment model

The comment model is used to add comments to the blog articles.

| Field   | Type                 |
|---------|----------------------|
| post    | models.ForeignKey    |
| name    | models.Charfield     |
| email   | models.EmailField    |
| comment | models.TextField     |
| date    | models.DateTimeField |
| active  | modesl.BooleanField  |

<div align="center">

## **Wireframes**

</div>

### _**Home Page**_
<br>
<p align="center">
    <img width="600" height="400" src="files/wireframes/home_page.png">
</p>
<br>

### _**Registration Page**_
<br>
<p align="center">
    <img width="600" height="400" src="files/wireframes/registration_page.png">
</p>
<br>

### _**Login Page**_
<br>
<p align="center">
    <img width="600" height="400" src="files/wireframes/login_page.png">
</p>
<br>

### _**Products Page**_
<br>
<p align="center">
    <img width="600" height="400" src="files/wireframes/products_page.png">
</p>
<br>

### _**Individual Product Page**_
<br>
<p align="center">
    <img width="600" height="400" src="files/wireframes/individual_product_page.png">
</p>
<br>

### _**Surf Lessons Page**_
<br>
<p align="center">
    <img width="600" height="400" src="files/wireframes/surf_lessons_page.png">
</p>
<br>

### _**Individual Surf Lessons Page**_
<br>
<p align="center">
    <img width="600" height="400" src="files/wireframes/individual_surf Lesson_page.png">
</p>
<br>

### _**Blog Page**_
<br>
<p align="center">
    <img width="600" height="400" src="files/wireframes/blog_page.png">
</p>
<br>

### _**Checkout Page**_
<br>
<p align="center">
    <img width="600" height="400" src="files/wireframes/checkout_page.png">
</p>
<br>

### _**Shopping Bag Page**_
<br>
<p align="center">
    <img width="600" height="400" src="files/wireframes/shopping_bag_page.png">
</p>
<br>

### _**Profile Page**_
<br>
<p align="center">
    <img width="600" height="400" src="files/wireframes/profile_page.png">
</p>
<br>

## **Features**

* **Navigation Bar** - The site features a consistent navigation bar, it uses [Bootstrap](https://getbootstrap.com/docs/4.0/components/navbar/) responsive navbar, it is easy to use and 
collapses down on smaller devices.

* **Search Box** - The navigation bar has a search box, where users can enter search terms to search for relevant products in the store.

* **Product Sorting** - Users have the ability to sort products by name, price and rating.

* **Product Filtering** - Users can filter products by category and subcsategory.

* **Shopping bag** - Users are able to add products to their shopping bag whilst browsing the store. When viewing the bag they can update (i.e. change sizes), or
remove products they no longer wish to purchase.

* **Toast Messages** - The site features [Bootstrap](https://getbootstrap.com/docs/4.3/components/toasts/) toast messages. Users get success messages when performing operations
such as logging in and out and adding products to their bag. Users also reveive error, info and warning messsages. 

* **Account Registration** - Users are able to enter their details and register for an account.

* **Profile Page** - Users get a profile page, which stores their default delivery information and previous order history.

* **Secure Checkout** - User can checkout and purchase goods securely, the site utilises [Stripe](https://stripe.com/gb), a secure online payment
processing facility.

* **Blog Comments** - Users are able to add their comments to the blog articles, using a form at the bottom of each blog article. The comments
are then displayed underneath the article.

## **Technologies Used**

[HTML5](https://en.wikipedia.org/wiki/HTML5) - Used to provide the structure and content of the templates.

[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Provides some of the styling for the site.

[Bootstrap](https://getbootstrap.com/) - Utilised for a lot of the styling of the site such as prodcut card and forms. Also used to make the site responsive.
Bootstrap 4.6 was chosen as Crispy Forms are not available with Bootstrap 5.

[Python](https://www.python.org/) - The main code used in the back end with Django.

[Django](https://www.djangoproject.com/) - A Python web framework used to create the website.

[Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - Used for account authentication, registration and account management.

[Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used for styling the websites forms, to make them match the Bootstrap theme.

[Django template engine](https://docs.djangoproject.com/en/3.1/topics/templates/) - Used as a templating language with Django and Python.

[Stripe](https://stripe.com/gb) - A secure online payment processing facility, used for processing customer payments.

[Sqlite3](https://www.sqlite.org/index.html) - Used for storing the databases when in develoment.

[Heroku Postgres](https://www.heroku.com/postgres) - Used for storing the databases in production.

[jQuery](https://jquery.com/) - USed for functionality of the site such as the Bootstrap carousel and stripe elements.

[Google Fonts](https://fonts.google.com/) -  The site uses the Oswald and Roboto fonts.

[Font Awesome](https://fontawesome.com/) - Used for the icons throughout the app.

[Git](www.github.com) - Used for version control, and tracking changes in the repository.

[Heroku](https://www.heroku.com/) - The platform used to deploy the app.

## **Testing**

A lot of the testing was carried out in develoment, using the developer tools in Google Chrome. I found this the most productive way of testing as I found
that I could fix issues found as I went along. The developer tools also assisted me in testing the responsiveness of the site.

### _**User Story Tests**_

I have created a separate file for the user story tests, you can find them by clicking [here](files/user_story_tests/testing.md).

**The website was tested using a Microsoft Surface Pro on Windows 10, on the following browsers.**

* Google Chrome - Version 88.0.4324.182 (Official Build) (64-bit)
* Microsoft Edge - Version 88.0.705.74 (Official build) (64-bit)
* Mozilla Firefox - 85.0.2 (64-bit)

The site functioned well in all of these browsers. Stripe payments worked correctly. All forms displayed and functioned
in the right way. Images were displayed as they should be, and all items were rendered correctly.

**The app was also tested on a number of devices as listed below.**

* Google Pixel 3 xl using Google Chrome on Android 11.

* Moto E5 using using Google Chrome on Android 8.1.

* Ipad 6th Generation using Safari on IOS 13.4.

* Iphone 11 using Chrome on IOS 14.4.

**I used the following websites for validation of my code**

[HTML validation.](https://validator.w3.org/)

[CSS validation.](https://jigsaw.w3.org/css-validator/)

### _**Issues found in testing**_

1. The Surf Lessons were displaying on the all products page, when they should only be displayed on the Surf Lessons page. To resolve this
I created a category objects filter for the surf lessons in the all_products view. Then created a prdoucts filter to not include the surf lessons.

2. No products were displaying after adding the product filter in the all_products view. This was resolved by changing the products.filter to 
**category__name__exact** instead of **category__name__in**.

3. On the checkout page the processing overlay was appearing on mobile devices after pressing the navbar hamburger link. I realised that 
I hadn't given an ID to the checkout button so the overlay was looing for anything with a class of button. This worked correctly once
this was changed.

4. After logging in with your username and password, a toast message should appear saying succesfully logged in. This was not showing on the site,
howerver when inspecting in Dev tools the HTML elements for the toast message were there. I found that the Bootstrap Jquery for the toast message
was not working fully on the home page. So I copied across the Jquery code to the **postloadjs** on the home page. 

5. The comments form on the blog details page was not responsive, causing the user to side scroll. I resolved this by rendering it as a **crispy form**.

## **Deployment**

Surf Matters was developed using Gitpod as an IDE, Github is used to store the repository and for version control. The website is deployed on 
Heroku.

The following steps are taken to deploy the website.

1. Navigate to my Surf Matters Github repository - <https://github.com/adamparker75/Surf_Matters>
2. Click on the dropdown that says code.

<p align="center">
    <img width="300" height="50" src="files/images/deployment/git_clone.JPG">
</p>

3. A URL is displayed, to clone with HTTPS copy this URL

<p align="center">
    <img width="400" height="300" src="files/images/deployment/git_clone_2.JPG">
</p>

4. Open up your preferred IDE (Integrated Development Environment)
5. Change the directory to the location you want the clone to be made.
6. Type **git clone** and then paste the copied URL from step 3.
7. Press Enter and your local clone will be created.
8. In your Environment variables ensure you add the following.

<p align="center">
    <img width="300" height="250" src="files/images/deployment/env_variables.JPG">
</p>

9. You may have to create a [Stripe](https://stripe.com/gb) account to obtain the public and secret keys.
10. Install the requirements.txt file by typing the following command. <br>
**pip3 install -r requirements.txt**

11. Carry out a migrate with the following command. <br>
**python3 manage.py migrate**

### _**Deploying to Heroku**_

1. In your IDE create a **Procfile** and add the following on the top line. <br>
**web: gunicorn surf_matters.wsgi:application**
2. Commit and push the files to Github.
3. Navigate to Heroku and login. <https://id.heroku.com/login>
4. Click on the new button and then choose create new app.

<p align="center">
  <img width="300" src="files/images/deployment/heroku_deploy.JPG">
</p> 

5. Give your app a name, select a region and then click create app.

<p align="center">
  <img width="400" height="200" src="files/images/deployment/heroku_deploy_2.JPG">
</p> 

6. In the deploy tab of your app, click connect to Github.

<p align="center">
  <img width="300" height="75" src="files/images/deployment/heroku_deploy_3.JPG">
</p> 

7. Search for your repository name, once found click connect.

<p align="center">
  <img width="400" height="75" src="files/images/deployment/heroku_deploy_4.JPG">
</p> 

8. Click the settings tab and then click reveal config vars.

<p align="center">
  <img width="300" src="files/images/deployment/heroku_deploy_5.JPG">
</p> 

9. Add in the following config variables. The same as in your environment variables. The email variables
are taken from Gmail.

<p align="center">
  <img width="400" height="400" src="files/images/deployment/heroku_deploy_6.JPG">
</p>

10. Click back to the deploy tab, choose a branch to deploy and then click enable automatic deploys.

<p align="center">
  <img width="400" height="250" src="files/images/deployment/heroku_deploy_8.JPG">
</p>

11. In the resources tab search for Postgres in add-ons 

<p align="center">
  <img width="400" height="150" src="files/images/deployment/heroku_deploy_9.JPG">
</p> 

12. Choose hobby/dev then click submit order form.

<p align="center">
  <img width="400" height="350" src="files/images/deployment/heroku_deploy_10.JPG">
</p> 

13. Click open app at the top of the page.

<p align="center">
  <img width="300" src="files/images/deployment/heroku_deploy_7.JPG">
</p>

The site is now deployed on Heroku.

### _**Amazon Web Services (AWS)**_

I have hosted the static files and media files for the deployed site in an [Amazon Web Services](https://aws.amazon.com/) **S3** bucket. To store the files,
an S3 bucket needs to be created, the documentation for setting one up can be found [here](https://docs.aws.amazon.com/s3/?id=docs_gateway). You will need to use 
the below code for your CORS configuration when required.

<p align="center">
  <img width="400" height="350" src="files/images/deployment/s3_cors_config.JPG">
</p>

Once the set up is complete you will be given a CSV file titled new_user_credentials. Download this file as it holds the Access_key_ID and the
Secret_Access_key which are needed to add to your Heroku config vars and, development environment variables.

<p align="center">
  <img width="350" height="250" src="files/images/deployment/s3_config_vars.JPG">
</p>

Back in your IDE follow the below steps.

1. Run the following commands. <br>
**pip3 install boto3** <br>
**pip3 install django-storages**

2. Freeze to requirements.txt <br>
**pip3 freeze > requirements.txt**

3. In settings.py add storages to **INSTALLED_APPS

<p align="center">
  <img width="200" src="files/images/deployment/s3_gitpod.JPG">
</p>

4. If not already there the following will need to be added to settings.py

<p align="center">
  <img width="350" height="250" src="files/images/deployment/s3_gitpod_settings.JPG">
</p>

5. In the project root directory create a **custom_storages.py** file and add teh following code.

<p align="center">
  <img width="350" height="250" src="files/images/deployment/s3_custom_storages.JPG">
</p>

6. Commit the changes and push to Github and Heroku.

## **Credits**

### _**Content**_

* The code for the navigation bar was taken from [Bootstrap](https://getbootstrap.com/docs/4.6/components/navbar/).
* The code for the account and bag links was taken from The Code Institute Boutique Ado project.
* The footer was taken from [MD Bootstrap](https://mdbootstrap.com/docs/b4/jquery/navigation/footer/).
* The Bootstrap carousel was taken from [Codepen](https://codepen.io/SitePoint/pen/ZbGwqe).
* The blog templates were taken from [Start Bootstrap](https://startbootstrap.com/template/blog-home).
* The blog comments form was created with help from [Django Central](https://djangocentral.com/creating-comments-system-with-django/).
* Overlay and spinner taken from [JS Fiddle](https://jsfiddle.net/mshaker88/u41rgq3e/).
* Product searching, filtering and sorting was created with help from The Code Institute Boutique Ado project. 
* The wireframes were created with [Balsamiq](https://balsamiq.com/).
* The favicon was created on [favicon-generator](https://www.favicon-generator.org/).
* This project was developed using the Boutique Ado project tutorial as a reference and guide. The code has been customised to fit the purpose of the project.

#### _**Product Images and content.**_

This site is a fictitious e-commerce store built for education purposes. The product images and descriptions however were taken from the following 
surf stores.
* [Tynemouth Surf Co](https://www.tynemouthsurf.co.uk/)
* [Shore](https://www.shore.co.uk/)
* [Boardshop](https://www.boardshop.co.uk/)
* [Surfdome](https://www.surfdome.com/Mens-Wetsuits/sddsl13650.htm)

### _**Media**_

The surfing images for the site were found through [Google](www.google.co.uk) images in the following loactions.

* Surf lesson 1 - <https://www.wavehunters.co.uk/>
* Surf lesson 2 - <https://tilegitsurf.com/en/surf-lessons-tenerife/>
* Surf lesson 3 - <http://sennenbeach.com/surf-lessons/>
* Surf lesson 4 - <https://soulsurfschool.com.au/byron-bay-surf-school-private-surfing-lessons/>
* Surfing Image 1 - <https://www.wavehunters.co.uk/>
* Surfing Image 2 - <https://www.surfline.com/surf-news/>
* Surfing Image 3 - <https://www.boardshop.co.uk/blog/mid-length-surfboards/>
* Surfing Image 4 - <https://www.helpfulholidays.co.uk/blog/10-cornish-beaches-for-surfing/>
* Blog image 1 - <https://www.stevens.edu/news/new-effort-harvest-sustainable-renewable-energy-ocean-waves>
* Blog image 2 - <https://www.livescience.com/38163-where-beach-sand-comes-from.html>
* Blog image 3 - <https://www.rnz.co.nz/news/sport/366883/paige-hareb-closes-in-on-medal-at-world-surfing-games>
* Surf wipeout - <https://www.booksurfcamps.com/news/surfing-wipeout>

### _**Acknowledgements**_

* To my wife **Claire Parker** for helping me test the app.
* To my mentor **Reuben Ferrante** for once again guiding me through this project, and being a fantastic mentor throughout this whole process.