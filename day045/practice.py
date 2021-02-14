import requests
from rich import box
from rich.table import Table
from rich.console import Console
from bs4 import BeautifulSoup as soup

# # read local HTML file
# with open("website.html") as f:
#     contents = [line.strip() for line in f.readlines()]
# contents = "".join(contents)

# # convert to soup
# page = soup(contents, "html.parser")

# # print page pretty
# print(page.prettify())

# # get page title
# print(page.title)

# # get page title tagname
# print(page.title.name)

# # get page title value
# print(page.title.string)

# # find all link texts
# print([link.string for link in page.find_all(name="a")])

# # find all link hrefs
# print([link.get("href") for link in page.find_all(name="a")])

# # find element with id
# print(page.find(id="name"))
# # print(page.select_one("#name"))

# # find all elements by class name
# print(page.find_all(class_="heading"))
# # print(page.select(".heading"))

# # get first link on page with css selectors
# print(page.select_one("p a"))

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

page = soup(response.text, "html.parser")
# print(page.prettify())

# get the stories table rows (row 0 = story link and text, row 1 = points, row 2 = spacer)
story_rows = page.select("table.itemlist tr")
unranked_links = []
found_link = False
j = 0
for i, _ in enumerate(story_rows):
    # cycle through each kind of row (they come in threes)
    row = {0: "link", 1: "points", 2: "spacer"}.get(i % 3)

    # this is a spacer row, which means we're moving on to the next story
    if row == "spacer":
        if found_link:
            j += 1
        found_link = False
        continue

    # this is the tr we're iterating over right now
    tr = story_rows[i]

    # this is a link row
    if row == "link":
        try:
            link = tr.select_one("a.storylink")
        except:
            continue
        else:
            try:
                text = link.string
            except:
                continue
            else:
                try:
                    url = link.get("href")
                except:
                    continue
                else:
                    unranked_links.append({
                        "text": text,
                        "url": url
                    })
                    found_link = True
        continue

    # this is a points row
    if row == "points" and found_link:
        try:
            points = int(tr.select_one("span.score").string.split(" ")[0])
        except:
            points = 0
        finally:
            unranked_links[j]["points"] = points
        continue

ranked_links = sorted(unranked_links, key=lambda d: d["points"], reverse=True)

table = Table(title="ycombinator ranked links", show_lines=True, box=box.MINIMAL_DOUBLE_HEAD)
table.add_column("Rank")
table.add_column("Title")
table.add_column("URL")
for link in ranked_links:
    table.add_row(str(link["points"]), link["text"], link["url"])
console = Console()
console.print(table)