from bs4 import BeautifulSoup


with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")


print(soup.title)
print(soup.title.name)
print(soup.title.string)



# Print out all of the HTML Code formatted properly
#print(soup.prettify())



# Print the FIRST occurance of each tag type
print(soup.a)
print(soup.li)
print(soup.p)



# Print ALL of the occurances of each tag
allAnchorTags = soup.find_all(name="a")
print(allAnchorTags)

allParagraphTags = soup.find_all(name="p")
print(allParagraphTags)



# Obtain particular information from each of the found tags
for tag in allAnchorTags:
    print(tag.getText())
    print(tag.get("href"))



# find a particular element
heading = soup.find(name="h1", id="name")
print(heading)

sectionHeading = soup.find(name="h3", class_="heading")
print(sectionHeading.getText())
print(sectionHeading.name)
print(sectionHeading.get("class"))


# we can also use CSS Selectors to locate items in HTML
companyURL = soup.select_one(selector="p a")
print(companyURL)

name = soup.select_one(selector="#name")
print(name)
