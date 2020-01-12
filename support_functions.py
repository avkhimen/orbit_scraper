import argparse

def get_input_args():
    
    parser = argparse.ArgumentParser()

    parser.add_argument('text_notification_or_or_off', type = bool, 
    					default = False, 
    					help = "Argument to enable text message "\
    					"notifications. Possible values are 'True' "\
    					"and 'False'")
    return parser.parse_args()