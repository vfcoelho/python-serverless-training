import json

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def claim_gift(event,context):

# 01 - Finding out how things communicate:

    # log.info(json.dumps(event))

# 02 - Manipulating objects:

    body = json.loads(event['body'])
    item_id = body['id']
    # log.info(item_id)

# 03 - Write test basic test for local execution

# 04 - Connecting to database:
    from utils.db_credentials import DBCredentials #place it on top
    import psycopg2
    
    conn = psycopg2.connect(**DBCredentials.credentials)
    cur = conn.cursor()

    cur.execute("update items set reserved = true where id = %s",(item_id,))

# 05 - Provision a cloud database:

# 06 - Change DBCredentials.credentials so get from environment variables

#07 - Provision CI/CD if psycopg has problems

# Common closing code -----------------------

    cur.close()
    conn.commit()
    conn.close()

    response = {
        "statusCode": 200
    }
    return response