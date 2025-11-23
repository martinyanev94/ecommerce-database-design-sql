db.orders.aggregate([
    { $match: { status: "shipped" } },
    { $group: { _id: "$customerId", total: { $sum: "$amount" } } }
]);
