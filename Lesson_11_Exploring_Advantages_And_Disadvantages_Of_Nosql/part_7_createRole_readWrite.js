db.createRole({
    role: "readWrite",
    privileges: [
        { resource: { db: "myDatabase", collection: "myCollection" }, actions: ["insert", "update", "remove"] }
    ],
    roles: []
});
