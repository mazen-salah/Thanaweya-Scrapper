import threading
from queue import Queue
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SeatScraper:
    def __init__(self, thread_id, start_id, end_id, data_queue):
        self.thread_id = thread_id
        self.start_id = start_id
        self.end_id = end_id
        self.data_queue = data_queue

    def get_data(self, driver, seatNumber):
        driver.get("https://natega.youm7.com/Home")
        seatNo = driver.find_element(By.NAME, "seatNo")
        seatNo.send_keys(str(seatNumber))
        seatNo.send_keys(Keys.ENTER)
        time.sleep(1)
        try:
            section = driver.find_element(By.CSS_SELECTOR, "#pills-tab > li:nth-child(7) > span:nth-child(2)").text
            marks = float(driver.find_element(By.CSS_SELECTOR, "#pills-tab > li:nth-child(2) > h1").text)
            if section == "علمي علوم" and 348 <= marks <= 375:
                name = driver.find_element(By.CSS_SELECTOR, "#pills-tab > li:nth-child(1) > span:nth-child(2)").text
                school = driver.find_element(By.CSS_SELECTOR, "#pills-tab > li:nth-child(2) > span:nth-child(2)").text
                district = driver.find_element(By.CSS_SELECTOR, "#pills-tab > li:nth-child(3) > span:nth-child(2)").text
                data = [seatNumber, name, marks, school, district]
                self.data_queue.put(data)
        except Exception as e:
            print(f"Error occurred for seat number {seatNumber}: {e}")

    def scrape_seats(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        try:
            for seat_id in range(self.start_id, self.end_id + 1):
                try:
                    self.get_data(driver, seat_id)
                except Exception as e:
                    print(f"Error occurred for seat number {seat_id}: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            driver.quit()

def append_data(data):
    with open('data.csv', 'a', encoding="utf-8") as data_file:
        data_file.write(','.join(map(str, data)) + '\n')
    print("Data Appended")

def main():
    num_threads = 5
    threads = []
    data_queue = Queue()

    start_id = int(input("Enter the start ID: "))
    end_id = int(input("Enter the end ID: "))

    range_per_thread = (end_id - start_id + 1) // num_threads

    for i in range(num_threads):
        if i == num_threads - 1:
            end_id_thread = end_id
        else:
            end_id_thread = start_id + (i + 1) * range_per_thread - 1

        scraper = SeatScraper(i, start_id, end_id_thread, data_queue)
        thread = threading.Thread(target=scraper.scrape_seats)
        thread.start()
        threads.append(thread)

        start_id = end_id_thread + 1

    for thread in threads:
        thread.join()

    while not data_queue.empty():
        data = data_queue.get()
        append_data(data)

    print("Scraping is done.")

if __name__ == "__main__":
    main()
