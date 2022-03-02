import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.transforms as trans
import random

#state of stress inputs

sigma_xx=int(input('Sigma xx (MPa): '))
tau_xy=int(input('Tau xy (MPa): '))
sigma_yy=int(input('Sigma yy (MPa): '))

"""
sigma_xx=random.uniform(-200,200)
tau_xy=random.uniform(-200,200)
sigma_yy=random.uniform(-200,200)
"""

####################    calculations    ######################

#calculate A,B
A=(sigma_xx,-tau_xy)
B=(sigma_yy,tau_xy)

#calculate AB line and line length
AB_slope=(B[1]-A[1])/(B[0]-A[0])
AB_linspace=np.linspace(A[0],B[0])
y_intercept=A[1]-AB_slope*A[0]
AB_line=(AB_slope*AB_linspace)+y_intercept
AB_length=math.sqrt(((B[1]-A[1])**2)+((B[0]-A[0])**2))

#calculate center
centerx=(B[0]+A[0])/2
centery=(B[1]+A[1])/2
center=(centerx,centery)

#calculate principal stresses and points
S1x=centerx+(0.5*AB_length)
S2x=centerx-(0.5*AB_length)
S1=[S1x,0]
S2=[S2x,0]

#calculate points of maximum shear stress
T1=[centerx,centery+(0.5*AB_length)]
T2=[centerx,centery-(0.5*AB_length)]

#calculate principal angle (obtained from kite.com "how to get the angle between two vectors")
vector_1 = [A[0]-centerx, A[1]-centery]
vector_2 = [S1[0]-centerx, 0]

unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
dot_product = np.dot(unit_vector_1, unit_vector_2)
mohr_theta = math.degrees(np.arccos(dot_product))

#stress element angle
if tau_xy < 0:
    angle=-mohr_theta/2
elif tau_xy > 0:
    angle=mohr_theta/2






########################    subplot 1 Plotting    #####################

#plot initialization
fig,(ax1,ax2)=plt.subplots(ncols=2)
fig.set_size_inches(12,6)
ax1.grid(True)

#create circle
circle=plt.Circle(center,(0.5*AB_length),facecolor='yellow',
edgecolor='black',zorder=5)

#mark axes
ax1.axhline(color='k')
ax1.axvline(color='k')

#plot A,B
ax1.plot(A[0],A[1],'bo',B[0],B[1],'bo',zorder=10)
ax1.text((A[0]+10),A[1],'A',
bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=12)
ax1.text((B[0]+10),B[1],'B',
bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=12)

#plot sigma_1,sigma_2
ax1.plot(S1[0],S1[1],'bo',S2[0],S2[1],'bo',zorder=10)

#annotate sigma_1,sigma_2
ax1.annotate('\u03C3'+'1',(S1[0],S1[1]),xytext=(30,-8),xycoords=ax1.transData,
textcoords='offset pixels',bbox=dict(boxstyle='round,pad=0.3',color='w',ec='k'),
zorder=12)
ax1.annotate('\u03C3'+'2',(S2[0],S2[1]),xytext=(-60,-8),xycoords=ax1.transData,
textcoords='offset pixels',bbox=dict(boxstyle='round,pad=0.3',color='w',ec='k'),
zorder=12)

#plot center and AB line
ax1.plot(center[0],center[1],'bo',zorder=10)
ax1.plot(AB_linspace,AB_line,'r',zorder=9)

#plot line across principal stress points
S_linspace=np.linspace(S2,S1)
ax1.plot(S_linspace,0*S_linspace,'cornflowerblue',zorder=9)

#plot maximum/minimum shear stress
ax1.plot(T1[0],T1[1],'bo',zorder=10)
ax1.annotate('\u03C4'+'1',(T1[0],T1[1]),xytext=(-15,40),xycoords=ax1.transData,
textcoords='offset pixels',bbox=dict(boxstyle='round,pad=0.3',color='w',ec='k'),
zorder=12)
ax1.plot(T2[0],T2[1],'bo',zorder=10)
ax1.annotate('\u03C4'+'2',(T2[0],T2[1]),xytext=(-15,-60),xycoords=ax1.transData,
textcoords='offset pixels',bbox=dict(boxstyle='round,pad=0.3',color='w',ec='k'),
zorder=12)

#sigma_xx
ax1.text(0.03,0.95,'\u03C3'+'xx = '+str(round(sigma_xx,2))+' MPa',transform=ax1.transAxes,
bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=12,fontsize='small')

#sigma_yy
ax1.text(0.03,0.9,'\u03C3'+'yy = '+str(round(sigma_yy,2))+' MPa',transform=ax1.transAxes,
bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=12,fontsize='small')

#tau_xy
ax1.text(0.03,0.85,'\u03C4'+'xy = '+str(round(tau_xy,2))+' MPa',transform=ax1.transAxes,
bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=12,fontsize='small')

