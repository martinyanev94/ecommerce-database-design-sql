def update_document(document_id, new_value):
    document = db.collection.find_one({"_id": document_id})
    if new_value["timestamp"] > document["timestamp"]:
        db.collection.update_one(
            {"_id": document_id},
            {"$set": new_value}
        )
    else:
        print("Old version of document, update ignored.")
