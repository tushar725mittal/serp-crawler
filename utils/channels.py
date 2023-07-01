import time, json
from selenium.common.exceptions import NoSuchElementException


def get_channel_links(driver, video_links, post_links, channel_links):
    """Get the channel links from the video links and save them to a JSON file"""
    print("Extracting channel links from the video links........")
    for video_link in video_links:
        # Navigate to the video page
        try:
            driver.get(video_link)
        except:
            continue

        # Wait for the page to load
        time.sleep(3)

        # Find the channel link on the page and add it to the list if it's not already there
        try:
            channel_link_elements = driver.find_elements(
                "css selector", "a.yt-simple-endpoint.style-scope.yt-formatted-string"
            )
            for channel_link_element in channel_link_elements:
                channel_link = channel_link_element.get_attribute("href")
                if channel_link not in channel_links and (
                    "@" in channel_link or "channel" in channel_link
                ):
                    channel_links.append(channel_link)
        except NoSuchElementException:
            # No channel link was found, so skip this video
            break

    print("Extracting channel links from the posts links........")
    for post_link in post_links:
        # Navigate to the post page
        driver.get(post_link)

        # Wait for the page to load
        time.sleep(2)

        # Find any YouTube channel links on the page and add them to the list if they are unique
        try:
            channel_links_elements = driver.find_elements(
                "css selector",
                "a.yt-simple-endpoint.style-scope.ytd-backstage-post-renderer",
            )
            for channel_link_element in channel_links_elements:
                channel_link = channel_link_element.get_attribute("href")
                if channel_link not in channel_links:
                    channel_links.append(channel_link)
        except NoSuchElementException:
            # No channel link was found, so skip this video
            break

    for channel_link in channel_links:
        print(channel_link)

    # Save the links to a JSON file
    with open("youtube_links.json", "w") as f:
        print("Saving the channel links to a youtube_links.json file.")
        json.dump({"channel_links": channel_links}, f)
