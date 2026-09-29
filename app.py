import app_data

# Add record to app_data.
# app_data.add_one("Rehan", "Sajid", "rehan@gmail.com")

# Delete record using rowid as string.
# app_data.delete_one('4')

# Lookup in data.
app_data.data_lookup("billie@gmail.com")

# Add many records.
# stuff = [
#     ('Leo', 'Alexander', 'leo@alex.com'),
#     ('Ethan', 'James', 'ethan@james.com'),
#     ('Maya', 'Elizabeth', 'maya@alex')
# ]
# app_data.add_many(stuff) 

# Show all records to app_data.
# app_data.show_all()