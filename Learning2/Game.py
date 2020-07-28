import pygame,sys
import Constants

def read(mapfile):
    with open(mapfile,"r")as f:
        world_map=f.readlines()
def main():
    read_map(Constants.mapfile)
if __name__=="main":
    main()