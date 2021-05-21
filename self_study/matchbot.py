from selenium import webdriver
from time import sleep
import os
from urllib.parse import urlparse

class MatchBot:
    CATEGORIES = ["animals", "fruits"]

    def __init__(self):
        # Set webdriver options to ignore "The system cannot find the file specified." warning
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=self.options)
        # Open chrome and go to game url
        url = "https://www.neok12.com/games/memory/memory.htm"
        self.driver.get(url)

    def set_cat(self, cat):
        select_xpath = "//select[@id='picSet']"
        # Find current category the game is on
        active_option = self.driver.find_element_by_xpath(f"{select_xpath}/option[@selected]")

        # Handle invalid category param scenarios or Auto-click dropdown based on category
        if cat.lower() == active_option.text.lower():
            print(f"Game is already set to {cat}")
        elif cat.lower() in self.CATEGORIES:
            select = self.driver.find_element_by_xpath(select_xpath)
            # Click on "Select Another Picture Set" dropdown
            select.click()
            # Choose category from dropdown
            option = self.driver.find_element_by_xpath(f"{select_xpath}/option[text()='{cat.title()}']")
            option.click()
            # Auto-accept alert message "Would you like to start over with the new picture set?"
            alert = self.driver.switch_to.alert
            if alert:
                alert.accept()
        else:
            print(f"{cat} is not a valid category. Please select from valid list: {self.CATEGORIES}")

    def click_tile(self, index):
        # Click img tile by name attribute
        tile = self.driver.find_element_by_xpath(f"//img[@name='mmi{index}']")
        tile.click()
    
    def reload(self):
        # Refresh browser
        self.driver.execute_script("location.reload()")

    def quit(self):
        # Close browser and terminate WebDriver session
        self.driver.quit()
        exit()

    def solve(self):
        """
        Brute force approach by clicking every tile and "remembering" each image
        while auto-solving when a match is found
        """
        # Key: img name, Value: index
        img_matches = {}
        # Current index
        i = 0

        while i < 36:
            # Wait for 0.8 seconds to prevent skipping clicks
            sleep(0.8)
            self.click_tile(i)

            # Extract img name from img src
            tile = self.driver.find_element_by_xpath(f"//img[@name='mmi{i}']")
            img_url = tile.get_attribute("src")
            parsed_url = urlparse(img_url)
            base_name = os.path.basename(parsed_url.path)
            img_name = base_name.replace(".gif", "") if base_name.endswith(".gif") else base_name.replace(".png", "")
            
            # If img name doesn't exist in dict, store in dict and initialize with single index
            if img_name not in img_matches:
                img_matches[img_name] = i   
            else:
                self.click_tile(img_matches[img_name])

            i += 1

    def cheat(self):
        """
        Scrapes answers and auto-solves first try by clicking on matching grid positions
        """
        # List of images indexed by grid position [0-35]
        answer_list = self.driver.execute_script("return map") # Execute JavaScript in browser to scrape answers from JS variable
        # Key: img name, Value: list of indices of matching pairs
        img_matches = {}

        # Set up answer data to process later
        for i, num in enumerate(answer_list):
            # If img name doesn't exist in dict, store in dict and initialize list with single index
            if f"img{num}" not in img_matches:
                img_matches[f"img{num}"] = [i]
            # if img name exists in dict, append index to list, completing a matching pair
            else:
                img_matches[f"img{num}"].append(i)

        # Iterates through all the matches and clicks the corresponding tiles on the grid
        for match in img_matches.values():
            # wait for 0.8 seconds to prevent skipping clicks
            sleep(0.8)
            for index in match:
                self.click_tile(index)

mb = MatchBot()