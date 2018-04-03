*** Settings ***
Documentation     Example test cases using the data-driven testing approach.
...
Test Template     Authenticate
Resource          ../Resource/resource.robot

*** Test Cases ***    Expression    Expected
Good Login
    ${AUTH URL}  user  password


Bad Logins     [Template]    Authenticate should fail
    ${AUTH URL}  ${EMPTY}  password
    ${AUTH URL}  user  ${EMPTY}
    ${AUTH URL}  ${SPACE}  password
    ${AUTH URL}  user  ${SPACE}


*** Keywords ***
Authenticate 
    [Arguments]  ${a}  ${b}  ${c}
    ${d}=  Custom Basic Auth  ${a}  ${b}  ${c}  
    Should Be Equal  ${200}  ${d}  

Authenticate should fail
    [Arguments]  ${a}  ${b}  ${c}
    ${d}=  Custom Basic Auth  ${a}  ${b}  ${c}  
    Should Be Equal  ${401}  ${d}  

