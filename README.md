# **We Rate Music**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Goals](#goals)
3. [Django Apps](#django-apps)
   - [Users](#users)
   - [Clubs](#clubs)
   - [Seasons](#seasons)
4. [Features:](#features)
   - [Spotify API](#spotify-api)
   - [User Profile](#user-profile)
   - [Settings](#settings)
   - [User Stats](#user-stats)
   - [Discover Playlists](#discover-playlists)
   - [Add Playlists](#add-playlists)
   - [View/Create Clubs](#view/create-clubs)
5. [Future Features/Roadmap](#future-featuresroadmap)
6. [Testing](#testing)
7. [Challenges & Bugs](#challenges—bugs)
8. [Technologies Used](#technologies-used)
9. [Deployment](#deployment)
10. [Creating the Heroku app](#creating-the-heroku-app)
11. [Development](#development)
12. [Credits](#credits)

## **Introduction**

We Rate Music was inspired by a group of friends and a WhatsApp group. We all enjoy listening to music and spend variying amounts of time discussing the importance of music in our lives, and the lives of human beings more generally.

The best way to explain what We Rate Music is, is that it is a "book club" for music; we each curate one playlist based on a set of rules that we discuss beforehand. Basic examples from the past include, "Best for studying" or "Best for a gym workout". And more interesting rulesets such as making a playlist where each chosen song must have an artist featured in the previous chosen song, with the first song of the playlist being a free choice.

Everyone within the WhatsApp group is chosen at random one by one to make their submission and we all have a set period of time to listen to the submitted playlist and rate it out of 10, based on how much we enjoyed it and how well it adhered to the rules given. The scores are arbitrary, but are averaged out for every submission and we have a leaderboard as to who scored the highest in each "Season" (Seasons being the different rulesets).

For some of us it is about chasing a higher score than your fellow friends, and for some of us it is a way to listen to new songs, that you perhaps wouldn't have listened to otherwise.

The application tries to mimic this as best as possible, so keep this in mind when using it. It isn't meant to replace Spotify or make it "better" in any way shape or form.

To access the application, visit the Heroku app [**here**](https://we-rate-music-6240e7e17326.herokuapp.com/).

## **Goals**

The current goals of the app are simple: to replace a WhatsApp group and a clumsy attempt at keeping past scores and submissions on an excel spreadsheet.

In the future of the app I would like to see more and more users use it for the same purpose that me and my friends use it for. I would like to expand the app in a way where users outside of their Club "bubbles" can follow other users they've discovered purely based on their music tastes. And perhaps even have Club on Club competitions, where submissions are anonymous until the very end.

## **Django Apps**

Though the apps primary features are detailed [**below**](#features), here is a quick overview on the Django file structure that is used and an overview on what the different apps do in the grand scheme of We Rate Music.

### **Users**

The "Users" application houses all the logic to add playlists (using the Spotify API) to a user's profile, view and discover new playlists of other users on the application. Users can also add/update their profile and background pictures, as well as add their Spotify username information to be able to initiate a search for their public playlists on Spotify.

### **Clubs**

The "Clubs" application has all the logic to create, view, edit and delete clubs. Within clubs, users can invite members to be a part of their club. Invitations are displayed on users profiles and can be accepted or rejected.

### **Seasons**

Within the "Seasons" application, founders of clubs can create seasons by entering a season title and a short description of what the season theme is. It is within this Django application where users can rate the playlists of their fellow club members and view what playlists were a part of which season.

## **Features**

### **Spotify API**

Public Spotify playlists of a user can be searched and added to their "We Rate Music" profile. The API is currently limited to this information:

- Playlist name
- Playlist album cover image
- Track names within the playlist

As the app grows I would like to include far more utility around the Spotify API, more information on what is on the roadmap can be found [**here**](#future-featuresroadmap).

Users must add their Spotify username to use this feature (found within the accounts tab in their Spotify app/web app). As this feature is an integral part of using the "We Rate Music" app, users without at least a free Spotify account will not be able to use it effectively.

### **User Profile**

Users can sign-up to the application using a username (must be unique) and password.

### **Settings**

- profile/background image
- user id for Spotify

### **User Stats**

### **Discover Playlists**

- search users

### **View/Create Clubs**

### **Add Playlists**

## **Future Features/Roadmap**

## **Testing**

### **Pylint**

### **Process**

## **Challenges & Bugs**

### **Challenges**

- REDIRECT URL 03/10-04/10/23

  - tried directly through settings.py: not industry standard, not advised
  - tried tweaking the LoginView from djangos own views, found out it would be best to create a custom view that inherits from LoginView + didn't work anyway
  - def get_success_url(self): tried messing with this in my own view and failed
  - def form_valid(self, form): tried changing this and returning my own dynamic url and also failed
  - pushed the issue down the line

- Using different views from Django:
  - because of my navbar in base.html requiring certain variables to be returned
    - FIXED by adding the method get_context_data

### **Fixed Bugs**

### **Unfixed Bugs**

## **Technologies Used**

### **Languages**

- HTML
- CSS
- JavaScript
- Python 3.11.1
- Bootstrap 5

### **Libraries**

- asgiref v3.7.2
- certifi v2023.7.22
- charset-normalizer v3.2.0
- cloudinary v1.34.0
- defusedxml v0.7.1
- Django v4.2.3
- django-allauth v0.54.0
- idna v3.4
- python-dotenv v1.0.0
- python3-openid v3.2.0
- requests v2.31.0
- requests-oauthlib v1.3.1
- sqlparse v0.4.4
- typing-extensions v4.7.1
- urllib3 v1.26.16

### **Tools**

- [**Heroku**](https://www.heroku.com/) - Used to house the in-browser app
- [**Lucid Charts**](https://www.lucidchart.com/) - Used to create the flow chart diagram

## **Deployment**

The project was deployed on GitHub pages from the ‘Main Branch Source Code’ using the following steps:

- ‘git add .’, ‘git commit” and ‘git push’ commands were issued one final time when the project was ready and finished.
- On Github the repository for the project was selected.
- Click the ‘Settings’ tab.
- On the left; select ‘Pages’.
- From here; select the source as ‘Main Branch’.
- Click ‘Save’.

GitHub may take a few minutes to deploy the website so be patient.

You can view the application on Heroku by clicking [**here**](LINK).

## **Creating the Heroku app**

Before creating the Heroku app:

1. Make sure you have a file named “requirements.txt” in your main project folder.
2. Open the command line and navigate to your project folder.
3. Run the command “pip3 freeze > requirements.txt”.
   - This will create a list of dependencies used in the project for Heroku to set up the environment later.
4. Push these latest changes, including the requirements.txt file, to your GitHub repository (or any other preferred Git service).

Now, you can proceed with creating the Heroku app:

1. Sign in to your Heroku account (if you don’t already have one, create a free account on [Heroku](https://www.heroku.com/) first).
2. Once logged in, click on the “Create new app” button on your Heroku dashboard and follow the subsequent steps.
3. From within your newly created app, click the “Settings” tab.
4. Scroll down to the section labeled “Config Vars” and click on “Reveal Config Vars”.
5. In the “Key” field enter “CREDS”.
6. In the “Value” field copy and paste the entire contents of the creds.json file from your project.
   - This will securely provide the necessary credentials to access your Google Sheets API.
7. Add another Key/Value of “PORT” and “8000” respectively.
8. Scroll down to the section labeled “Buildpacks” and click “Add buildpack”.
9. Add Python and NodeJS and make sure they are shown in that order.
10. Navigate to the “Deploy” tab at the top of the page.
11. Choose your preferred deployment method (GitHub, for example) and connect it to your app.
12. Search for the repository name in the dropdown menu and select it.
13. Click “Connect”.
14. Then, either select “Enable Automatic Deploys” or “Deploy Branch”; the difference is that one automatically deploys the app every time a change is pushed to GitHub and the other needs to be redeployed manually every time.
15. You should now have a working Heroku app on your dashboard.

## **Development**

If you would like to contribute to this project, please follow the following steps:

From GitHub:

1. Create a separate branch for your development work
2. Make any necessary modifications and improvements to the project on your branch.
3. Create a pull request with a clear and detailed description of the changes you have made.
4. I will review your changes and provide feedback if needed.
5. If everything looks good, I will merge the changes into the main branch of the project.

If you wish to use any parts of the project for your project, you are welcome to do so. However, please give credit to me by linking my GitHub profile.

Thank you for your interest in the project, and I look forward to any contributions or acknowledgments!

## **Credits**

- https://startbootstrap.com/template/full-width-pics - For homepage (index.html)
- https://www.youtube.com/watch?v=jqSl36xR9Ys&t=169s - live search feature + talk about jinja template not accepting JS template literals (${..})

### **Content**

- [Django Documentation](https://docs.djangoproject.com/en/4.2/)
- [Mozilla Developer](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Spotify API Documentation](https://developer.spotify.com/documentation/web-api)
- [Cloudinary Documentation](https://cloudinary.com/documentation)
- [Jinja Documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/)
- [WhiteNoise Django Documentation](https://whitenoise.readthedocs.io/en/latest/django.html)
- [Stack Overflow](https://stackoverflow.com/) - general enquiries/syntax
- [W3Schools](https://www.w3schools.com/) - general enquiries/syntax

<!-- CHECK that every POST method has {% csrf_token %} -->
<!-- CHECK ALL TEMPLATES FOR COMMENTS - ARE ALL STYLE SHEETS NEEDED FOR EXAMPLE - DELETE UNNEEDED ONES -->
<!-- Separate scripts in all templates into block scripts and add it to base.html -->
<!-- I have 2 env files, why? -->

<!-- Questions for Brian -->

1. Should I split the apps into their groups; Users, Clubs, Seasons or something alike? Or leave it all in one place?
2. Do I need to worry about the overuse of django "View", should I try to branch out more into CreateView, UpdateView for example?
3. Is my current ReadMe okay in terms of content direction and format?
