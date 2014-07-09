__author__ = 'yiqing'

from arango import create

conn = create(db='test')
conn.database.create()

conn.test_collection.create()

conn.test_collection.documents.create(
    {
        'sample_key':'sample_value'
    }
)

doc = conn.test_collection.documents().first

print(doc.body)

for doc in conn.test_collection.query.execute():
    print(doc.id)

