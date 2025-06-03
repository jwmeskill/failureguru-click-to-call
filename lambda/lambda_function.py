# lambda_function.py

def lambda_handler(event, context):
    # TODO: Handle click-to-call or webhook events
    print('Event received:', event)
    return {'statusCode': 200, 'body': 'OK'}
