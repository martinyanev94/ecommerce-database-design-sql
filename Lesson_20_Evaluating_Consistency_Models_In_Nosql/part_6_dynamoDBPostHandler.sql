let response = await dynamoDB.put({
    TableName: 'Posts',
    Item: {
        userId: 'abcd',
        postId: '1234',
        content: 'Hello World!'
    }
}).promise();

let post = await dynamoDB.get({
    TableName: 'Posts',
    Key: {
        userId: 'abcd',
        postId: '1234'
    },
    ConsistentRead: true
}).promise();
