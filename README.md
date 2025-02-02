# Fingrid Data Fetcher

This Python script fetches time series data from Fingrid's open data API.

This program is **not designed** for downloading entire datasets.  
If you need **all data**, download it directly from **Fingrid’s website**.

## Usage

1. **Fetch a latest single page and display data in the terminal**
    ```
    python3 filename.py 124 --pageSize 1 --verbose
    ```

2. **Fetch and display demo data in the terminal**
    ```
    python3 filename.py 124 --verbose
    ```

3. **Fetch more data in a single request**
Here the pageSize is kinda funky. The value 500 is enough to get the months data, but its overkill. Good pageSize
depends on the measurement time interval. Adjust based on measurement interval. For example 15min intervals on a solid data would be 96(24*4) for one day data. Overkill value for pageSize works, but it is not optimal.

    ```
    python3 filename.py 124 2020-10-10 2020-11-10 --pageSize 500 --verbose
    ```

4. **Save data to a CSV file**
    ```
    python3 filename.py 124 2020-10-10 2020-11-10 --format csv --toFile --pageSize 96
    ```

## Parameters

| Parameter      | Description |
|---------------|------------|
| `datasetId` (Required) | The dataset ID to fetch |
| `startTime` (Default: 2000-01-01) | Start date (yyyy-mm-dd) |
| `endTime` (Default: now) | End date (yyyy-mm-dd) |
| `--format` (Default: json) | json, csv, or xml |
| `--pageSize` (Default: 10, works as demo size to check data) | Number of records per request |
| `--verbose` | Displays the retrieved data in the terminal |
| `--toFile` | Saves the data as a CSV file |

