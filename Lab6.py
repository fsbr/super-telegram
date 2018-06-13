import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# when you get the plot running, do
# print(plt.style.available) and pick a style you think
# is interesting. your choice
plt.style.use('fivethirtyeight')


Tx = np.linspace(0,5,5)
i = 0
for T in Tx:
    num = [8, (-3*np.exp(-4*T)-5)]
    den = [12, (-7*np.exp(-4*T) -5)]

    dtf = sig.dlti(num,den)
    t,y = sig.dstep((dtf),n=1000)

    tCirc = np.linspace(0,2*np.pi,100)
    xCirc = np.cos(tCirc)
    yCirc = np.sin(tCirc)

    poleLocation = np.roots(den)
    colorIndicator = "b"
    markerIndicator = "o"

    if abs(poleLocation)>1:
        colorIndicator = "r"
        markerIndicator = "x"
    print("pole location",poleLocation)

    f,xarr = plt.subplots(2)

    xarr[0].set_title("T = %s"%T)
    xarr[0].plot(t,y[:][0])
    xarr[1].plot(1,0,c="g",marker="o")
    xarr[1].plot(xCirc,yCirc)
    xarr[1].scatter(poleLocation,0,c=colorIndicator, marker=markerIndicator)
    xarr[1].set_xlabel("pole magnitude is %s"%poleLocation)
    xarr[1].set_xlim([-2,2])

    # plt.savefig('animation%s.png'%i)
    plt.show()
    i+=1
