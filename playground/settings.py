"""
Eve playground settings
"""

DOMAIN = {
    "accounts": {
        "schema": {
            "name": {
                "type": "string",
            },
            "can_manage": {
                "type": "list",
                "schema": {
                    "type": "objectid",
                    "data_relation": {
                        "resource": "accounts",
                        "field": "_id",
                        "embeddable": True,
                    },
                },
            },
        },
    },
}

RESOURCE_METHODS = ["GET", "POST"]
ITEM_METHODS = ["GET", "PATCH"]

MONGO_HOST = "db"
MONGO_PORT = 27017
MONGO_DBNAME = "playground"
