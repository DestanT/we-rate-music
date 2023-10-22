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

We Rate Music is a "book club" for music. Inspired by a group of friends and their WhatsApp group. We all enjoy listening to music and spend variying amounts of time discussing the importance of music in our lives, and in the lives of human beings more generally.

Users can form clubs with their friends and within their own clubs create custom themed "seasons". Each season will have a short description, describing what the rules for the season are. Some examples of this may include; "Best for studying" or "Best for a gym workout". Or more interestingly; "each chosen song within the playlist must have an artist featured in the previous chosen song, with the first song being a free choice".

Club members are prompted to make their submissions and the app will roll out the playlists, with their respective spotify links, one by one to its members to listen to and rate out of 10. Once all ratings are gathered the next playlist will be featured.

To access the application, visit the Heroku app [**here**](https://we-rate-music-6240e7e17326.herokuapp.com/).

## **Goals**

The primary goals are to replace manual clumsy attempts at keeping past scores and submissions on an excel spreadsheet, and to create a thriving community of users who also enjoy curating playlists and listening to music. In the future, we envision:

- Expanding the user base and allowing users to form connections with one another based on their shared music tastes.
- Facilitating Club-on-Club competitions with anonymous submissions and ratings until the very end.
- Further intregration of the Spotify API to enhance parameters and thus set better recommendations between users.

## **Django Apps**

Though the apps primary features are detailed [**below**](#features), here is a quick overview on the Django file structure that is used and an overview on what the different apps do in the grand scheme of We Rate Music.

### **Users**

The "Users" application allows users to:

- Add their public Spotify playlists to their "We Rate Music" profile.
- Discover and explore playlists shared by other users.
- Personalise their profiles with a profile picture, a background picture for their profile and their Spotify username information.

### **Clubs**

The "Clubs" application serves users with all club-related features:

- Create, view, edit, and delete clubs.
- Invite members.
- Handle invitations displayed on users' profiles.

### **Seasons**

Within the "Seasons" application, club founders can:

- Create seasons with a short description for rules of the season.
- Collect and display playlists from its club members.
- Enable members to rate playlists, with the results tracked and averaged for each playlist in each season.

## **Features**

### **Spotify API**

Public Spotify playlists of a user can be searched and added to their "We Rate Music" profile. The API is currently limited to this information:

- Playlist name.
- Playlist album cover image.
- Track names within the playlist.

As the app grows I would like to include far more utility around the Spotify API, more information on what is on the roadmap can be found [**here**](#future-featuresroadmap).

Users must add their Spotify username to use this feature (found within the accounts tab in their Spotify app/web app). As this feature is an integral part of using the "We Rate Music" app, users without at least a free Spotify account will not be able to use "We Rate Music" effectively .

### **User Profile**

Users can sign-up to the application using a unique username and password.

### **Settings**

Within the "Settings" tab in user profiles, users can:

- Customise user profiles with profile/background pictures.
- Add their Spotify username information.

### **User Stats**

Coming soon...

### **Discover Playlists**

Within the "Discover" view users can:

- Explore other users' playlists.
- Search for other users and view their profiles.

### **View/Create Clubs**

This feature allows users to:

- Create clubs.
- Invite members.
<!-- NOT YET ADDED -->
- Create seasons with a text descriptive theme.
- Rate other members' playlists within seasons.
- View past seasons, playlist submissions and respective ratings.

### **Add Playlists**

Users can use the Spotify API to:

- Add their public Spotify playlists to their "We Rate Music" profile.
<!-- NOT YET ADDED -->
- Remove playlists from their profiles.

## **Future Features/Roadmap**

The roadmap includes:

- Enhanced Spotify API integration for a better user experience, such as the inclusion of genre information on tracks within playlists. This will enable the app to better pinpoint user genre preferences and allow other users to see this information on each others profiles.
- Support for club-on-club competitions; with anonymous submissions and scoring right up until the end, users can be excited to see which club curated the better playlists on average for the chosen season.
- User-Follow functionality; allowing users to stay connected to other users based on their ability to curate music and their music taste.
- Comments section for playlists, to allow users to express their thoughts and feelings on playlists.
- Season voting system; club founders can propose a few season/rules to their members and members can vote on which season goes next.
- Join season feature; giving members more flexibility to join or skip a season.
- More control for clubs; founders can kick members and urge them to hasten up their submissions.
- User-Statistics tab: for a more advanced view on each user's genre preference, average ratings given, amount of seasons completed etc.

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
