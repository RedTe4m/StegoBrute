# StegoBrute
A script designed to brute force some password protected steganography files.

Intended to crack files with embedded text created using the steghide program.

Requires: python3+ and steghide
To install steghide on Debian Linux (Kali, BackBox, Ubuntu, etc.), fun the command 'apt-get update && apt-get install -y steghide'

To use: Put they StegoBrute.py in a folder with the .jpg file that you think might have embedded text along with a list of possible passwords that may have been used to protect the text from keyless extraction.  Run the script using the 'python3 StegoBrute.py' command and follow the prompts.  It will ask you for the name of the .jpg image (and path if it is in another folder) and the name of the password list (and path if it is in another folder).  The script will work the password list top to bottom attempting to extract the data until it either succeeds or exhausts the list.  If successful, the password will be displayed and the extracted data will be written to a new file in the same folder with the StegoBrute.py script.
