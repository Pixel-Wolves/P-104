import cv2
img=cv2.imread("solar-system.jpg")
text1="Sol"
text2="Mercurio"
text3="Venus"
text4="Tierra"
textx="Luna"
text5="Marte"
text6="Jupiter"
text7="Saturno"
text8="Urano"
text9="Neptuno"
cv2.putText(img,text1,(100,60),fontFace=cv2.FONT_ITALIC,fontScale=1,color=(0,0,255))
cv2.putText(img,text2,(125,250),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text3,(205,170),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text4,(260,250),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,textx,(300,150),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text5,(400,260),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text6,(500,100),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text7,(700,260),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text8,(930,260),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text9,(1080,160),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.imshow("Solar System",img)
cv2.waitKey(0)