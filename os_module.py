import os, glob, time, humansize
print(os.getcwd()) #get current working directory
os.chdir(os.path.expanduser('~')) #change directory
print(os.getcwd())
pathname = '/home/deen/Project/Python/Dive into Python 3/humansize.py'
print(os.path.split(pathname))
(dirname, filename) = os.path.split(pathname)
print(dirname, filename)
(name, ext) = os.path.splitext(filename)
print(name, ext)

#globbbing
print(glob.glob('*')) #The glob module takes a wildcard and returns the path of all files and directories matching the wildcard
print(glob.glob('*.zip'))

#getting metadata
metadata = os.stat('open_gapps-arm-6.0-pico-20160519.zip')
print(metadata)
time = time.localtime(metadata.st_mtime)
print(time.tm_mday,'/', time.tm_mon, '/', time.tm_year)
print(metadata)
print(metadata.st_size)
print(humansize.approximate_size(metadata.st_size, a_kilobyte_is_1024_bytes = False))

#real path
print(os.path.realpath('open_gapps-arm-6.0-pico-20160519.zip'))

#putting globbed paths in a list

a_list = [os.path.realpath(f) for f in glob.glob('*.zip')]
print(a_list)

print([os.path.realpath(f) for f in glob.glob('*.zip') if os.stat(f).st_size > 6000])
