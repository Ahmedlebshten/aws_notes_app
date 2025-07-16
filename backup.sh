#!/bin/bash
TIMESTAMP=$(date +%F_%H-%M)
mysqldump -u root -p12345 notesdb > /mariadb-backup/notes_backup_$TIMESTAMP.sql
