import shelve

# Open the shelf file
myData = shelve.open("myData")

# Insert data into the shelf
cats = ["Zophie", "Pooka", "Simon"]
myData["cats"] = cats

# Close the shelf
myData.close()

# Reopen the shelf file to retrieve the data
myData = shelve.open("myData")

# Retrieve the data
retrieved_cats = myData["cats"]

# Display the retrieved data
print("Retrieved cats:", retrieved_cats)

# Close the shelf
myData.close()
