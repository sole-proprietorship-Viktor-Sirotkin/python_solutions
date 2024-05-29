import xml.etree.ElementTree as ET

# Define the dictionary of European capitals
european_capitals = {
    "Albania": "Tirana",
    "Andorra": "Andorra la Vella",
    "Armenia": "Yerevan",
    "Austria": "Vienna",
    "Azerbaijan": "Baku",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Bosnia and Herzegovina": "Sarajevo",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Georgia": "Tbilisi",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Kazakhstan": "Nur-Sultan",
    "Kosovo": "Pristina",
    "Latvia": "Riga",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg City",
    "Malta": "Valletta",
    "Moldova": "Chisinau",
    "Monaco": "Monaco",
    "Montenegro": "Podgorica",
    "Netherlands": "Amsterdam",
    "North Macedonia": "Skopje",
    "Norway": "Oslo",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "San Marino": "San Marino",
    "Serbia": "Belgrade",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Turkey": "Ankara",
    "Ukraine": "Kyiv",
    "United Kingdom": "London",
    "Vatican City": "Vatican City",
}

# Create the root element of the XML tree
root = ET.Element("capitals")

# Iterate over the dictionary and create an XML element for each country
for country, capital in european_capitals.items():
    country_element = ET.SubElement(root, "country", {"name": country})
    country_element.text = capital

# Create an ElementTree object and write it to an XML file
tree = ET.ElementTree(root)
tree.write("european_capitals.xml", encoding="utf-8", xml_declaration=True)

print("XML file 'european_capitals.xml' has been created successfully.")
