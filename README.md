# ICS344project

## Phase One

In the first phase, we started by importing the iso image of metasploitable3 using virtualbox. After that, we updated Metasploit on the Kali machine.
We configured the two machines using a virtual NAT network to determine connectivity and find the victim machine to target it. We tried to do a ping scan using Nmap with the following command <code>nmap -sn 10.0.2.0/28</code>

![image](https://github.com/user-attachments/assets/209f37d4-9a70-4792-b892-49c6b1ae4d03)

From the following output, we can determine there are two active virtual machines: one is the Kali linux that I'm currently using, and the other is our victim.

### TASK 1.1:Use Kali Linux tool Metasploit to compromise the service

From the list of available vulnerable services on Metasploitable3, we chose **SSH** as the service that we wanted to attack. Our attack is a **brute-force attack** to determine the credentials of the machine to gain access.
we first start the metasploitable using the following command <code>msfconsole</code> then we used <code>use auxiliary/scanner/ssh/ssh_login</code> to set the attack we want to use then we determine our target using
<code>set RHOST 10.0.2.15</code> then we did set both our user list and our password list. to make the attack

![image](https://github.com/user-attachments/assets/dece770e-5e1b-495b-b528-1a26763eccd4)

From the picture, we can determine that our attack was successful; we got access there, for there is a pair of passwords and usernames that is correct in our list. And the pair is also shown in the picture <code>vagrant:vagrant</code>

in Summary:
- Tool: Metasploit using <code>ssh_login</code>
- Configuration: two lists of words for username and password
- Attack was successful using the tool
- NOTE: The username file and password file must contain the correct password and username among other passwords and usernames