#critical points
ax1.text(0.7,0.75,'Critical Points:\nA: ('
+str(round(A[0],2))+', '+str(round(A[1],2))+')\nB: ('+str(round(B[0],2))+', '+
str(round(B[1],2))+')\n\u03C3'+'1: ('+str(round(S1[0],2))+', '+
str(round(S1[1],2))+')\n\u03C3'+'2: ('+str(round(S2[0],2))+', '+
str(round(S2[1],2))+')\n\u03C4'+'1: ('+str(round(T1[0],2))+', '+
str(round(T1[1],2))+')\n\u03C4'+'2: ('+str(round(T2[0],2))+', '+
str(round(T2[1],2))+')',bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),
transform=ax1.transAxes,fontsize='small')

#principal Stresses
ax1.text(0.05,0.05,'Principal Stresses:\n\u03C3'+'1'+'= '
+str(round(S1[0],2))+' MPa\n\u03C3'+'2'+'= '+str(round(S2[0],2))+' MPa',
bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),transform=ax1.transAxes,
fontsize='small')

#maximum shear stresses
ax1.text(0.6,0.05,'Max Shear Stresses:\n\u03C4'+'1'+'= '
+str(round(T1[1],2))+' MPa\n\u03C4'+'2'+'= '+str(round(T2[1],2))+' MPa',
bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),transform=ax1.transAxes,
fontsize='small')













####################    subplot 2 plotting     #####################


########## Element 1 ##########

#element 1 label
ax2.text(0.05,0.95,'Given State of Stress',bbox=dict(color='w',ec='k',
boxstyle='roundtooth'))
stress_element1=plt.Rectangle((0.65,0.65),width=0.2,height=0.2,
facecolor="yellow",edgecolor="black",zorder=10)

#plot element1 center dot
ax2.plot(0.75,0.75,'bo',scalex=False,scaley=False,zorder=15)

#element1 axes
xaxis1=np.linspace(.75,.975)
yaxis1=np.linspace(.75,.975)

#plot element1 axes
ax2.plot(xaxis1,0*xaxis1+0.75,'r',scalex=False,scaley=False,zorder=11,
linestyle='--',linewidth=2.0)
ax2.plot(0*yaxis1+0.75,yaxis1,'r',scalex=False,scaley=False,zorder=11,
linestyle='--',linewidth=2.0)

