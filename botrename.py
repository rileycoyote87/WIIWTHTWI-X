import re;
import fileinput;
from random import randint;
import sys;

reg = re.compile("^(Hard|Easy|Elite|Expert|VeryHard|Tough|Normal|Fair|Easy)(\+| ).*");

files = [];
files.append('botprofile.db');


for line in fileinput.input(files,inplace=True):
    if(reg.match(line)):
        lineparts = line.split(' ');
        num = randint(1,8);
        line = lineparts[0] + ' ' + str(num) + lineparts[1];
        sys.stdout.write(line);
    else:
        sys.stdout.write(line);
