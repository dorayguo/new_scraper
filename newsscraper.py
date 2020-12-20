from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser

journal_input = input("The Atlantic or Scientific American? [a/s]: ")

# the latest at atlantic
if journal_input == "a":
    url = 'https://www.theatlantic.com/latest/'
    browser = webdriver.Edge('C:/Users/doray/msedgedriver.exe')
    browser.get(url)

    print("Searching for latest news in The Atlantic...")
    articles = browser.find_elements_by_class_name('blog-article')
    articles_list = []

    for article in articles:
        title = article.find_element_by_xpath('.//a/h2').text
        articles_list.append(title)

    x = 1
    for a in articles_list:
        print(str(x) + ". " + a)
        x += 1

    more_input = input("\nWhat article do you want to know more about or none? [#/n]: ")
    while more_input != 'n' and more_input != '':
        description = articles[int(more_input) - 1].find_element_by_xpath('.//p').text
        print("\n" + description + "\n")
        next_input = input("Would you like to read the article? [y/n]: ")
        if next_input == "y":
            link = articles[int(more_input) - 1].find_element_by_xpath('.//a').get_attribute('href')
            print(link)
            webbrowser.open_new_tab(link)
        more_input = input("\nWhat article are you interested in or none? [#/n]: ")

# the latest at scientific american
elif journal_input == "s":
    url = 'https://www.scientificamerican.com/section/lateststories/?page=1'
    browser = webdriver.Edge('C:/Users/doray/msedgedriver.exe')
    browser.get(url)

    print("Searching for latest news in Scientific American..")
    articles = browser.find_elements_by_class_name('listing-wide')
    articles_list = []

    for article in articles:
        title = article.find_element_by_xpath('.//div[@class="listing-wide__inner"]/h2').text
        articles_list.append(title)

    x = 1
    for a in articles_list:
        print(str(x) + ". " + a)
        x += 1

    next_input = input("Would you like to read an article? [#/n]: ")
    while next_input != 'n':
        link = articles[int(next_input) - 1].find_element_by_xpath('.//div[@class="listing-wide__inner"]/h2/a').get_attribute('href')
        print(link)
        webbrowser.open_new_tab(link)
        articles_left = browser.find_element_by_xpath('//*[@id="spw-article-count"]')
        print("\nYou have " + articles_left + " articles left to read today!")
        next_input = input("\nWould you like to read another article? [#/n]: ")

print("\nIt was a pleasure learning with you! Have a great day :)")
