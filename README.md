# Top-Ship
(Developer: Keith Bautista)

![Start screen](docs/features/features_welcome_message.PNG)

[Live Webpage](https://top-ship.herokuapp.com/)

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Site Owner Stories](#site-owner-stories)
3. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [PEP8 validation](#pep8-validation)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgments](#acknowledgments)

## Project Goals
Top-Ship is an application that mimics the very popular boardgame "Battleship", though with a little Top-Gun twist :)

### User Goals
- Enjoy a memorable game such as Battleship and also get lost in the sea with hints of Top-Gun loitered about.

### Site Owner Goals
- Providing users with the ability to play a fun filled game from their childhood at the tips of their fingers and without having to clean up!

## User Experience

### Target Audience
- People who grew up with Battleship as one of their board games and Top-Gun as their favorite movies.
- People who would like to play a board game from the comfort of their phone and not having to clean up the board game.

### User Requirements and Expectations
- Easy to load and set up with having minimal input
- Ability to personalize the game to your liking
- Easy to use

### User Stories
1. As a user, I want to be able to open up the game without having to set it up
2. As a user, I want to be able to personalise the game based to my liking 
3. As a user, I want to be able to see the game in an easy to read format and grid

### Site Owner Stories
4. As a site owner, I want users to be able to personalise the game to their liking
5. As a site owner, I want users to easily load the game and see an easy to understand format game.

## Technical Design

### Flowchart
<details><summary>Flowchart</summary>
<img src="docs/flowchart_top_ship.png">
</details>

## Technologies Used

### Languages
- Python 3

### Frameworks and Tools
- diagrams<span>.</span>net - to create a flow chart
- GitHub
- GitPod
- Git
- Heroku
- Textart<span>.</span>io - to create image out of text for homepage

## Features

### Welcome Message
- Shows a welcome message and an ASCII art containing a ship with the words Top-Ship across its side.

<details><summary>Welcome message</summary>
<img src="docs/features/feature_welcome_message.jpg">
</details>

### Choose Board Size
- Ability to choose board size to user liking
<details><summary>Choose Board Size</summary>
<img src="docs/features/features_choose_board_size.png">
</details>

### Choose No. Ships
- Ability to choose amount of ships to user liking
<details><summary>Choose No. Ships</summary>
<img src="docs/features/features_choose_ship_no.png">
</details>

### User Input Validation
- If Board Size or Ship No is too big or incorrect format then we request for the input again.
<details><summary>Input validation</summary>
<img src="docs/features/features_choose_board_size_input_validation.png">
</details>

### Easily Reset Game
- Ability to easily reset the game through a click of a button
<details><summary>Reset Game</summary>
<img src="docs/features/features_reset_game.png">
</details>

## Validation
PEP8 online was used to check the code for PEP8 requirements.
All code passed with no errors and no warnings to show.

<details><summary>run.py</summary>
<img src="docs/validation/pep8_validation_run.png">
</details>

extendsclass was also used as a Python Validator on top of the IDE.
All code passed with no errors and no warnings to show.

<details><summary>run.py</summary>
<img src="docs/validation/python_validator_run.png">
</details>

### Testing User Stories
### User Stories
1. As a user, I want to be able to open up the game without having to set it up

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Welcome Message | Run Program | Easily Set Up Game | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_stories_welcome_message.PNG">
</details>

2. As a user, I want to be able to personalise the game based to my liking 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Choose Board Size, Choose No. Ships | Provide desired input based on liking | Based on input, grid will adjust | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_stories_choose_board_size.png">
<img src="docs/user_stories/user_stories_choose_ship_no.png">
<img src="docs/user_stories/user_stories_grid_adjusted.png">
</details>

3. As a user, I want to be able to see the game in an easy to read format and grid

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Welcome Message, Whole Program | Input desired no of ships and board size | Based on input, grid will adjust | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_stories_grid_adjusted.png">
</details>

### Site Owner Stories
4. As a site owner, I want users to be able to personalise the game to their liking

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Choose Board Size, Choose No. Ships | Provide desired input based on liking | Based on input, grid will adjust | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_stories_choose_board_size.png">
<img src="docs/user_stories/user_stories_choose_ship_no.png">
<img src="docs/user_stories/user_stories_grid_adjusted.png">
</details>

5. As a site owner, I want users to easily load the game and see an easy to understand format game.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Welcome Message, Whole Program | Input desired no of ships and board size | Based on input, grid will adjust | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_stories_grid_adjusted.png">
</details>

## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| When updating the board size and no of ships in the input, the accomodating variables were not being updated | Allowing the variable to be accessed Globally meant that other methods were able to use it |
| Whitespace | PEP8 validator found all whitespaces, in order to remove this error, you need to remove spaces that you may not see using the naked eye unless highlighted |

## Deployment
The website was deployed using Heroku by following these steps
1. Login or Create a Heroku Account
2. Click the "new" button in the upper right corner and select "create new app"
3. Choose and app name and your region and click "Create app"
4. Go to the "settings" tab of your build and add the python build first and then the node.js build. Without the node.js pack the mock terminal will not work.
5. Go to the Config Vars just right above the buildpacks and place in "PORT" as the "KEY" and then "8000" as the "VALUE" 
6. Navigate to the "deploy" tab and pick GitHub as your deployment method. Make sure that you opt into the "Automatic Deploys" as the Heroku app will update as soon as you push from gitpod to GitHub
7. Search for the repository you would like to connect to. This option should be right above where you clicked "Enable Automatic Deploys"
8. Wait for the app to build and then click on the "View" link

You can fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on the Fork button in the upper right-hand corner

You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone.
