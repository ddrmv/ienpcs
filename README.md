# IENPCs catalogue and portraits

Infinity Engine NPC catalogue and portraits.


## Description

This Django app serves as a character management system, featuring a gallery of NPCs, each with unique attributes and portraits. It functions as a character browser, portrait gallery, and adventuring party organizer.

As anonymous user you can:
- browse games
- browse NPCs per game
- browse characters, related NPC and portraits
- see linked sites
- use contact form to reach site admin
- toggle the theme between Dark and Light
- register a user account

As a registered user you can do all of the above and:
- add NPC to party roster from game page or character page
- create/update/delete custom player characters (PCs)
- upload a portraits for the PCs and modify their attributes
- manage a custom party selection list of up to 20 NPCs and 10 PCs
- manage an up to six-slot party, persistent between logins
- add to the slots NPCs and PCs from the list
- clear slots or swap with adjacent slots
- change the number of slots in the party ranging from 1 to 6

As an admin you can do all of the above and:
- manage users, invitation codes
- add/update/remove games, NPCs, characters, portraits
- create and manage links between NPCs, characters, games, portraits


## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Screenshots](#screenshots)
4. [Technologies Used](#technologies-used)
5. [Contact Information](#contact-information)


## Installation
To run the project locally:

```bash
# 1. Clone the repo
git clone https://github.com/ddrmv/ienpcs.git

# 2. Set up virtual environment and activate it
python -m venv .venv

.venv\Scripts\activate     # Windows
# or
source .venv/bin/activate  # Unix/MacOS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup the Django database
# navigate to manage.py
python manage.py makemigrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver

# 6. The application should be now accessible at http://127.0.0.1:8000/

# 7. See below for creating superuser and loading data into the site
```
Note: Web server file upload size limit needs to be set due to forms processing user-uploaded images for player characters. There is a check for maximum 100KB size, but Django can only check after completed upload.


## Usage
Instructions on how to use your project, including any necessary commands to run the server, create a superuser, etc.

There are three use levels for the site: as Admin, as a registered user and as anonymous/guest user.

First, you need to create the superuser account: 

```bash
# After you have installed the app navigate to manage.py and type
python manage.py createsuperuser

# Enter username and password, the email is optional

# Start the website
python manage.py runserver
```
Navigate to the Admin site at http://127.0.0.1:8000/admin/.

Log in as the superuser. Add an invitation code to enable users to register via the site. Go to Invitation Codes -> Add, the users will need to add the code exactly as written. Optionally increase the Max uses. Now users can register at http://127.0.0.1:8000/gallery/register/. 

The Admin can add Games, NPCs, Characters, Portraits. Other registered users can manage a party and browse, anonymous users can browse.

There is very little on the website, unless the aforementioned data has been populated. To load data from fixtures:

```bash
python manage.py loaddata TODO:FIXTURE
```

## Screenshots

### Games list (Home page)
![Games List](https://i.imgur.com/EYpFpCm.png)
A Light theme screenshot of the game list page. Here users can see a list of games and all associated NPCs.

### Game detail page
![Games detail](https://i.imgur.com/UFiMUKI.png)
A Dark theme screenshot of the game detail page, with all NPCs in three groups: original, added by Beamdog in Enhanced Editions, created by modders.

### Party management page
![Party management](https://i.imgur.com/ynZzwoj.png)
A screenshot of the party management page, as it works for registered users. For unregistered users it is mostly empty.

![Party management as guest](https://i.imgur.com/5PFUt8f.png)
The party management page when not logged in.

Registered users can add NPCs and create, modify and delete custom PCs:
![Add PC](https://i.imgur.com/lnGLV0e.png)

### Character list page
![Character list](https://i.imgur.com/pa0Ilb0.png)
At the character list page are all characters of all games.

### Character detail page
![Character detail](https://i.imgur.com/Voj6UWJ.png)
At the character detail page are all portraits for the character and their appearances in games as slightly different NPCs.

### About/Contact page
![About](https://i.imgur.com/BtleRz4.png)
The About page explains in more detail the structure of the site, how it works, and provides a form to send a message to the site owner.

### Links page
![Links](https://i.imgur.com/UqXRFAv.png)
The links page contains links to relevant websites.


## Technologies Used
The project uses Django and Bootstrap.


## Contact Information

Please feel free to reach out with comments:

- GitHub: [github.com/ddrmv](https://github.com/ddrmv)
