import requests
import argparse
from datetime import datetime
import os

# test getenv() method for api key management
api_key = os.getenv("API_KEY_FINGRID")

def getFingridData():
    # dir_path to save csv
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # two datetimes for default endTime and csv filename
    dtToday = datetime.today().strftime("%Y-%m-%d")
    now = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    # parser manages command line options, prints helps and makes them callable
    parser = argparse.ArgumentParser(description ='Get data from Fingrids open data site', 
                                     usage="example: python3 filename.py 124 2024-10-10 2024-11-10")

    parser.add_argument("datasetId", type=int, help="Integral")
    parser.add_argument("startTime", type=str, nargs="?", default="2000-01-01", help="yyyy-mm-dd")
    parser.add_argument("endTime", type=str, nargs="?", default=now, help="yyyy-mm-dd")
    parser.add_argument("--format", type=str, nargs="?", default="json", help="json(default), csv, xml")
    parser.add_argument("--pageSize", type=int, nargs="?", default=10, help="How many pageSizes of data you want to use? default = 10" )
    parser.add_argument("--verbose", action="store_true", help="program prints more information")
    parser.add_argument("--toFile", action="store_true", help="creates a file for the data in csv format")
    args = parser.parse_args()

    datasetId = args.datasetId
    startTime = args.startTime
    endTime = args.endTime
    format = args.format
    pageSize = args.pageSize

    try:
        # build url for the req. could have used f string but this method was familiar from school
        url = "https://data.fingrid.fi/api/datasets/{0}/data?startTime={1}&endTime={2}&format={3}&pageSize={4}".format(
            datasetId, startTime, endTime, format, pageSize)
        # hidden api key usage to header
        hdr ={'x-api-key': api_key}

        req = requests.get(url, headers=hdr)

        # print url and req status code for testing the api quickly
        print(f"URL: {url}")
        print(f"Status code: {req.status_code}")

        # xml got least love from me, you can see if the api is working with it and print the data with --verbose
        if args.format == "xml":
            if args.verbose:
                print(req.text)
            return

        # json is the default option 
        jsondata = req.json()
        if args.verbose:
            print(jsondata)

        # data to csv. csvdata gets the data part from the jsondata, and this writes it to file in cwd
        if args.toFile and args.format == "csv":
            # if get method finds "data"-key, data goes to csvdata variable. otherwise csvdata is empty and results in empty file
            csvdata = jsondata.get("data", [])
            csvFile = open(f"{dir_path}/fingriddata{dtToday}.csv", "w")
            csvFile.write(csvdata)
            csvFile.close()
            print("CSV to file OK")
    # basic error handling which was actually quite nice
    except requests.exceptions.RequestException as e:
        print(e)
    return

getFingridData()