
# Git Logs

This code is a script that fetches git logs for multiple repositories, extracts relevant information, and saves it into a CSV file. It uses the argparse module to parse command-line arguments and accepts various options such as specifying starting and ending dates, filtering by authors, creating an email, sending an email, and increasing verbosity. The script iterates over each repository, updates the local branches, fetches logs, and extracts information such as author, date, branch, number of commits, files changed, insertions, deletions, and comments. Finally, it creates a CSV file with the extracted information.

Email feature is not ready yet.

## Installation

Download the distribution file located at dist (only .exe file, soon will be available for Linux). Or download the source code.

## Usage
Download the distribution file (windows only) located at dist and run:

```bash
git-logs [-h] [-u UNTIL] [-a AUTHORS] [-e] [-s] [-v] [-d DIRECTORY] [--csv-config CSV_CONFIG] since

Get git logs and save them into a CSV file

positional arguments:
  since                 Starting date for getting logs. Ex: "today" or "yesterday" or "April 20, 2023" or "2023-08-01"

options:
  -h, --help            show this help message and exit
  -u UNTIL, --until UNTIL
                        Starting date for getting logs. If is not specified, "today" will be used (default: None)
  -a AUTHORS, --authors AUTHORS
                        List of developers will get the logs (default: None)
  -v, --verbose         Increase verbosity (default: False)
  -d DIRECTORY, --directory DIRECTORY
                        Path to git repositories (default: Current path)
  --csv-config CSV_CONFIG
                        CSV config file path. Ex: "csv.yaml" (default: if not specified, "csv.yaml" will be created and used)
```

### Windows
```./git-logs.exe --help```

### Linux

Clone the repository (requires python 3 or higher) and run:

```bash
./git-logs.py --help
```

## Contributing

If you would like to contribute to this project, please open an issue or send a pull request.
