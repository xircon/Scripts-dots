from path import Path
d = Path("/home/steve/scripts/i3/backup") 
num_files = len(d.files())

print(num_files)