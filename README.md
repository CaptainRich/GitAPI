# $`\textcolor{blue}{\text{GitAPI}}`$
A script to query the GitHub API for starred Python (or other 'language' projects.
Richard Ay (March 2024, *updated March 2024*)

## $`\textcolor{blue}{\text{Table of Contents}}`$
* [Setup](#setup)
* [Environment](#environment)
* [Usage](#Usage)
* [References](#references)
* [File List](#file-list)
* [Technologies and Imports](#Technologies-and-Imports)
* [Images](#Images)

## Setup

*To use this program, activate the 'virtual environment' "GitAPIEnv".  

## Environment
A virtual environment is created so that the installation of matplotlib and plotly
remain local to this subdirectory, and do not affect the rest of the machine.

The virtual environment can be setup using the command: 
**'python -m venv "GitAPIEnv" --upgrade-deps --prompt="GitAPIEnv"'**

To start/stop the virtual environment, use the commands: **'VisualEnv\scripts\activate'** 
or **'deactivate'**. Once activated, the virtual environment will change the (terminal) 
prompt from (PS) to (VisualnEnv).

After starting the virtual environment, matplotlib and plotly (and pandas) can be installed 
with the commands:  
**'python -m pip install --user requests'**  
**'python -m pip install plotly'**  
**'python -m pip install pandas'**  

Subsequently the installations can be verified with the command:   
**'python -m pip show requests'**  
**'python -m pip show plotly'**  
**'python -m pip show pandas'** 


## Usage
From VSCode, by issuing the command (note the suffix ".py' is required)  
- 'python py_repos.py'  

The script reports status to the terminal.  If the search for the selected language
is successful, the summary data of the top 30 repositories is written to the file 'repos.out'.
A bar-chart is created showing the relative 'likes' of these 30 repositories, where the name of
the repository (used as the 'x' axis label) is a link to the associated repository.


## References
1. Python Crash Course, Eric Matthes, No Starch Press, 2023. Chapters 12-15.  


## File List
**py_repose.py** - a script to list and plot the top <language> repositories found on GitHub.
<language> can be 'Python' or 'Javascript'.   
**repos.out** - a text file (created by py_repos.py) that lists the repositories found. 



**/images** - a subdirectory with script images  


## Technologies and Imports
The following modules are necessary imports (imported in the .py files):  
- matplotlib  
- plotly
- pandas
 

## Images
The images below show the resulting visualizations and status reports generated 
by the script:  

The 'Python' repository:    
![Python Repository](https://github.com/CaptainRich/GitAPI/blob/main/images/python_repos.png)  

The 'Javascript' repository':  
![Javascript Repository](https://github.com/CaptainRich/GitAPI/blob/main/images/javascript_repos.png)  

The 'terminal status' report:  
![Terminal Status Report](https://github.com/CaptainRich/GitAPI/blob/main/images/terminal_status.png)  

The 'die roll' plot:  
![Die Roll Plot](https://github.com/CaptainRich/Visualizations/blob/main/images/die_roll_results.png)  



