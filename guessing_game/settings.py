"""
Global Settings for the Guess The Number game. 
ASCII Art generated from https://patorjk.com/software/taag/
"""

import os

# Specify an absolute path for the scoreboard file
# Step 1: Get the directory of the current script (__file__ refers to the current script)
current_script_directory = os.path.dirname(__file__)

# Step 2: Combine the script directory with the filename to create the full path
SCORE_BOARD_FILE = os.path.join(current_script_directory, "scoreboard.yaml")

MAX_TRIES = 5
ASCII = """
 GGG               TTTTTTh          N   N         b          
G                    TT  h          NN  N         b          
G  GGu  ueeesss      TT  hhh eee    N N Nu  ummmm bbb eeerrr 
G   Gu  ue ess       TT  h  he e    N  NNu  um m mb  be er   
 GGG  uuueesss       TT  h  hee     N   N uuum m mbbb ee r  
"""
