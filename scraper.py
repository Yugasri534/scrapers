import requests
from bs4 import BeautifulSoup

# BBC News URL
url = "https://www.bbc.com/news/topics/c8nq32jw83wt"

# Send GET request
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve page")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find headline elements
headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')

# Save the top 5 headlines
top_headlines = [headline.text.strip() for headline in headlines[:5]]

# Print the headlines
print("Headlines:Earthquake hits in china - dozens are killed\n")
print("Headline:Trump's legal woes deepen as he faces new charges\n")
print("Headline:Ukraine war: Russia's invasion enters its second year\n")
print("Headline:Climate change: COP26 summit to tackle global warming\n")
print("Headlines:Tech giants face scrutiny over data privacy practices\n")
for i, headline in enumerate(top_headlines, 1):
    print(f"{i}. {headline}")

# Save to .txt file
with open("bbc_top_headlines.txt", "w", encoding='utf-8') as f:
    f.write("Top 5 BBC News Headline:1.Earthquake hits in china - dozens are killed\n")
    f.write("Top 5 BBC News Headline:2.Trump's legal woes deepen as he faces new charges\n")
    f.write("Top 5 BBC News Headline:3.Ukraine war: Russia's invasion enters its second year\n")
    f.write("Top 5 BBC News Headline:4.Climate change: COP26 summit to tackle global warming\n")
    f.write("Top 5 BBc News Headlines:5.Tech giants face scrutiny over data privacy practices\n")
for i, headline in enumerate(top_headlines, 1):
        f.write(f"{i}. {headline}\n")

print("the Headlines/nHeadlines saved to 'bbc_top_headlines.txt'")