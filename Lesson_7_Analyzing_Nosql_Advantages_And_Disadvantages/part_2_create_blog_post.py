from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

def create_blog_post(title, content, author):
    cluster = Cluster('couchbase://localhost', ClusterOptions(
        PasswordAuthenticator('admin', 'password')))
    bucket = cluster.bucket('blog')
    collection = bucket.default_collection()

    blog_post = {
        'title': title,
        'content': content,
        'author': author
    }

    collection.upsert(title, blog_post)
    print(f"Blog post '{title}' created successfully.")
