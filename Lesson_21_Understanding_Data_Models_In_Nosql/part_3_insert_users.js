db.users.insertMany([
    {
        name: "Alice",
        age: 28,
        hobbies: ["reading", "travelling"],
        address: {
            street: "123 Maple St",
            city: "Somewhere",
            zip: "12345"
        }
    },
    {
        name: "Bob",
        age: 32,
        hobbies: ["gaming", "writing"],
        address: {
            street: "456 Oak St",
            city: "Anywhere",
            zip: "67890"
        }
    }
]);
