#!/usr/bin python3
# _*_ coding: utf-8 _*_
import os
import sys
import im2gif
import cmath as cm
import numpy as np
from io import BytesIO
from PIL import Image as im
from matplotlib import pyplot as plt

# main function
def main():
    #=======================================================================
    # part 1: datamation
    #=======================================================================
    # set barrier width a
    a = 0.16

    # set ratio of E/U0
    ratio = float(input('please input ratio of E/U0: '))
    # example:
    # ratio = 0.6
    # ratio = 1
    # ratio = 1.4
    # to avoid ratio being smaller than 0.01 or equal to 1
    ratio = 0.01 if ratio < 0.01 else ratio if ratio != 1 else ratio + 1e-10

    # set barrier constant k0
    # k0 = cm.sqrt(2 * m * U0 / pow(h_, 2))
    # it will affect the wavelength of probability wave
    k0 = 4

    # define wave Energy E
    # E = ratio * U0

    # set scale value.()
    # it will contral the wave length on display
    # while scale = 0.5e-8, there are no auto scale
    # if you don't want auto scale, just del denominator: cm.sqrt(ratio)
    # scale = 1
    scale = 1 / cm.sqrt(ratio)

    # define wave vactor k
    # k1 = scale * cm.sqrt(2 * m * E / pow(h_, 2))
    # k2 = scale * cm.sqrt(2 * m * (E - U0) / pow(h_, 2))
    k1 = scale * k0 * cm.sqrt(ratio)        # wave vector of part 1 and 3
    k2 = scale * k0 * cm.sqrt(ratio - 1)    # wave vector of part 2

    # define intensity ratio of wave
    # A and A_ belong to wave of part 1
    # B and B_ belong to wave of part 2
    # C and C_ belong to wave of part 3
    # De is just a common denominator value
    # we define A = 1 and others will be directly proportional to A
    A = 1.2
    De = pow(k1 - k2, 2) * np.exp(1j * k2) - pow(k1 + k2, 2) * np.exp(-1j * k2)
    A_ = 2j * (pow(k1, 2) - pow(k2, 2)) * np.sin(k2) * A / De
    C = -4 * k1 * k2 * np.exp(-1j * k1) * A / De
    B = (A * k1 + A * k2 - A_ * k1 + A_ * k2) / (2 * k2)
    B_ = (A * k2 - A * k1 + A_ * k1 + A_ * k2)/ (2 * k2)

    # define three part
    x1 = np.linspace(-1, 0, 10e3)       # x limit of part 1
    x2 = np.linspace(0, a, 10e3)        # x limit of part 2
    x3 = np.linspace(a, a + 1, 10e3)    # x limit of part 3

    # define wave function
    y1_r = A * np.exp(1j * k1 * x1/a)     # right wave function of part 1
    y1_l = A_ * np.exp(-1j * k1 * x1/a)   # left wave function of part 1
    y2_r = B * np.exp(1j * k2 * x2/a)     # right wave function of part 2
    y2_l = B_ * np.exp(-1j * k2 * x2/a)   # left wave function of part 2
    y3_r = C * np.exp(1j * k1 * x3/a)     # right wave function of part 3

    y1 = y1_r + y1_l                    # wave function of part 1
    y2 = y2_r + y2_l                    # wave function of part 2
    y3 = y3_r                           # wave function of part 3

    w1 = abs(y1)**2
    w2 = abs(y2)**2
    w3 = abs(y3)**2

    # debug out
    # print('k1', k1, '\nk2', k2, '\nA', A, '\nA_', A_, '\nB', B, '\nB_', B_, '\nC', C, '\nDe', De)

    #=======================================================================
    # part 2: visualization
    #=======================================================================
    # set x, y half axis limit
    x_limit = 1
    y_limit = 4

    # create a new figure
    plt.figure(figsize=(10,45/8))

    # set axis scope
    plt.axis([-x_limit, a + x_limit, -y_limit, y_limit])

    # hide the axis
    plt.axis('off')

    # set hold on
    plt.hold(True)

    # set alpha of lines
    alpha = 1
    color_com = (0,0.5,0, alpha)
    color_inc = (0,0,1,alpha)
    color_ref = (1,0,0,alpha)
    color_pro = (0,0,0.5,0.6)
    color_fil = (0,0,0.5,0.3)
    # draw wave in part 1 and get three plot handle for data updating later
    h10, = plt.plot(x1, np.real(y1), color=color_com, linestyle='-', label='composite wave', linewidth=2)
    h11, = plt.plot(x1, np.real(y1_r), color=color_inc, linestyle='--', label='incident wave', linewidth=2)
    h12, = plt.plot(x1, np.real(y1_l), color=color_ref, linestyle='--', label='reflected wave', linewidth=2)
    # draw imag wave of part 1
    plt.plot(x1, np.imag(y1), color=color_com, linestyle=':', label='imag part', linewidth=2)
    # draw probability density line of part 1
    plt.plot(x1, w1 - y_limit + 1, color=color_pro, label='probability density')
    # fill probability line of part 1
    plt.fill_between(x1, np.zeros_like(x1)-y_limit+1, w1-y_limit+1, color=color_fil)
    # draw legend
    plt.legend(fontsize=14, frameon=True, fancybox=True, framealpha=0.3)

    # draw wave in part 2 and get three plot handle for data updating later
    h20, = plt.plot(x2, np.real(y2), color=color_com, linestyle='-', linewidth=2)
    h21, = plt.plot(x2, np.real(y2_r), color=color_inc, linestyle='--', linewidth=2)
    h22, = plt.plot(x2, np.real(y2_l), color=color_ref, linestyle='--', linewidth=2)
    # draw imag wave of part 1
    plt.plot(x2, np.imag(y2), color=color_com, linestyle=':', linewidth=2)
    # draw probability density line of part 2
    plt.plot(x2, w2 - y_limit + 1, color=color_pro)
    # fill probability line of part 2
    plt.fill_between(x2, np.zeros_like(x2)-y_limit+1, w2-y_limit+1, color=color_fil)
    
    # draw wave in part 3
    h30, = plt.plot(x3, np.real(y3), color=color_com, linestyle='-', linewidth=2)
    # draw imag wave of part 1
    plt.plot(x3, np.imag(y3), color=color_com, linestyle=':', linewidth=2)
    # draw probability density line of part 3
    plt.plot(x3, w3 - y_limit + 1, color=color_pro)
    # fill probability line of part 3
    plt.fill_between(x3, np.zeros_like(x3)-y_limit+1, w3-y_limit+1, color=color_fil)

    # draw barrier line
    plt.plot([-1,0,0,a,a,a+1], [-3,-3,3,3,-3,-3], color=(0,0,0,alpha), linestyle='-', linewidth=2)

    # draw reference center line
    plt.plot([-1, a + 1], [0, 0], color=(0.5,0.5,0.5,alpha), linestyle='-.')

    # set hold off
    plt.hold(False)

    # draw text information
    ## define font dict creater function
    def font(family='serif', color='black', weight='normal', size='16'):
        return {'family': family, 'color': color, 'weight': weight, 'size': size}
    # draw title
    plt.title('Barrier Penetration And Tunneling', fontdict=font(size=20))
    # draw barrier height value U0
    plt.text(a, 3, '$U_0$', fontdict=font(size=20))
    # draw value of k0
    plt.text(-.9, 3, '$\itK_0=%d$' % k0, fontdict=font(size=20))
    # draw value of E/U0
    plt.text(-.6, 3, '$\itE/\itU_0=\it%.2f$' % ratio, fontdict=font(size=20))
    # draw scale value text
    plt.text(-.7, -3.3, '$\itscale=%.2f$' % np.real(scale), fontdict=font())
    # draw barrier left limit
    plt.text(-.02, -3.3, '$0$', fontdict=font())
    # draw barrier right limit
    plt.text(a-.02, -3.3, '$a$', fontdict=font())
    # draw x axis mark 'x'
    plt.text(a+.95, -2.95, '$x$', fontdict=font())
    # draw water mark of author
    plt.text(a+.7, -3.4, '$author: ph$', fontdict=font(color='gray'))
    # show plot
    # plt.show()
    if len(sys.argv) > 1:
        if  sys.argv[1] == '-d':
            # set gif save root dir
            gif_root = './gif'
            # check gif root dir
            if not os.path.isdir(gif_root):
                os.makedirs(gif_root)
            # set frame number N
            FN = 40
            # pre storage allocation
            images = []
            for i in range(FN):
                # add time factor
                Et = np.exp(-2j * np.pi * i / FN)

                # update the plot data
                h10.set_ydata(np.real(y1 * Et))
                h11.set_ydata(np.real(y1_r * Et))
                h12.set_ydata(np.real(y1_l * Et))
                h20.set_ydata(np.real(y2 * Et))
                h21.set_ydata(np.real(y2_r * Et))
                h22.set_ydata(np.real(y2_l * Et))
                h30.set_ydata(np.real(y3 * Et))

                # create bytes buffer
                buf = BytesIO()

                # save plot date to buf
                plt.savefig(buf, format='png')

                # read buf as image date and append to images 
                images.append(im.open(buf))
            # set gif file save path
            gif_path = os.path.join(gif_root, 'slgc_%.2f.gif' % ratio)
            # create GIF dynamic plot from images
            im2gif.writeGif(filename=gif_path, images=images, duration=2 / FN)

            # print status message
            print('gif file created at path: %s.' % os.path.abspath(gif_path))
        elif sys.argv[1]=='-s':
            png_root = './png'
            if not os.path.isdir(png_root):
                os.makedirs(png_root)
            png_path = os.path.join(png_root, 'slgc_%.2f.png' % ratio)
            plt.savefig(png_path, format='png')
            print('png file created at path: %s.' % os.path.abspath(png_path))
    else:
        plt.show()
if __name__ == '__main__':
    main()