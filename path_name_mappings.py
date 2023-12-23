#Zmienne z path docelowym do plikow

import socket
import os

full_hostname = socket.gethostname()
hostname_parts = full_hostname.split('-')

if len(hostname_parts) > 0:
    hostname = hostname_parts[0]
else:
    hostname = "default_user"

destination_path_pdf = f'/home/{hostname}/SIWB/PLANY_PDF/'
destination_filed_xlsx = f'/home/{hostname}/SIWB/PLANY_XLSX/'
output_precision_data = f'/home/{hostname}/SIWB/ForkFromXLSX/'
test_pdf = f'/home/{hostname}/SIWB/PLANY_PDF_Test/'


