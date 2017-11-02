# Haxxorz
Repo for stuff related to hacking competition or similar

lv1: boJ9jbbUNNfktd78OOpsqOltutMc3MY1  
lv2: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9  
lv3: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK  
lv4: pIwrPrtPN36QITSp3EQaw936yaFoFgAB  
lv5: koReBOKuIDDepwhWk7jZC0RTdopnAYKh  for f in ./*; do (echo "$f:"; cat "$f"; echo; echo); done  
As suggested in https://stackoverflow.com/questions/8183191/concatenating-files-and-insert-new-line-in-between-files  
lv6: DXjZPULLxYr17uwoI01bNLQbtFemEgo7  Use du (disk usage) on all subdirs/files. Can use grep to find the exact size (1033).  
lv7: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs  Use find with -user and -group  
lv8: cvX2JJa4CFALtqS87jk27qwqGhBM9plV  Use grep. Can use -B and -A to specify the number of displayed lines before and after the text.  
lv9: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR  sort data.txt | uniq -u (seems like seq doesn't work well here, so using pipe).  
Alternatively: sort data.txt > temp.txt; uniq -u temp.txt; rm temp.txt  
lv10:truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk  grep -ao ==[^$] data.txt (a to interpret the file as text, o to only show matching expression)  
Need to search the result manually. Did cut all preceding text on the line. Assumes that following text is printed until end of line ($).  
lv11:IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR  base64 -d data.txt (decodes base64 data).  
lv12:5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu  tr [A-Za-z] [N-ZA-Mn-za-m] < data.txt (seems to translate char-by-char from first array to second).  
lv13:8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL  use xxd to decode, then use file to find how it's compressed.  
Use gunzip, bunzip2 and tar -xvf recursively depending on what kind of file it is (might need to rename files).
I did this manually, but it might be better to write some kind of loop containing conditional tests.
Should be doable when we know that the files are either gzip, bzip2 or tar.  
lv14:4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e  ssh -i sshkey.private bandit14@... (to get in, then navigate to the password).
lv15:

These are for the pre-assignment task. The assignments themselves will not be posted here while the competition is still running.  
UPDATE 1: Apparently, the assignments are planned to be reused, so solutions will not be posted here.  
Instead, there will be more focus on pre-assignment and possibly other wargames.  
UPDATE 2: Tip from an online source: Close the previous connection before making a new one. (less traffic I guess).  
