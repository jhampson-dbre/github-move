# Fantasy Football Draft Picker

[![Build Status](https://dev.azure.com/jhampso2/FFBTeamBuilder/_apis/build/status/FFBTeamBuilder?branchName=master)](https://dev.azure.com/jhampso2/FFBTeamBuilder/_build/latest?definitionId=1&branchName=master)

## Prerequisites

- [Python 3.6.8](https://www.python.org/downloads/release/python-368/)

## Installing

1. Click the Azure Pipelines build status badge above and download the latest FFB_Draft_Picker zip artifact
2. Extract the zip file
3. Run the following commands in a terminal window

   ```sh
   # Change to the directory where you unzipped the artifact
   cd $Unzip_Path
   tar -zxvf ./ffb_draft_picker.tar.gz
   python3 -m venv .venv/bin/activate
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

2. As players are drafted, update `data/player_exclusions.yaml`

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

3. When it is your pick, Run read_player_csv.py

   Use the player data to make a decision on who to draft

   ```sh
   # Run with standard scoring
   python read_player_csv.py

   # Run with ppr scoring
   python read_player_csv.py --scoring-system ppr

   # Show help
   python read_player_csv.py -h

   usage: read_player_csv.py [-h] [--scoring-system {standard,ppr}]
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

4. Continue updating the `data/player_exclusions.yaml` file and running `read_player_csv.py` until your draft is complete!
