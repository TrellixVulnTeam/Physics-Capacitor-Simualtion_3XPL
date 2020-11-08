# this file is opening saved classes
import pickle
import numpy as np
import matplotlib.pyplot as plt
from Plate_Capacitor import Plate_Capacitor

if __name__ == "__main__":
    # setting a path
    path = 'D:\\Python\\Programme\\Physics-Capacitor-Simualtion\\resources\\exports\\29_10_2020__12_15_19\\class.pickle'
    # path open an old pickle file
    # cap = pickle.load(open(path, "rb", -1))
    cap = Plate_Capacitor(n_neg=15, n_pos=15, p1=[0.01, 0.01], p2=[0.02, 0.02], plane_z_pos=[0.001],
                          plane_z_neg=[0.002],
                          random=False)
    # cap.plotting_plates()
    x = np.linspace(0.001, cap.plate_neg.x_length-0.001, 5) + cap.p1[0]
    # getting the field lines
    print(cap.plot_field_lines(x_plane=x, num_field_lines=8))
