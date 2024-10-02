
# Domain Discovery - xreverselabs.org API

![server](https://raw.githubusercontent.com/xReverseLabs/Domain-Discovery-python/refs/heads/main/img/server.gif)

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Domain Discovery is a simple tool that leverages the API from [xreverselabs.org](https://xreverselabs.org) to automatically find and store domains. This tool supports domain scraping in multiple iterations, with configurable delays between requests, and ensures that no duplicate results are stored during the scraping process.

## Features
- **Automated Scraping**: Automatically fetch domain data from the xreverselabs.org API.
- **Random User-Agent**: Uses `fake_useragent` to simulate a real browser request with varied User-Agent headers.
- **Duplicate-Free Domains**: Ensures no duplicate domains are saved between scraping requests.
- **Colored Output**: Uses the `colorama` library for colored terminal output, making it easier to read.
- **Save Results**: Automatically saves the scraping results in a `result_discover.txt` file.

## Preview

![preview](https://raw.githubusercontent.com/xReverseLabs/Domain-Discovery-python/refs/heads/main/img/preview.png)

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## Requirements

Before running this tool, make sure you have the following:
- Python 3.8 or higher
- An API key from xreverselabs.org (Use `FREE-TRIAL` for a free version)
- A few Python libraries that need to be installed (see the [Installation](#installation) section)

## Installation

1. Clone this repository to your local directory:

    ```bash
    git clone https://github.com/xReverseLabs/Domain-Discovery-python.git
    cd domain-discovery
    ```

2. Install all the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

    **requirements.txt** will include the following:
    ```text
    requests
    fake_useragent
    colorama
    ```

3. Once all dependencies are installed, you are ready to run the tool!

## Usage

1. Run the main script using the following command:

    ```bash
    python Domain_Discovery.py
    ```

2. Upon running, you will be prompted to enter the number of iterations (how many times the scraping will be performed) and the delay in seconds between each request. For example:

    ```
    Enter how many times to scrape: 10
    Enter delay between requests (in seconds): 5
    ```

3. The scraping results will be printed in the terminal and saved in a `result_discover.txt` file. If a domain already exists from previous requests, the tool will avoid storing duplicates.

### Sample Output

```

[Scraping Attempt 1]
15 new domains found.
New results saved to result_discover.txt

[Scraping Attempt 2]
No new domains found in this request.

[Scraping Attempt 3]
8 new domains found.
New results saved to result_discover.txt
```

The `result_discover.txt` file will look like this:
```
example.com
sample.net
domain.org
...
```

## Contribution

Contributions are welcome! If you would like to contribute, please fork this repository and submit a pull request with improvements or new features. You can also open an issue if you find any bugs or have feature ideas.

### Steps to contribute:
1. Fork this repository
2. Create a new feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

