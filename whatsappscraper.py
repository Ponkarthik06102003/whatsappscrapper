from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from whatsapp_group_contacts_scraper import WhatsAppGroupContactsScraper

# Path to your ChromeDriver executable
webdriver_service = Service('path/to/chromedriver.exe')

# Path to your Chrome profile directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=/path/to/chrome/profile')

# Initialize ChromeDriver with the configured options
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code manually
input('Please scan the QR code and press Enter to continue...')

# Find and click on the desired group
group_name = input('Enter the name of the group: ')
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.send_keys(group_name)
sleep(2)  # Wait for search results to load
group = driver.find_element(By.XPATH, f'//span[@title="{group_name}"]')
group.click()

# Wait for the group to load
sleep(5)

# Find the participants section and click on it
participants_button = driver.find_element(By.XPATH, '//div[@title="Participants"]')
participants_button.click()

# Wait for the participants list to load
sleep(2)

# Scrape participant details using WhatsApp-Group-Contacts-Scraper library
scraper = WhatsAppGroupContactsScraper(driver)
participant_details = scraper.get_participant_details()

# Extract required information from participant details
participant_count = len(participant_details)
participant_names = [participant['name'] for participant in participant_details]
participant_phone_numbers = [participant['phone_number'] for participant in participant_details]
participant_statuses = [participant['status'] for participant in participant_details]
participant_cleaned_statuses = [participant['cleaned_status'] for participant in participant_details]
participant_admins = [participant['admin'] for participant in participant_details]

# Print the participant count
print(f'Participant Count: {participant_count}')

# Print participant names
print("Participant Names:")
for name in participant_names:
    print(name)

# Print participant phone numbers
print("Participant Phone Numbers:")
for phone_number in participant_phone_numbers:
    print(phone_number)

# Print participant WhatsApp statuses
print("Participant WhatsApp Statuses:")
for status in participant_statuses:
    print(status)

# Print participant cleaned statuses
print("Participant Cleaned Statuses:")
for cleaned_status in participant_cleaned_statuses:
    print(cleaned_status)

# Print participant admin details
print("Participant Admins:")
for admin in participant_admins:
    print(admin)

# Close the browser
driver.quit()
