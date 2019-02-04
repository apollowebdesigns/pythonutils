import os

def info_of_hard_drive(hard_drive_name):
    os.system('diskutil info /Volumes/' + hard_drive_name)


info_of_hard_drive('My\ Passport')


def nfts_convert():
    # Key in your uuid for your hard drive from previous command
    os.system('UUID=5B5C4986-DB46-4AB7-9244-FA3D1B2D1DCE none ntfs rw,auto,nobrowse')
