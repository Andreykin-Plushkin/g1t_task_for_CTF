
if grep -wq "SECRET_KEY" .env
then
	echo "[!] Key is exist. Skipping..."
else
	echo "[+] Generate new key"
	KEY=$((RANDOM%31+25))
	echo "export SECRET_KEY=${KEY}" >> .env
fi
