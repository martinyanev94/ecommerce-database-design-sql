CREATE KEYSPACE my_keyspace WITH REPLICATION = 
{ 'class' : 'NetworkTopologyStrategy', 'dc1' : 3, 'dc2' : 2 };
