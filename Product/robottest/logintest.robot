*** Settings ***
Documentation     A test suite for valid and invalid login scenarios

Resource          resources.robot

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Login Page Should Be Open

Login Page Should Be Open
    Title Should Be    Login page

Go To Login Page
    Go To    ${LOGIN URL}
    Login Page Should Be Open

Input Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Click Button    login-button

Welcome Page Should Be Open
    Location Should Be    ${WELCOME URL}
    Title Should Be    Edit page

Invalidlogin Page Should Be Open
    Location Should Be    ${ERROR URL}
    Title Should Be    Login page


*** Test Cases ***
Invalid Login
    Open Browser To Login Page
    Input Username    Invalid
    Input Password    Invalid
    Submit Credentials
    Invalidlogin Page Should Be Open
    [Teardown]    Close Browser

Valid Login
    Open Browser To Login Page
    Input Username    admin
    Input Password    admin123
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser
