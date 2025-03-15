# File Organizer CLI

tidyfs is a simple and efficient command-line tool to organize files in a directory by sorting them into folders based on their extensions. This tool also supports scheduling the file organization process using cron jobs.

## Features
- Automatically moves files into categorized folders based on their extensions.
- Supports custom directory paths.
- Allows scheduling file organization using cron jobs.
- Lightweight and easy to use.

## Installation
Ensure you have Python installed (>=3.6), then install the required dependencies:

```sh
pip install tidyfs
```

## Usage

### Organize Files

To organize files in a specific directory:
```sh
tidyfs move /path/to/directory
```

### Schedule Organization with Cron
To schedule file organization at a specific time:
```sh
tidyfs cron "0 2 * * *" /path/to/directory
```
This example runs the file organization process every day at 2 AM.

## Requirements
- Python 3.7+
- `typer` for CLI functionality
- `cron-validator` for validating cron expressions

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Pull requests and suggestions are welcome! Feel free to submit issues or contribute to improvements.