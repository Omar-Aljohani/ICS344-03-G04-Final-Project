# ICS344project

## Phase One

In the first phase, we started by importing the iso image of metasploitable3 using virtualbox. After that, we updated Metasploit on the Kali machine.
We configured the two machines using a virtual NAT network to determine connectivity and find the victim machine to target it. We tried to do a ping scan using Nmap with the following command <code>nmap -sn 10.0.2.0/28</code>

![image](https://github.com/user-attachments/assets/209f37d4-9a70-4792-b892-49c6b1ae4d03)

From the following output, we can determine there are two active virtual machines: one is the Kali linux that I'm currently using, and the other is our victim.

### TASK 1.1: Use Kali Linux tool Metasploit to compromise the service

From the list of available vulnerable services on Metasploitable3, we chose **SSH** as the service that we wanted to attack. Our attack is a **brute-force attack** to determine the credentials of the machine to gain access.
we first start the metasploitable using the following command <code>msfconsole</code> then we used <code>use auxiliary/scanner/ssh/ssh_login</code> to set the attack we want to use then we determine our target using
<code>set RHOST 10.0.2.15</code> then we did set both our user list and our password list. to make the attack

![image](https://github.com/user-attachments/assets/dece770e-5e1b-495b-b528-1a26763eccd4)

From the picture, we can determine that our attack was successful; we got access there, for there is a pair of passwords and usernames that is correct in our list. And the pair is also shown in the picture <code>vagrant:vagrant</code>

In summary:
- Tool: Metasploit using <code>ssh_login</code>
- Configuration: two lists of words for username and password
- Attack was successful using the tool
- NOTE: The username file and password file must contain the correct password and username among other passwords and usernames

### TASK 1.2: Compromise the service using a custom script that you create (an automated script that compromises the target and shows a Proof of Concept).

For the second task, I will use Python with the paramiko package to install it. Run the following command: <code>sudo apt install python3-paramiko</code>
We will use paramiko to create a session and make an SSH login attempt. to code is simple to prove a concept. It one a file of usernames and reads it line by line, then  takes each line and tries each password possible in a second file.
For the code to work, you must set up the correct configuration at the top of the script.
```python
  target_ip = '10.0.2.15'  # Replace with your Metasploitable IP
  username_file_path = 'users.txt'
  password_file_path = 'passwords.txt'
```
I have provided dummy data in the folder /phase1 for users.txt and passwords.txt

![image](https://github.com/user-attachments/assets/b986cfed-cd54-4ee7-9b04-a786dabf61df)

The output will show each attempt with the user and the password used for that attempt, followed by an indication if the attempt failed or was successful.
At the end, the script will print a message telling the user if it successfully found an account to login; if it did, it will print a dictionary containing the account
that succeeded in the login attempt.

![image](https://github.com/user-attachments/assets/0ce73da6-b630-4908-9b11-387c3b4cb4d6)

# Phase 2 - Visual Analysis with a SIEM Dashboard

## Overview
In this phase, we set up a SIEM environment using Splunk to collect and visualize attack logs from the Metasploitable3 victim machine. We specifically focused on detecting and analyzing SSH brute-force attacks.

---

## Steps Completed

1. **Environment Setup**
   - Followed the official guidelines to set up the Metasploitable3 VM in VirtualBox.
   - Installed Kali Linux VM and downloaded the Metasploit Framework to perform attacks against the victim machine.

2. **Splunk Installation**
   - Installed Splunk on the Kali Linux machine to act as the SIEM server.
   - Installed Splunk Universal Forwarder on the Metasploitable3 machine to forward logs.

3. **Log Forwarding**
   - Configured the Splunk Universal Forwarder to send `/var/log/auth.log` from Metasploitable3 to the Splunk server on Kali.
   - Verified that logs were received successfully in Splunk's **Search & Reporting → Data Summary**.

4. **Filtering SSH Attack Logs**
   - Used the following search query to filter SSH login attempts:
     ```spl
     index=* sourcetype=syslog host="metasploitable3-ub1404" (sshd AND ("Failed password" OR "Accepted password"))
     ```
   - This query allowed isolating SSH login events for further analysis.
   - ![logs from both environments](https://github.com/user-attachments/assets/c1a81480-4f86-4f59-b71c-df79f0f46691)


5. **Attack Visualization and Analysis**
   - Used the following search query to classify attacks and extract attacker IP addresses:
     ```spl
     index=* sourcetype=syslog host="metasploitable3-ub1404" (sshd AND ("Failed password" OR "Accepted password"))
     | eval attack_type=if(like(_raw, "%Failed password%"), "SSH Failed Login", "SSH Successful Login")
     | rex "from\s(?<src_ip>\d+\.\d+\.\d+\.\d+)"
     | eval attack_category="SSH Attack"
     | stats count by src_ip, attack_category, attack_type
     | sort - count
     ```
   - Visualization was created as a **bar chart** showing:
     - Attacker IP addresses
     - Attack types (SSH Failed Login or SSH Successful Login)
     - Number of attempts
   - This provided clear visibility into attack patterns and sources.
   - ![attack visualization and analysis](https://github.com/user-attachments/assets/e789cf76-5ffa-49aa-8801-9875b044d20d)


---



