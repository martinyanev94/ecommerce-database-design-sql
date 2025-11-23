CREATE PUBLICATION my_publication FOR TABLE orders;
CREATE SUBSCRIPTION my_subscription
CONNECTION 'host=primary_host dbname=postgres user=replicator password=replicator_password'
PUBLICATION my_publication;
