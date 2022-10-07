import json

def lambda_handler(event, context):
    
    response = {
        "status": 302,
        "statusDescription": "Found",
        "isBase64Encoded": False,
        "headers": {
            "location": [{
                "key": 'Location',
                "value": 'http://new.aitherlabs.ninja/app/v2/newlogin.html',
            }],
        }
    }
    
    return response