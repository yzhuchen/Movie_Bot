###################################################################
######## Configuration files for Bot   ##########################
###################################################################

"""
    config.py 
    
    This files has all the configurations for your bot.
    
"""

from elasticsearch import Elasticsearch
import watson_developer_cloud
from slackclient import SlackClient

location = "/Users/yz/Downloads/Movie_Bot-master"  # replace with the full folder path where you downloaded the github repo

###################################################################
######## Slack configuration   ##########################
###################################################################

SLACK_BOT_TOKEN='xoxp-671083137175-668758664628-660070245715-0d87ebc35e854672f31c62882464119b'
SLACK_VERIFICATION_TOKEN='BJEvijfSJjjlBc5COBbfi68w'  

# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN) # do not change this parameter

###################################################################
######## Watson service configuration   ##########################
###################################################################

service = watson_developer_cloud.AssistantV1(
    iam_api_key = 'HdKlAM9t_57j4SwnO5A60fxK8Ay6SoY4w6OXxEAy8f7e', # replace with Password
    version = '2018-09-20'
)

workspace_id = '741bfeed-7ae2-495c-89ad-c175c1915dfa' # replace with Assistant ID

###################################################################
######## Log files configuration   ##########################
###################################################################

log_commands_path = location + "logs/log_commands.py" # do not change this parameter
follow_up_path = location + "logs/followup_email.py" # do not change this parameter

###################################################################
######## Temp files configuration   ##########################
###################################################################

onetime_path = location + "nlp/nlp_solutions/onetime_run_file.py" # do not change this parameter
onetime_file = location + "nlp/nlp_solutions/onetime.txt" # do not change this parameter