#sigma_xx
if sigma_xx>0:
    #right
    ax2.annotate("",xy=(0.975,0.75),xytext=(0.85,0.75),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    #left
    ax2.annotate("",xy=(0.525,0.75),xytext=(0.65,0.75),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    ax2.text(0.05,0.875,'\u03C3'+'xx = '+str(round(sigma_xx,2))+' MPa',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10)
elif sigma_xx<0:
    #right
    ax2.annotate("",xy=(0.85,0.75),xytext=(0.975,0.75),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    #left
    ax2.annotate("",xy=(0.65,0.75),xytext=(0.525,0.75),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    ax2.text(0.05,0.875,'\u03C3'+'xx = '+str(round(sigma_xx,2))+' MPa',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10)
else:
    pass

#sigma_yy
if sigma_yy>0:
    #top
    ax2.annotate("",xy=(0.75,0.975),xytext=(0.75,0.85),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    #bottom
    ax2.annotate("",xy=(0.75,0.525),xytext=(0.75,0.65),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    ax2.text(0.05,0.8,'\u03C3'+'yy = '+str(round(sigma_yy,2))+' MPa',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10)
elif sigma_yy<0:
    #top
    ax2.annotate("",xy=(0.75,0.85),xytext=(0.75,0.975),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    #bottom
    ax2.annotate("",xy=(0.75,0.65),xytext=(0.75,0.525),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    ax2.text(0.05,0.8,'\u03C3'+'yy = '+str(round(sigma_yy,2))+' MPa',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10)
else:
    pass

#tau_xy
if tau_xy>0:
    #top
    ax2.annotate("",xy=(0.85,0.885),xytext=(0.65,0.885),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    #right
    ax2.annotate("",xy=(0.885,0.85),xytext=(0.885,0.65),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    #bottom
    ax2.annotate("",xy=(0.65,0.615),xytext=(0.85,0.615),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    #left
    ax2.annotate("",xy=(0.615,0.65),xytext=(0.615,0.85),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    ax2.text(0.05,0.725,'\u03C4'+'xy = '+str(round(tau_xy,2))+' MPa',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10)
elif tau_xy<0:
    #top
    ax2.annotate("",xy=(0.85,0.885),xytext=(0.65,0.885),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    #right
    ax2.annotate("",xy=(0.885,0.65),xytext=(0.885,0.85),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    #bottom
    ax2.annotate("",xy=(0.65,0.615),xytext=(0.85,0.615),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    #left
    ax2.annotate("",xy=(0.615,0.85),xytext=(0.615,0.65),
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=15)
    ax2.text(0.05,0.725,'\u03C4'+'xy = '+str(round(tau_xy,2))+' MPa',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10)
else:
    pass

######## element 2 ########

#element 2 label
ax2.text(0.05,0.5,'Principal Stresses',bbox=dict(color='w',ec='k',
boxstyle='roundtooth'))

#create rectangle
stress_element2=plt.Rectangle((0.65,0.125),width=0.2,height=0.2,
transform=trans.Affine2D().rotate_deg_around(*(0.75,0.225),angle)+ax2.transAxes,
facecolor="yellow",edgecolor="black",zorder=10)

#element2 middle dot
ax2.plot(0.75,0.225,'bo',scalex=False,scaley=False,zorder=15)

#element2 axes
xaxis2=np.linspace(.75,.975)
yaxis2=np.linspace(.225,.455)

#plot element2 axes
ax2.plot(xaxis2,0*xaxis2+0.225,'r',scalex=False,scaley=False,zorder=11,
linestyle='--',linewidth=2.0)
ax2.plot(0*yaxis2+0.75,yaxis2,'r',scalex=False,scaley=False,zorder=11,
linestyle='--',linewidth=2.0)

#S1 arrow
s=trans.Affine2D().rotate_deg(angle).translate(0.75,0.225)+ax2.transAxes

#element2 new axes
axis3=np.linspace(0,.225)

#plot element2 new axes
ax2.plot(axis3,0*axis3,'cornflowerblue',scalex=False,scaley=False,transform=s,
zorder=11,linestyle='--',linewidth=2.0)
ax2.plot(0*axis3,axis3,'cornflowerblue',scalex=False,scaley=False,transform=s,
zorder=11,linestyle='--',linewidth=2.0)

if S1[0]>0:
    #right
    ax2.annotate('',xy=(0.225,0),xytext=(0.1,0),
    xycoords=s, 
    textcoords=s,
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=11)
    #left
    ax2.annotate('',xy=(-0.225,0),xytext=(-0.1,0),
    xycoords=s, 
    textcoords=s,
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=11)
    ax2.text(0.05,0.4,'\u03C3'+'1 = '+str(round(S1[0],2))+' MPa',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10)
elif S1[0]<0:
    #right
    ax2.annotate('',xy=(0,0.1),xytext=(0,0.225),
    xycoords=s, 
    textcoords=s,
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=11)
    #left
    ax2.annotate('',xy=(0,-0.1),xytext=(0,-0.225),
    xycoords=s, 
    textcoords=s,
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=11)
    ax2.text(0.05,0.4,'\u03C3'+'1 = '+str(round(S1[0],2))+' MPa',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10)
else:
    pass

#S2 arrow
t=trans.Affine2D().rotate_deg(angle).translate(0.75,0.225)+ax2.transAxes

if S2[0]>0:
    #top
    ax2.annotate('',xy=(0,0.225),xytext=(0,0.1),
    xycoords=t, 
    textcoords=t,
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=11)
    #bottom
    ax2.annotate('',xy=(0,-0.225),xytext=(0,-0.1),
    xycoords=t, 
    textcoords=t,
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=11)
    ax2.text(0.05,0.3,'\u03C3'+'2 = '+str(round(S2[0],2))+' MPa',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10)
elif S2[0]<0:
    #top
    ax2.annotate('',xy=(0,0.1),xytext=(0,0.225),
    xycoords=t, 
    textcoords=t,
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=11)
    #bottom
    ax2.annotate('',xy=(0,-0.1),xytext=(0,-0.225),
    xycoords=t, 
    textcoords=t,
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'),zorder=11)
    ax2.text(0.05,0.3,'\u03C3'+'2 = '+str(round(S2[0],2))+' MPa',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10)
else:
    pass

#theta arrow
if angle < 0:
    ax2.annotate('',xy=(0,0.225),xytext=(0.75,0.45),
        xycoords=t,
        textcoords=ax2.transAxes, 
        arrowprops=dict(arrowstyle='->',
        connectionstyle=f'angle3,angleA=0,angleB={angle}',zorder=11))
    
    #theta text
    ax2.text(0.775,0.475,r'$\theta$'+' = '+str(round(angle,2))+u'\N{DEGREE SIGN}',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10,
    size='small')

elif angle > 0:
    ax2.annotate('',xy=(0,0.225),xytext=(0.75,0.45),
        xycoords=t,
        textcoords=ax2.transAxes, 
        arrowprops=dict(arrowstyle='->',
        connectionstyle=f'angle3,angleB={angle},angleA=0',zorder=11))
    
    #theta text
    ax2.text(0.575,0.475,r'$\theta$'+' = '+str(round(angle,2))+u'\N{DEGREE SIGN}',
    bbox=dict(boxstyle="round,pad=0.3",color='w',ec='k'),zorder=10,
    size='small')




###########   plot adjustments    ##############

#center mohr's circle and define data limits
ax1.margins(0.7)

#set aspect ratios of subplots to 1, add artists
ax1.set_aspect(1)
ax2.set_aspect(1)
ax1.add_artist(circle)
ax2.add_artist(stress_element1)
ax2.add_artist(stress_element2)

#plot title, axis labels
fig.suptitle("Mohr's Circle for Stress",y=0.93)
ax1.set_xlabel('Sigma (MPa)')
ax1.set_ylabel('Tau (MPa)')
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)
plt.show()

