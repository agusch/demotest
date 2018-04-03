*** Settings ***
Documentation     A test suite with a single test for valid login.
...
Resource          ../Resource/resource.robot

*** Test Cases ***
Valid Auth
    Custom Basic Auth  ${AUTH URL}  ${USER}  ${PASSWORD}
    Check Status  ${200}
    Check Authenticated  ${True}

Valid Get
    Custom Get  ${GET URL}
    Check Status  ${200}

Valid Stream
    Custom Stream  ${STREAM URL}  ${20}
    Check Status  ${200}
    Check Lines  ${20}

Header Check
    Custom Get  ${GET URL}
    &{a}=  Get Headers
    Should Be Equal  httpbin.org  &{a}[Host]
