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
|               |                    | **Viewing and navigation**                       |                                                                                |
| 1             | Shopper            | View all products                            | Select what I would like to purchase                                           |
| 2             | Shopper            | View individual product details              | See the price, product description and any other information about the product |
| 3             | Shopper            | Add items to a shopping bag                  | Review what I want to purchase                                                 |
| 4             | Shopper            | View the total of my purchases               | Avoid over spending                                                            |
|               |                    | **Registration and User Accounts**               |                                                                                |
| 5             | Site User          | Register for an account                      | Have a profile with saved details such as delivery address and previous orders |
| 6             | Site User          | Login and logout                             | Access my personal information                                                 |
| 7             | Site user          | Receive email comfirmation after registering | Check that my account registration was a success                               |
| 8             | Site User          | Recover my password if I forget it           | Maintain aceess to my account                                                  |
|               |                    | **Purchasing and checkout**                      |                                                                                |
| 9             | Shopper            | Select the size and quantity of a product    | Make sure I purchase the correct product for me                                |
| 10            | Shopper            | View items in my bag before purchase         | Check the cost and items that I want to buy                                    |
| 11            | Shopper            | Amend or delete items in my bag              | Make changes if I change my mind about certain purchases                       |
| 12            | Shopper            | Securely make a payment                      | Be confident my personal details are not shared with anyone                    |
|               |                    | **Sorting and searching**                        |                                                                                |
| 13            | Shopper            | Sort the list of products                    | Find the best price or best rated product                                      |
| 14            | Shopper            | View products by category                    | View specific products that I am in interested in                              |
| 15            | Shopper            | Search for a product by name                 | Find a specific product I am in terested in                                    |
|               |                    | **Admin and Product Management**                 |                                                                                |
| 16            | Site / Store Owner | Add a product                                | Increase the product range I am selling                                        |
| 17            | Site / Store Owner | Edit a product                               | Change product prices, descriptions etc                                        |
| 18            | Site / Store Owner | Delete a product                             | Remove products that are no longer available.                                  |
|               |                    | **Blogs**                                        |                                                                                |
| 19            | Site User          | Read blog articles                           | Read about a subject of interest to me                                         |
| 20            | Site User          | Comment on a blog article                    | Let the author know how I felt about their post.   


### _**Database Schema**_

The databases were stored in [sqlite3](https://docs.python.org/3/library/sqlite3.html) in development, and [heroku postgres](https://www.heroku.com/postgres) in
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

### Category and Subcategory models

The Category and Subcategory models are identical, both contain two fields. A name field which is used in the back end. The 
other field is a friendly_name which is used to display the name to the end user.

| Field         | Type             |
|---------------|------------------|
| name          | models.Charfield |
| friendly_name | models.Charfield |

### Order model

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
| country          | models.CharField     |
| date             | models.DateTimeField |
| delivery_cost    | models.DecimalField  |
| order_total      | models.DecimalField  |
| grand_total      | models.DecimalField  |
| original_bag     | models.TextField     |
| stripe_pid       | models.CharField     |

### OrderLineItem model



| Field          | Type                |
|----------------|---------------------|
| order          | models.ForeignKey   |
| product        | models.ForeignKey   |
| product_size   | models.CharField    |
| quantity       | models.IntegerField |
| lineitem_total | models.DecimalField |