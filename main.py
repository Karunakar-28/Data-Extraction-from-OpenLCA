import olca_ipc as ipc
from helper import *


try:
    # Connect to the OpenLCA IPC server
    client = ipc.Client(8080)
    # get all process ids
    ids_list = get_all_process_ids(client)

except Exception as e:
    print("Connection to OpenLCA may have failed. Ensure IPC server is running in OpenLCA")
    print(f"More details about exception {e}")

print("Data extraction in progress ...")

# scrape the data
get_all_data(client,ids_list)

print("Data Collection Completed")


# Reference:
# https://greendelta.github.io/olca-schema/classes/Exchange.html
























