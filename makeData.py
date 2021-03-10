#!/usr/bin/env python3
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

auth_provider = PlainTextAuthProvider(username='user', password='pass')
cluster = Cluster(['YOURADDRESS'], auth_provider=auth_provider)
session = cluster.connect()

session.exicute( CREATE KEYSPACE test WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'dc1' : 3 })
session.exicute( CREATE TABLE test.users (username text, name text, age int, PRIMARY KEY(username));)
session.exicute(INSERT INTO users(username,name,age) VALUES ('EricZ','Eric Zietlow',67);)

cluster.shutdown()
