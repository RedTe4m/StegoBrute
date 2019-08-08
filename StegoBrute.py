print("..####...######..######...####....####...#####...#####...##..##..######..######.")
print(".##........##....##......##......##..##..##..##..##..##..##..##....##....##.....")
print("..####.....##....####....##.###..##..##..#####...#####...##..##....##....####...")
print(".....##....##....##......##..##..##..##..##..##..##..##..##..##....##....##.....")
print("..####.....##....######...####....####...#####...##..##...####.....##....######.")
print("..By Z3r0Sh0t...................................................................")
### setup module
import subprocess
encoding = 'utf-8'
img_in = input("Type the .jpg name (with complete path if not in same folder as script). ")
pospws = input("Type the password file name (with complete path if not in same folder as script). ")

### passfind module
fp = open(pospws, 'r')
num_lines = sum(1 for line in open(pospws))
print("Okay. Testing", pospws, "which has", num_lines, "total entries.")
print("................................................................................")

line = fp.readline()
while line:
    ckpw = ("{}".format(line.strip()))
    line = fp.readline()
    cmd = ' '.join(['steghide extract -sf', img_in, '-p', ckpw, '-f' ])
    res = subprocess.run([cmd], shell=True, capture_output=True)
    bytes = b" ".join(res.stderr.split())
    str = bytes.decode(encoding)
    if (str.find('not') != -1):
        pass
    else:
        print("Found a valid password:", ckpw )
        print(str)
        print("................................................................................")
        fp.close
        quit()
print("No valid password found. It may not have anything hidden in it, or you might need to try a different password list. Exiting.")
fp.close
quit()
