# passwordbreachchecker
This Python script allows users to check if a specific password appears in the RockYou wordlist, a commonly used list of passwords that were exposed in a data breach that is used by bruteforce apps. 
Description
This Python script helps you to find out if your password is vulnerable to brute-force attacks. It does so by checking your password against the RockYou wordlist, which is commonly used in various types of cyber attacks.

Features
Superhero-themed ASCII art interface
Checks the vulnerability of a password against the RockYou wordlist
Calculates the time taken for the check

Installation
- Download the rockyou.txt wordlist and place it in /usr/share/wordlists/.( If it's compressed, unzip it:sudo gunzip /usr/share/wordlists/rockyou.txt.gz)
Clone this repository:
- git clone https://github.com/yourusername/yourrepository.git
Navigate to the directory:
- cd yourrepository

Usage
Run the script using Python 3:
python3 passwordbreachchecker.py
Follow the on-screen instructions. Enter the password you want to check, or enter 'q' to quit the application.

Dependencies
Python 3.x
RockYou wordlist
