# Fantasy Football Draft Picker

[![Build Status](https://dev.azure.com/jhampso2/FFBTeamBuilder/_apis/build/status/FFBTeamBuilder?branchName=master)](https://dev.azure.com/jhampso2/FFBTeamBuilder/_build/latest?definitionId=1&branchName=master)

## Prerequisites

- [Python 3.6.8](https://www.python.org/downloads/release/python-368/)

## Optional

- [AutoHotKey](https://www.autohotkey.com/) (Windows only)

## Installing

1. Click the Azure Pipelines build status badge above and download the latest FFB_Draft_Picker zip artifact
2. Extract the zip file
3. Run the following commands in a terminal window

   ```sh
   # Change to the directory where you unzipped the artifact
   cd $Unzip_Path
   tar -zxvf ./ffb_draft_picker.tar.gz
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pip --upgrade
   pip install -r requirements.txt
   ```

## Usage

1. If not already activated, activate the virtual environment

   ```sh
   cd $Unzip_Path
   source .venv/bin/activate
   ```

1. As players are drafted, update `data/player_exclusions.yaml`

   ```yml
   # data/player_exclusions.yaml start of first round
   drafted: []
   other: []

   # Add players you don't want to draft to 'other'
   drafted: []
   other:
     - Sammy Watkins

   # data/player_exclusions after first round
   drafted:
     - Saquon Barkley
   other:
     - Sammy Watkins

   # Players in 'other' should still be added to the drafted listed as they are drafted
   drafted:
     - Saquon Barkley
     - Sammy Watkins
   other:
     - Sammy Watkins
   ```

   The draft list can be manually updated by typing the player's name as they are drafted, or by copying and pasting their name from the draft site's draft log.
   
   - Automated drafted list update using AutoHotkey (Windows only)  

     On Windows, the majority of the tasks for updating the draft list can be performed automatically using AutoHotKey  
     
     __NOTE 1:__ AutoHotKey must be installed before using the Automated draft list update method  
     __NOTE 2:__ You should practice using the automated draft list update in a mock draft before drafting a team for your league
     1. Before the draft starts, setup the empty drafted list. Ensure the text cursor is one space after the `-` so that the playey names will be copied to the correct spot.
        ```yml
         # data/player_exclusions.yaml before start of draft
         drafted: 
           - 
         ```
     1. Double click on `copy_player_name.ahk` to enabled the AutoHotKey draft list update shortcut
     1. Open `player_exclusions.yaml` in a text editor and ensure the text cursor is in the correct position
     1. Open your draft website and monitor the draft log. __DO NOT__ open any other browser tabs or other programs. 
     1. As players are drafted, hover the mouse over the players name and press `ctrl+shift+x` to activate the shortcut. This will perform the following actions:
        1. Highlight the first and last name of the player under the mouse
        1. Copy the player's name
        1. Switch to the `player_exclusions.yaml` file
        1. Paste the player in the drafted list
        1. Save the `player_exclusions.yaml` file
        1. Add a new blank entry to the drafted list
        1. Switch back the draft website
   - Limitiations of the Automated draft list update method
     - Only player's first and last name are copied. Players with 3+ parts to their name will have to have the rest of their name added manually (e.g. adding 'Jr.' to 'Odell Beckham')
     - Players with periods in their name will not copy correctly (e.g. T.Y. Hilton). You should manually add/correct these entries.
     - It is possible for the text cursor to end in the incorrect spot in `player_exclusions.yaml` due to timing issues, such as the draft log scrolling at the same time that you activate the player copy shortcut.
     The text cursor should always be positioned one space after the `-`. If it is not, you should manually correct this before copying additional players.

1. When it is your pick, Run ffb_draft_picker.py in a terminal window

   Use the player data to make a decision on who to draft

   ```sh
   # Run with standard scoring
   python ffb_draft_picker.py

   # Run with ppr scoring
   python ffb_draft_picker.py --scoring-system ppr

   # Show help
   python ffb_draft_picker.py -h

   usage: ffb_draft_picker.py [-h] [--scoring-system {standard,ppr}]
                          [--ranking-system {Rank}]

    Fantasy Football Draft Picker

    optional arguments:
    -h, --help            show this help message and exit
    --scoring-system {standard,ppr}
                            Scoring system
    --ranking-system {Rank}
                            Ranking system (Expert Consesus, ADP, etc). Only
                            Expert Consensus (Rank) supported.
    ```
1. After running `ffb-draft_picker.py`, switch back to the text editor with `player_exclusions.yaml` and validate the cursor is positioned correctly, then switch back to monitoring the draft log.
1. Continue updating the `data/player_exclusions.yaml` file and running `ffb_draft_picker.py` until your draft is complete!
