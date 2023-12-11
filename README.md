# passwordbreachchecker
The Password Breach Checker is a Python script designed to assess the security of passwords. It checks a given password against the RockYou wordlist, a compilation of passwords exposed in a data breach and frequently used by brute-force attack tools.

# Installation Steps:

Ensure Kali Linux distribution is being used, as it comes with the necessary tools and environment.
Download and place the rockyou.txt wordlist in /usr/share/wordlists/.

If the wordlist is compressed, decompress it using:

```sudo gunzip /usr/share/wordlists/rockyou.txt.gz```

Clone Repository:

```git clone https://github.com/YeranG30/passwordbreachchecker.git```

Navigate to Directory:

```cd passwordbreachchecker```

Usage

```python3 pwdchecker.py```

# Section 1: Project Overview

<img width="879" alt="image" src="https://github.com/YeranG30/passwordbreachchecker/assets/74067706/dbb62eb8-4910-4904-a25e-e77525437175">

The Password Breach Checker is a Python-based tool designed to enhance cybersecurity awareness and practices. It allows users to check if their passwords are part of the RockYou wordlist - a compilation of passwords exposed in past data breaches and often used for brute-force attacks.

# Section 2: Key Features
Password Vulnerability Check: Cross-references user-inputted passwords against the RockYou wordlist to check for potential vulnerabilities.
<img width="543" alt="image" src="https://github.com/YeranG30/passwordbreachchecker/assets/74067706/b213bacb-2750-4690-a952-cd4d025c94fd">


Time Efficiency Analysis: Calculates and displays the time taken to search the wordlist, showcasing the script's efficiency.



Dependencies
- Python 3.x
- RockYou wordlist

