import os
import requests
from bs4 import BeautifulSoup
from path_name_mappings import destination_path_pdf
from urllib3.exceptions import InsecureRequestWarning

# Wyłączenie ostrzeżeń dotyczących niezweryfikowanego certyfikatu SSL
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Folder {directory} został utworzony.")

def get_all_links(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('https://ans-gniezno.edu.pl/wp-content/'):
            links.append(href)

    return links

url = 'https://ans-gniezno.edu.pl/studenci/plany-zajec/'
links = get_all_links(url)

output_dir = destination_path_pdf
create_directory_if_not_exists(output_dir)

for link in links:
    response = requests.get(link, verify=False)
    if response.status_code == 200:
        file_path = os.path.join(output_dir, os.path.basename(link))
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print("Plik PDF został pobrany:", link)
    else:
        print(f"Nie udało się pobrać pliku PDF: {link}")