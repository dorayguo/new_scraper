from selenium import webdriver
from selenium.webdriver.common.keys import Keys

student_input = input("What class do you want to check for availability?: ")

url = 'https://www.lsa.umich.edu/cg/default.aspx'
browser = webdriver.Edge('C:/Users/doray/msedgedriver.exe')
browser.get(url)

input_form = browser.find_element_by_xpath('//*[@id="contentMain_txtCourse"]')
input_form.send_keys(student_input)
input_form.send_keys(Keys.ENTER)

class_confirmation = browser.find_element_by_xpath('//*[@id="contentMain_panelResults"]/div[5]/div/div[1]/div/a/font').text
print("You are checking class availability for " + class_confirmation + "...\n")

browser.find_element_by_xpath('//*[@id="contentMain_panelResults"]/div[5]/div/div[1]/div/a').click()

classes_list = []
discussion = "DIS"
lab = "LAB"
availability = bool(False)
lab_or_discussion_required = bool(False)

# gather all classes
for class_row in browser.find_elements_by_class_name('clsschedulerow'):
    class_item = class_row.find_element_by_xpath('.//div[@class="col-md-12"]/div[1]')
    section = class_item.find_element_by_xpath('.//div[1]').text
    number = class_item.find_element_by_xpath('.//div[3]').text
    open_seats = class_item.find_element_by_xpath('.//div[5]').text
    wait_list = class_item.find_element_by_xpath('.//div[7]').text
    day_time = class_item.find_element_by_xpath('.//div[8]').text
    if discussion in section or lab in section:
        lab_or_discussion_required = bool(True)
    if open_seats == "0":
        continue
    if discussion in section or lab in section:
        availability = bool(True)
    each_class = section + " " + number + " -- Open Seats: " + open_seats
    if wait_list != "-":
        each_class += " -- Waitlist: " + wait_list
    each_class += " [" + day_time + "]"
    classes_list.append(each_class)

for c in classes_list:
    print(c)

if not classes_list:
    print("\nNo classes for " + class_confirmation + " are available :/")
elif availability == bool(False) and lab_or_discussion_required == bool(True):
    print("\nNo lab or discussion sections for " + class_confirmation + " are available :(")
else:
    print("\nToday's your lucky day! Classes are available for " + class_confirmation)
    print("Remember to check if the Day/Time works for you~")

further_input = input("Would you like to redirect to a possible [s]yllabus, [a]tlas profile, or do [n]othing? [s/a/n]?: ")
if further_input == "a":
    browser.find_element_by_xpath('//*[@id="contentMain_lnk_SearchforSyllabus"]').click()
elif further_input == "s":
    browser.find_element_by_xpath('//*[@id="contentMain_lnk_ART"]').click()
