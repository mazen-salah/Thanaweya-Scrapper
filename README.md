# Seat Scraper Project

This is a Python project created by Mazen Tamer for scraping data from a website called "natega.youm7.com." The project uses multi-threading to fetch data for a range of seat numbers and store the results in a CSV file.

## Prerequisites

Before running this project, make sure you have the following dependencies installed:

- [Python](https://www.python.org/downloads/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [Chrome WebDriver](https://sites.google.com/chromium.org/driver/)
- [Queue](https://docs.python.org/3/library/queue.html)

## Getting Started

1. Clone this repository to your local machine or download the project files.
   
2. Install the required Python libraries mentioned in the Prerequisites section using `pip`:

   ```bash
   pip install selenium
   ```
   
3. Download the [Chrome WebDriver](https://sites.google.com/chromium.org/driver/) for your specific version of Google Chrome and place the driver executable in the same directory as the project files.

## Usage

1. Run the `main()` function in the `seat_scraper.py` script.

2. You will be prompted to enter the start and end seat IDs for the range you want to scrape.

3. The script will use multiple threads to fetch data for the specified range of seat numbers.

4. The data will be appended to a CSV file named `data.csv` in the same directory.

## Example

Here's how you can use this script:

   ```bash
   python seat_scraper.py
   ```

You will be prompted to enter the start and end seat IDs. Once you provide the input, the script will start scraping the data.

## Data Format

The data will be stored in the `data.csv` file in the following format:
   ```bash
   SeatNumber,Name,Marks,School,District
   ```

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



