🛠 DevOps Project: Deploy a Note-Taking Web App on AWS EC2 with Backup Strategy
📘 Project Title
Deploy a Note-Taking Website on AWS EC2 with Backup Strategy (Flask + MariaDB + EBS Backup)
________________________________________
🎯 Overview
This project demonstrates the deployment of a simple Flask-based note-taking web application on an Amazon EC2 instance running RHEL 9, connected to a MariaDB database, and implements a backup strategy using an attached EBS volume. The goal is to apply DevOps and Linux system administration concepts by provisioning cloud infrastructure, deploying a backend application, configuring services, and automating backups.
________________________________________
🧰 Technologies Used
•	Amazon EC2 (RHEL 9, t2.micro)
•	Flask (Python 3)
•	MariaDB (SQL)
•	Amazon EBS Volume (for backup)
•	cron jobs
•	bash scripting
________________________________________
📦 Project Structure
/home/ec2-user/note-app
├── app.py , backup.sh        # Flask web application

/mariadb                      # Mounted EBS volume for MariaDB data
└── mysql                     # MariaDB data directory

/mariadb-backup               # Mounted EBS volume for database backups
└── notes_backup_YYYY-MM-DD.sql
________________________________________
✅  Project Requirements & Setup
1. ✅  Launch EC2 Instance (RHEL 9)
•	Instance Type: t2.micro
•	OS: Red Hat Enterprise Linux 9 (RHEL 9)
•	Configure Security Group to allow:
o	SSH (TCP 22) from 0.0.0.0/0
o	HTTP (TCP 80) from 0.0.0.0/0
________________________________________
2. ✅  SSH Access
ssh -i "devops.pem" ec2-user@<your-ec2-public-dns>
________________________________________
3. ✅  Install Python, Flask, and Tools
sudo dnf install python3 -y
sudo dnf install git -y
sudo dnf install nano -y
sudo python3 -m pip install flask mysql-connector-python
________________________________________
4. ✅  Install MariaDB Server
sudo dnf install mariadb-server -y
sudo systemctl enable mariadb
sudo systemctl start mariadb
________________________________________
5. ✅  Setup MariaDB Database and User
sudo mysql -u root
CREATE DATABASE notesdb;
CREATE USER '****'@'localhost’ IDENTIFIED BY '****';
GRANT ALL PRIVILEGES ON notesdb.* TO 'root';
FLUSH PRIVILEGES;
EXIT;
Create the table:
USE notesdb;
CREATE TABLE notes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
________________________________________
6. ✅  Flask Web App (app.py)
Run the app:
sudo python3 app.py
________________________________________
💾 Create EBS Volume for Data and Backup
1. ✅  Create 2 EBS volumes in the same AZ
2. ✅  Attach them to EC2 instance  
3. ✅  Format and Mount them
Firs disk to store data:
sudo mkfs -t ext4 /dev/xvdb
sudo mkdir /mariadb
sudo mount /dev/xvdb /mariadb

second disk to backup:
sudo mkfs -t ext4 /dev/xvdc
sudo mkdir /mariadb-backup
sudo mount /dev/xvdc /mariadb-backup
To make mount persistent, add to /etc/fstab:
________________________________________
🔁 Setup Backup Automation (Daily mysqldump)
✅  1. Create a script: /usr/local/bin/backup.sh
#!/bin/bash
TIMESTAMP=$(date +%F)
mysqldump -u **** -p**** notesdb > / mariadb-backup/notes_backup_$TIMESTAMP.sql
sudo chmod +x /usr/local/bin/backup.sh
✅  2. Edit Cronjob:
sudo crontab -e
Add this line:
0 2 * * * /usr/local/bin/backup.sh
This will back up the database every day at 2 AM.
________________________________________
📷 Screenshots 
•	✅  EC2 instance running 
•	✅  Flask app UI
•	✅  Database structure
•	✅  List all partitions and hard disks  
•	✅  EBS volumes  
•	✅  Backup file: /mariadb-backup/notes_backup
 
________________________________________
🧪 Testing
•	Added multiple notes through browser
•	Verified data stored in MariaDB using:
sudo mysql -u **** -p****
USE notesdb;
SELECT * FROM notes;
•	Verified backup files exist:
ls -lh /mariadb-backup
________________________________________

