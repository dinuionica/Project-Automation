# Copyright 2021 Dinu Ion-Irinel

# import needed
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys

# init the driver for browser
driver = webdriver.Chrome("/usr/bin/chromedriver")

# the function that automates the creation of a new project
def create_project():

    # extract username and password from informations file
    file = open("informations.txt", "r")
    username = file.readline()
    password = file.readline()

    # create the directory and open it with the name of argument
    directory_name = sys.argv[1]
    parent_directory = "/home/ionica/Documents/Projects/"
    path = os.path.join(parent_directory, directory_name)
    os.mkdir(path)
    # change the current directory
    os.chdir(path);

    # connect with github
    driver.get("https://github.com/login")

    # set username
    username_label = driver.find_element_by_xpath("//*[@id='login_field']")
    username_label.send_keys(username)

    # set password
    password_laber = driver.find_element_by_xpath("//*[@id='password']")
    password_laber.send_keys(password)

    # login button
    login_button = driver.find_element_by_xpath(
        "//*[@id='login']/div[4]/form/div/input[12]")
    login_button.click()

    # create new repository
    driver.get("https://github.com/new")

    repository_name = driver.find_element_by_xpath(
        "//*[@id='repository_name']")
    repository_name.send_keys(directory_name)

    # create repository 
    new_repo_button = driver.find_element_by_xpath(
        '//*[@id="new_repository"]/div[4]/button')
    new_repo_button.submit()

if __name__ == "__main__":
    create_project()
