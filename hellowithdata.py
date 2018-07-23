def handler(event, context):
    try:
        print event['data']
    except:
        pass
    return "ok google, deploy this"
