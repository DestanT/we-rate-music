# __We Rate Music__

## __Table of Contents__
1. [Introduction](#introduction)
2. [Goals](#goals)
3. [Django Apps](#django-apps)
    * [Users](#users)
    * [Clubs](#clubs)
4. [Features:](#features)
    * [Spotify API](#spotify-api)
    * [User Profile](#user-profile)
    * [Settings](#settings)
    * [User Stats](#user-stats)
    * [Discover Playlists](#discover-playlists)
    * [Add Playlists](#add-playlists)
    * [View/Create Clubs](#view/create-clubs)
5. [Future Features/Roadmap](#future-featuresroadmap)
6. [Testing](#testing)
7. [Challenges & Bugs](#challenges—bugs)
8. [Technologies Used](#technologies-used)
9. [Deployment](#deployment)
10. [Creating the Heroku app](#creating-the-heroku-app)
11. [Development](#development)
12. [Credits](#credits)

## __Introduction__

Intro paragraph

To access the application, visit the Heroku app [**here**](LINK).

## __Goals__

We Rate Music aims to bring users together for their music tastes. The application also allows users to form groups and from within their groups submit playlists. Members of groups should commit to listening to the submitted playlists and rate them accordingly.

## __Django Apps__
### __Users__
- models
- views
### __Clubs__
- models
- views

## __Features__
### __Spotify API__
### __User Profile__
- follow
### __Settings__
- profile/background image
- user id for Spotify
### __User Stats__
### __Discover Playlists__
- search users
### __View/Create Clubs__
### __Add Playlists__

## __Future Features/Roadmap__

## __Testing__
### __Pylint__
### __Process__

## __Challenges & Bugs__
### __Challenges__
### __Fixed Bugs__
### __Unfixed Bugs__

## __Technologies Used__
### __Languages__
* HTML
* CSS
* JavaScript
* Python 3.11.1
* Bootstrap 5
### __Libraries__
* asgiref v3.7.2
* certifi v2023.7.22
* charset-normalizer v3.2.0
* cloudinary v1.34.0
* defusedxml v0.7.1
* Django v4.2.3
* django-allauth v0.54.0
* idna v3.4
* python-dotenv v1.0.0
* python3-openid v3.2.0
* requests v2.31.0
* requests-oauthlib v1.3.1
* sqlparse v0.4.4
* typing-extensions v4.7.1
* urllib3 v1.26.16
### __Tools__
* [**Heroku**](https://www.heroku.com/) - Used to house the in-browser app
* [**Lucid Charts**](https://www.lucidchart.com/) - Used to create the flow chart diagram

## __Deployment__

The project was deployed on GitHub pages from the ‘Main Branch Source Code’ using the following steps:
* ‘git add .’, ‘git commit” and ‘git push’ commands were issued one final time when the project was ready and finished.
* On Github the repository for the project was selected.
* Click the ‘Settings’ tab.
* On the left; select ‘Pages’.
* From here; select the source as ‘Main Branch’.
* Click ‘Save’.

GitHub may take a few minutes to deploy the website so be patient.

You can view the application on Heroku by clicking [**here**](LINK). 

## __Creating the Heroku app__

Before creating the Heroku app:
1. Make sure you have a file named “requirements.txt” in your main project folder.
2. Open the command line and navigate to your project folder.
3. Run the command “pip3 freeze > requirements.txt”.
    * This will create a list of dependencies used in the project for Heroku to set up the environment later.
4. Push these latest changes, including the requirements.txt file, to your GitHub repository (or any other preferred Git service).

Now, you can proceed with creating the Heroku app:
1. Sign in to your Heroku account (if you don’t already have one, create a free account on [Heroku](https://www.heroku.com/) first).
2. Once logged in, click on the “Create new app” button on your Heroku dashboard and follow the subsequent steps.
3. From within your newly created app, click the “Settings” tab.
4. Scroll down to the section labeled “Config Vars” and click on “Reveal Config Vars”.
5. In the “Key” field enter “CREDS”.
6. In the “Value” field copy and paste the entire contents of the creds.json file from your project.
    * This will securely provide the necessary credentials to access your Google Sheets API.
7. Add another Key/Value of “PORT” and “8000” respectively.
8. Scroll down to the section labeled “Buildpacks” and click “Add buildpack”.
9. Add Python and NodeJS and make sure they are shown in that order.
10. Navigate to the “Deploy” tab at the top of the page.
11. Choose your preferred deployment method (GitHub, for example) and connect it to your app.
12. Search for the repository name in the dropdown menu and select it.
13. Click “Connect”.
14. Then, either select “Enable Automatic Deploys” or “Deploy Branch”; the difference is that one automatically deploys the app every time a change is pushed to GitHub and the other needs to be redeployed manually every time.
15. You should now have a working Heroku app on your dashboard.

## __Development__

If you would like to contribute to this project, please follow the following steps:

From GitHub:
1. Create a separate branch for your development work
2. Make any necessary modifications and improvements to the project on your branch.
3. Create a pull request with a clear and detailed description of the changes you have made.
4. I will review your changes and provide feedback if needed.
5. If everything looks good, I will merge the changes into the main branch of the project.

If you wish to use any parts of the project for your project, you are welcome to do so. However, please give credit to me by linking my GitHub profile.

Thank you for your interest in the project, and I look forward to any contributions or acknowledgments!

## __Credits__
### __Content__
* [Django Documentation](https://docs.djangoproject.com/en/4.2/)
* [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Spotify API Documentation](https://developer.spotify.com/documentation/web-api)
* [Cloudinary Documentation](https://cloudinary.com/documentation)
* [Jinja Documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/)
* [Stack Overflow](https://stackoverflow.com/) - general enquiries/syntax
* [W3Schools](https://www.w3schools.com/) - general enquiries/syntax