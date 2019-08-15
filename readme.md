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
   python -m venv .venv
   pip install pip --upgrade
   pip install ./requirements.txt
   ```