from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


def search_results(driver, search_query):
    """Search for the given query for first 10000 results and return a list of youtube video links, post links and channel links that appears in the search results"""
    # Navigate to the Google search page
    driver.get("https://www.google.com")

    # Find the search box and enter the search query
    search_box = driver.find_element("name", "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for the page to load
    time.sleep(2)

    # Initialize a list to store the links
    video_links = []
    post_links = []
    channel_links = []

    # Loop until we have 10000 links or we reach the end of the search results
    print("Searching for Youtube Links on the page........")
    while len(video_links) + len(channel_links) + len(post_links) < 10000:
        # Find all the search result links on the page
        result_links = driver.find_elements("css selector", "a")

        # Loop through the links and add any YouTube video links to the list of video links, Youtube post links to post links and any YouTube channel links to the list of channel links if they're not already there
        for link in result_links:
            href = link.get_attribute("href")
            if href and "&t=" in href:
                href = href.split("&t=")[0]
            if href and "youtube.com/watch" in href and href not in video_links:
                video_links.append(href)
            elif href and "youtube.com/post" in href and href not in post_links:
                post_links.append(href)
            elif href and ("youtube.com/channel" in href and href not in channel_links):
                channel_links.append(href)

        # Click the "Next" button to go to the next page of results if there is one and wait for the page to load
        try:
            next_button = driver.find_element("id", "pnnext")
            next_button.click()
        except NoSuchElementException:
            # No "Next" button was found, so this is the last page of results
            break

        # Wait for the page to load
        time.sleep(2)

    print("Serching for Youtube Links on the page completed........")
    return video_links, post_links, channel_links
