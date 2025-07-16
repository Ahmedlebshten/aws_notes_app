#!/bin/bash
TIMESTAMP=$(date +%F_%H-%M)
mysqldump notesdb > /mariadb-backup/notes_backup_$TIMESTAMP.sql

