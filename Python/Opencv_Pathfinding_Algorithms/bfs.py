import cv2
from collections import deque

img1 = cv2.imread("Image.png")
# img = img1
img = cv2.resize(img1, (100, 100))
img1 = img
# cv2.namedWindow('blob', cv2.WINDOW_NORMAL)
# cv2.imshow("Lenna", img)
# cv2.waitKey(0)

print(img.shape)    # 400 * 400 * 3

# BGR
red = [0, 0, 255]
blue = [255, 0, 0]
white = [255, 255, 255]
grey = [127, 127, 127]
green = [0, 255, 0]

class Node():
    def __init__(self, index, parent):
        self.x = index[0]
        self.y = index[1]
        self.parent = parent

def show_path(end, start):
    print("e ", end.x, end.y)
    print("s ", start.x, start.y)
    current = end
    while(current != start):    # can we equate 2 class in C++?
        img1[current.x][current.y] = green
        current = current.parent
    
def bfs(start):  # plan of calling it once we encounter start (red pixel)
    q = deque()
    q.append(start)
    
    # any() vs all()
    # current will always be grey, kyunki hum pehle hi children ko grey kar dete hai
    # while (img[current.x][current.y] != blue).any(): 
    cv2.namedWindow('path', cv2.WINDOW_NORMAL)
    while len(q):
        current = q.popleft()
        i, j = current.x, current.y
        # print(img[i][j])    # current is always grey !!
        cv2.imshow('path', img)
        cv2.waitKey(1)
        
        if j+1 < img.shape[1]:     # i - coloumn; j - rows
            if (img[i][j+1] != white).any() and (img[i][j+1] != grey).any():
                if (img[i][j+1] == blue).all():
                    break   # reached
                
                img[i][j+1] = grey  # taki dubara se na ho gaye check
                n = Node((i, j+1), current)
                q.append(n)
        if i+1 < img.shape[0]:
            if (img[i+1][j] != white).any() and (img[i+1][j] != grey).any():
                if (img[i+1][j] == blue).all():
                    break
                
                img[i+1][j] = grey
                n = Node((i+1, j), current)
                q.append(n)
        if j-1 > 0:
            if (img[i][j-1] != white).any() and (img[i][j-1] != grey).any():
                if (img[i][j-1] == blue).all():
                    break
                
                img[i][j-1] = grey
                n = Node((i, j-1), current)
                q.append(n)
        if i-1 > 0:
            if (img[i-1][j] != white).any() and (img[i-1][j] != grey).any():
                if (img[i-1][j] == blue).all():
                    break
                
                img[i-1][j] = grey
                n = Node((i-1, j), current)
                q.append(n)
                        
    show_path(current, start)  

esc=False
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(img[i][j]==red).all():
            start = Node((i, j), None)
            esc=True
            bfs(start)
            break
        
    if(esc):
        break

print("Done!")    
cv2.namedWindow('final', cv2.WINDOW_NORMAL)
cv2.imshow("final", img1)
cv2.waitKey(0)