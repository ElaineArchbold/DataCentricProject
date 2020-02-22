## Elaine Archbold Data Centric Milestone Project

For this project, I created a website around the book ‘Mrs Hinch, the Activity Journal’. ‘Mrs Hinch’ is Sophie Hinchliffe. She has a huge online following, particularly on Instagram and YouTube. She is ALL about cleaning. She shares cleaning tips and hacks with her followers, and has released a book, and now an Activity Journal where people can write down their to-do lists, shopping lists and cleaning tips or hacks. 


## UX
My goal in the design was to create a very user friendly site where users could access everything to do with Mrs Hinch in one place. 

I kept the Navbar and footer simple, and the lightbox on the inspiration page gives an overall gallery view before an image is selected, which is when the lightbox effect kicks in. The images used are from unsplash.com, but these could be replaced with professional photos of Mrs Hinch’s home.

*User A – wants to create their tailor made Mrs Hinch shopping list, and either print it to take it shopping with them, or use the app while they are out and about. On the home page, as you scroll past the opening paragraph, there is a shopping list containing all of the Mrs Hinch must-have items. 

*User B – wants to create and up-date an online cleaning to-do list. In the To-Do page, I have created a To-Do list, using MongoDB where the user can add, edit, update and remove items from their to-do list. They can use this list directly on the website and edit it as they go. There is also a tab for checking completed tasks so they can see what they have done.

*User C - wants to search for tips for cleaning. On the tips page, there are the most popular Mrs Hinch YouTube videos. I have also wired up a search bar to take users directly to her YouTube channel to search through her full collection of videos.

The site can be viewed through Heroku: https://hinching-journal.herokuapp.com/home

I created Wireframes of how I wanted the site to look before starting. See below:
![Desktop View1](static/images/homepage.png)
![Desktop View1](static/images/todolist.png)
![Desktop View1](static/images/tips.png)
![Desktop View1](static/images/inspiration.png)


## Features
### Existing Features
The HOME page features a scrolling parallax effect, with three sections. Section one is an introductory paragraph from Mrs Hinch, taken from her book introduction. Section two is a shopping list, where users can select the most popular Mrs Hinch items that they may need to stock up on. Section three contains iframes for YouTube and Instagram. The Instagram feed could be added here, with login details from Mrs Hinch.

The TO-DO page uses a MongoDB database to allow the user to add, edit, update and remove items from their to-do list. They can use this list directly on the website and edit it as they go. There is also a tab for checking completed tasks so they can see what they have done.

The TIPS page has a video gallery of the most popular Mrs Hinch YouTube videos. I have also created and wired up a search bar which brings users directly the Mrs Hinch YouTube channel. I used Google developer tools on YouTube to find the correct code for this.

I also created a favicon in Photoshop which can be seen on the browser tab and can further be used for social media branding.


### Features Left to Implement
With the Mrs Hinch login details for Instagram, I would be able to replace the Instagram iframe on the home page with her Instagram feed.


## Technologies Used
1.	GitPod IDE
2.	HTML
3.	CSS
4.	Bootstrap (4)
5.	Materialize
6.	Photoshop
7.	Python
8.	Flask
9.	MongoDB
10.	Jquery
11.	PyMongo
12.	Jinja
13.	Google Fonts
14.	Font Awesome



## Testing
LINKS – I have tested all links. The email and Facebook links in the footer go those platform homepages. All other links go to the relevant accounts.

I used Google Developer Tools to check the responsiveness of the site. The Navbar and footer are responsive and reduce on smaller screens. I have used media queries throughout to allow for better UX on mobile devices.

The site had been tested on Chrome, Firefox and Safari.

I used the Heroku link to check the site on my phone, where I discovered some discrepancies between what was shown in developer tools and what was actually showing on the live site. This allowed me to fix these issues to ensure that the live site would look how it should.

All HTML was checked on the W3C Mark-up Validation Service.

The CSS was checked on the W3C CSS Validation Service.

All HTML was formatted on https://freeformatter.com.

Screenshots of the responsive design can be seen here:

![Desktop View1](assets/images/responsivedesign.jpg)


## Deployment

I have set Heroku to link to GitHub, so each push to GitHub also pushes to Heroku.
I have set the IP and PORT as below, and saved the MongoDB URI details here also. I used an env.py file to save the MongoDB URI in GitPod and imported this to app.py so that the details were not on view to anyone looking at the site on GitHub.

Once the Heroku app is created with the details below, you click on ‘open app’ and you can view the site.

To run this project on your own IDE:

Download a copy of the file from GitHub at https://github.com/ElaineArchbold/DataCentricProject.git and open it up in your IDE. The following must be installed on your machine:
- dnspython
- flask
- flask-PyMongo
- pyMongo
- An account with MongoDB Atlas


## Heroku Deployment

1.	Create a requirements.txt file and a Procfile.
2.	Create a new app in Heroku.
3.	In "Settings" > "Reveal Config Vars" and set the IP to 0.0.0.0 and PORT to 5000. 
4.	IP | 0.0.0.0 and your MONGO_URI.
5.	Click Deploy.

## Credits
### Content
The text in the 'about me' section on the home page was taken from the introduction section in ‘Mrs Hinch, the Activity Journal’.

### Media
All of the photos used are from unsplash.com.

I used Photoshop to create the background image for Parallax one. I replaced the background on an image I found of ‘Mrs Hinch’.

### Acknowledgements
The footer and navbar were taken and amended from previous projects.

I found the scrolling parallax tutorial on: https://www.w3schools.com/howto/howto_css_parallax.asp

I found the lightbox snippet on the Portfolio page on: https://epicbootstrap.com/snippets/lightbox-gallery

I found the snippet for the YouTube video gallery on: http://www.prebootstrap.com/bootstrap-template/video-gallery

