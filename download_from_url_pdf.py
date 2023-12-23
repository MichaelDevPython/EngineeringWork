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
        if href and href.startswith('https://ans-gniezno.edu.pl/wp-content/') and 'wykaz-tygodni' not in href:
            links.append(href)

    return links

def download_and_update_files(links, output_dir):
    existing_files = set(os.listdir(output_dir))

    # Usuń pliki lokalne, których nie ma na liście linków
    for local_file in existing_files:
        local_file_path = os.path.join(output_dir, local_file)
        if local_file not in [os.path.basename(link) for link in links]:
            os.remove(local_file_path)
            print("Usunięto nieaktualny plik:", local_file_path)

    # Pobierz lub zaktualizuj pliki zgodnie z listą linków
    for link in links:
        response = requests.get(link, verify=False)
        if response.status_code == 200:
            file_name = os.path.basename(link)
            file_path = os.path.join(output_dir, file_name)

            # Sprawdź, czy plik jest aktualny
            if os.path.exists(file_path) and file_name == os.path.basename(file_path):
                print("Plik PDF jest już aktualny:", link)
            else:
                # Pobierz nowy plik lub zaktualizuj istniejący
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                if os.path.exists(file_path):
                    print("Plik PDF został zaktualizowany:", link)
                else:
                    print("Plik PDF został pobrany:", link)

url = 'https://ans-gniezno.edu.pl/studenci/plany-zajec/'
links = get_all_links(url)

output_dir = destination_path_pdf
create_directory_if_not_exists(output_dir)

download_and_update_files(links, output_dir)
