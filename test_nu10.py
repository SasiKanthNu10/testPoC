import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def setup():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Quit the WebDriver after the test completes
    driver.quit()

def test_form_filling_and_submission(setup):
    driver = setup
    # Navigate to the website
    driver.get("https://nu10.co/")

    # Clicking on the contact button
    contact_btn = driver.find_element(By.XPATH, "//*[text()='Contact']").click()

    # Verify the landing page
    lnd_page = driver.find_element(By.XPATH,"//h1[@class='elementor-heading-title elementor-size-default']")
    assert lnd_page.text == "Contact Us"

    # Fill in the form fields
    name_field = driver.find_element(By.NAME, "firstname")
    name_field.send_keys("Prakash")

    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.send_keys("9700023539")

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("prakash@nu10.co")

    msg_field = driver.find_element(By.NAME, "message")
    msg_field.send_keys("Hello, Just testing please ignore!")

    # Submit the form
    submit_button = driver.find_element(By.XPATH,"//input[@type='submit']")
    submit_button.click()

    # Wait for the submission to complete and the result to load
    time.sleep(5)

    # Verify the submission by checking for a success message
    success_message = driver.find_element(By.XPATH,"//div[@class='wpcf7-response-output']")
    assert success_message.text == "Thank you for your message. It has been sent."

def test_form_without_filling(setup):
    driver = setup
    # Navigate to the website
    driver.get("https://nu10.co/")

    # Clicking on the contact button
    contact_btn = driver.find_element(By.XPATH, "//*[text()='Contact']").click()

    # Submit the form
    submit_button = driver.find_element(By.XPATH,"//input[@type='submit']")
    submit_button.click()

    # Wait for the submission to complete and the result to load
    time.sleep(5)

    # Verify the submission by checking for a error message
    err_message = driver.find_element(By.XPATH,"//div[@class='wpcf7-response-output']")
    assert err_message.text == "One or more fields have an error. Please check and try again."
