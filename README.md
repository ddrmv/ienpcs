# IENPCs catalogue and portraits

Plan for two apps:
- NPC catalogue.
- A corresponding portrait catalogue for each.

The apps should be linked but not dependant on each other.

User stories for the portrait gallery:

As a PERSONA, I WANT_TO, SO_THAT.
```
As the admin:
-----------------------------------------------------------------------
I want to upload an image I've created for an NPC to the NPC's gallery
So that I can share my art

I want to create, read, update, delete a game
So I can manage the games I have portraits for

I want to CRUD an NPC, so I can manage them

I want to CRUD a portrait pack, so I can manage them


As a user:
-----------------------------------------------------------------------
I want to see a home page with the games and all npcs for each game
So I get an overview of all NPCs on the site

I want to see a game page with all NPCs
So I can see all NPCs together

I want to see a game page with a how to update portraits
So I can replace the portraits in my own game
```

Models:
```
class Game
name
codename

class Npc
game_fk
name
adnd_class
race
alignment
str
str_percentile
dex
con
int
wis
cha
description

class Portrait
npc_fk
description
gallery_image
zip_file
```