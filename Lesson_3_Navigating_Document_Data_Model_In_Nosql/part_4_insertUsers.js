db.users.insertMany([
    {
        "user_id": "124",
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "preferences": {
            "newsletter": true,
            "notifications": true
        },
        "addresses": []
    },
    {
        "user_id": "125",
        "name": "Tom Brown",
        "email": "tombrown@example.com",
        "preferences": {
            "newsletter": false,
            "notifications": true
        },
        "addresses": [
            {
                "type": "home",
                "address": "789 Elm St, Springfield, IL"
            }
        ]
    }
]);
