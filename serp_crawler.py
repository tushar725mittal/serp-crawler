from selenium import webdriver
from utils import channels, search


# main function
def main():
    # Selemium web driver is used to do the search and extracting the links. Initializing the chrome webdriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome("./chromedriver", options=options)
    driver.minimize_window()  # minimize the window to avoid any interruption

    search_query = "site:youtube.com openinapp.co"
    video_links, post_links, channel_links = search.search_results(driver, search_query)
    channels.get_channel_links(driver, video_links, post_links, channel_links)

    driver.quit()


# call main function
if __name__ == "__main__":
    main()
