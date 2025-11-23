// User Alice adds an item to the shopping cart
db.carts.update({ user_id: "001" }, { $addToSet: { items: "item123" } });

// User Bob queries the cart before synchronization
let cart = db.carts.findOne({ user_id: "001" });
// There may be a delay where Bob's view doesn't reflect Alice's current changes.
