import requests
from rich import box
from rich.table import Table
from rich.console import Console
from bs4 import BeautifulSoup as soup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

page = soup(response.text, "html.parser")
# with open("pageoutput.html", "w") as f:
#     f.write(page.prettify())

# get the movies
movies = page.select("h3.title")
print(movies)
for movie in movies:
    print(movie)

# THIS DOESN't WORK IN 2021!!!!

# table = Table(title="ycombinator ranked links", show_lines=True, box=box.MINIMAL_DOUBLE_HEAD)
# table.add_column("Rank")
# table.add_column("Title")
# table.add_column("URL")
# for link in ranked_links:
#     table.add_row(str(link["points"]), link["text"], link["url"])
# console = Console()
# console.print(table)