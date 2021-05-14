import xml.etree.ElementTree as ET

tree = ET.parse("moviesdat.xml")
root = tree.getroot()

print(root.tag) # this should return "collection"
print(root.attrib) # returns empty dictionary

for child in root:
    print(child.tag, child.attrib)
        # Returns "genre {'category': 'Action'}"
        # returns "genre {'category': 'Thriller'}"
        # returns "genre {'category': 'Comedy'}", etc...

# iterate over the entire tree, and display results
for elem in root.iter():
    print(elem.tag)

print(ET.tostring(root, encoding="utf8").decode("utf8"))

for movie in root.iter("movie"):
    print(movie.attrib)
input("Press Enter to continue")
# Below is the data that we expect our loop to return.
#{"favorite": "True", "title": "Indiana Jones: The raiders of the lost Ark"}
#{"favorite": "True", "title": "THE KARATE KID"}
#{"favorite": "False", "title": "Back 2 the Future"}
#{"favorite": "False", "title": "X-Men"}
#{"favorite": "True", "title": "Batman Returns"}
#{"favorite": "False", "title": "Reservoir Dogs"}
#{"favorite": "False", "title": "ALIEN"}
#{"favorite": "True", "title": "Ferris Bueller's Day Off"}
#{"favorite": "FALSE", "title": "American Psycho"}
#{"favorite": "False", "title": "Batman: The Movie"}
#{"favorite": "True", "title": "Easy A"}
#{"favorite": "True", "title": "Dinner for SCHMUCKS"}
#{"favorite": "False", "title": "Ghostbusters"}
#{"favorite": "True", "title": "Robin Hood: Prince of Thieves"}

print("Print the descriptions of each movie")
for description in root.iter('description'):
    print(description.text)
# this will print out the descriptions of each movie

print("Movies that came out in 1992")
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

print("Movies available in multiple formats")
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(movie.attrib)
