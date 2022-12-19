import matplotlib.pyplot as plt
import numpy as np
from os import path


def plot_reflectances(type, color_checker_case, save_name=None):
    fig, ax = plt.subplots(figsize=(22, 12))

    ax.set_xlabel('Wavelength (in nm)', fontsize=16)
    ax.set_ylabel('Reflectance', fontsize=16)
    ax.tick_params(labelsize=16)
    ax.grid()

    if type == 'CC':
        plot_CC(color_checker_case, ax)

    elif type == 'CC_GEOM':
        plot_CC_GEOM(color_checker_case, ax)

    else:
        plot_CC(color_checker_case, ax, joint=True)
        plot_CC_GEOM(color_checker_case, ax, joint=True)

        ax.set_title(f'Reflectances of the case {color_checker_case:02} in function of the wavelength for CC and CC_GEOM.', fontsize=18)
        ax.legend(bbox_to_anchor=(1, 1), loc='upper left', fontsize=16)

    if save_name is not None:
        fig.savefig(path.join('plots', type, save_name))


def plot_CC(color_checker_case, ax, joint=False):
    data = np.load(path.join('CC', 'CC.npz'))
    wavelengths = data['wavelengths']
    reflectances = data['reflectances']
    data.close()

    if color_checker_case:
        if joint:
            ax.plot(wavelengths, reflectances[color_checker_case - 1], label='CC')

        else:
            ax.plot(wavelengths, reflectances[color_checker_case - 1])
            ax.set_title(f'Reflectance of the case {color_checker_case:02} in function of the wavelength.', fontsize=18)

    else:
        for i in range(24):
            cmap = plt.get_cmap('brg')
            colors = [cmap(i) for i in np.linspace(0, 1, 24)]

            if i % 4 == 0:
                ax.plot(wavelengths, reflectances[i], color=colors[i], label='Case %02d' % (i + 1))

            elif i % 4 == 1:
                ax.plot(wavelengths, reflectances[i], '-.', color=colors[i], label='Case %02d' % (i + 1))

            elif i % 4 == 2:
                ax.plot(wavelengths, reflectances[i], '--', color=colors[i], label='Case %02d' % (i + 1))

            else:
                ax.plot(wavelengths, reflectances[i], ':', color=colors[i], label='Case %02d' % (i + 1))

            ax.set_title('Reflectances of all the cases in function of the wavelength.', fontsize=18)
            ax.legend(bbox_to_anchor=(1, 1), loc='upper left', fontsize=16)


def plot_CC_GEOM(color_checker_case, ax, joint=False):
    data = np.load(path.join('CC_GEOM', 'CC_GEOM.npz'))
    wavelengths = data['wavelengths']
    angles = data['angles']
    reflectances = data['reflectances'][color_checker_case - 1]
    data.close()

    for i in range(len(angles)):
        ax.plot(wavelengths, reflectances[i, :], ['b', 'g', 'r', 'c', 'm', 'y', 'k'][i], label=f'Angle {angles[i]}°')

    if not joint:
        ax.set_title(f'Reflectances of the case {color_checker_case:02} in function of the wavelength for all the angles.', fontsize=18)
        ax.legend(bbox_to_anchor=(1, 1), loc='upper left', fontsize=16)