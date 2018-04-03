*** Settings ***
Library           ../Libraries/custom_lib.py

*** Variables ***
${SERVER}           httpbin.org
${USER}             user
${PASSWORD}         password
${GET URL}          http://${SERVER}/get
${STREAM URL}       http://${SERVER}/stream
${AUTH URL}         http://${SERVER}/basic-auth/user/password
