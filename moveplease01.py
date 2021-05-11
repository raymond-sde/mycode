#!/usr/bin/env python3
import shutil
import os

# start script from desired directory
os.chdir('/home/student/mycode/')

# move file to dest directory
shutil.move('raynor.obj', 'ceph_storage/')

# prompt user for new name for kerrigan.obj
xname = input('What is the new name for kerrigan.obj? ')

# rename kerrigan with prompted set name
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

