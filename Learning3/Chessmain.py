#Valid moves and game state
import pygame as p
import ChessEngine
Width=Height=512
Dimension=8 #8by8 board
SQ_SIZE=Height/Dimension
Max_Fps=15
IMAGES={}

def load_Images():
    pieces = ["wp","wR","wN","wB","wK","wQ","bp","bR",'bN',"bK","bQ"]
    for piece in pieces:
        IMAGES[piece]=p.transform.scale(p.image.load("images/"+piece+".png"),(SQ_SIZE,SQ_SIZE))

def main():
    p.init()
    screen=p.display.set_mode((Width,Height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs=ChessEngine.GameState()
    print(gs.board)
main()