import numpy as np
import cv2


img = cv2.imread('1.jpg')
chessboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
playsteps =0
winner = 0
cv2.imshow('image',img)

def mouse_dclick(event,x,y, flags, param):
    global playsteps, winner
    if event == cv2.EVENT_LBUTTONDBLCLK:
        i, j = y // 100, x // 100
        if chessboard[i][j] == 0:
            player = playsteps % 2 + 1
            print("mc", player)
            chessboard[i][j] = player
            winner = getWinner(i, j, player)
            playsteps += 1

def getWinner(row, col, player):
    row_valid, col_valid = True, True
    dia_validl, dia_valid2 = False,False
    
    for i in range(3):
        if chessboard[row][i] != player:
            row_valid = False
        if chessboard[i][col] != player:
            col_valid = False

    if row == col:
        dia_validl = True
        for i in range(3):
            if chessboard[i][i] != player:
                dia_validl = False
                
    if row + col == 2:
        dia_valid2 = True
        for i in range(3):
            if chessboard[i][2 - i] != player:
                dia_valid2 = False
                
    if row_valid or col_valid or dia_validl or dia_valid2:
        return player
    else:
        return 0

cv2.setMouseCallback('image', mouse_dclick)
while True:
    for i in range(3):
        for j in range(3):
            cv2.rectangle(img,(100*j,100*i),(100*(j+1),100*(i+1)),(0, 255,255),2)
            if chessboard[i][j] != 0:
                isSolid = -1 if chessboard[i][j] == 2 else 2
                cv2.circle(img,(50+100*j, 50+100*i), 50, (0, 255, 0), isSolid)
    cv2.imshow('image', img)
    
    if winner == 1 or winner == 2:
        break
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Winnner is '+str(winner), (50, 180), font, 2, (0, 255, 255),4)
cv2.imshow("image", img)
cv2.waitKey(5000)
cv2.destroyAllWindows() 
