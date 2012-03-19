#!/usr/bin/python

import unittest
import os
import pymatgen.band_structure.band_structure
from pymatgen.band_structure.band_structure import Bandstructure_line
from pymatgen.band_structure.plotter import BSPlotter

module_dir = os.path.dirname(os.path.abspath(__file__))

class BSPlotterTest(unittest.TestCase):

    def setUp(self):  
        import json
        with open(os.path.join(module_dir,"Cao_2605.json"), "rb") as f:
            dict=json.loads(f.read())
            self.bs=pymatgen.band_structure.band_structure.Bandstructure_line.from_dict(dict)
            self.plotter=BSPlotter(self.bs)
            
    def test_bs_plot_data(self):
        print self.plotter.bs_plot_data['ticks']['label'][5]
        self.assertEqual(len(self.plotter.bs_plot_data['distances']), 160, "wrong number of distances")
        self.assertEqual(self.plotter.bs_plot_data['ticks']['label'][5], "K", "wrong tick label")
        self.assertEqual(len(self.plotter.bs_plot_data['ticks']['label']), 19, "wrong number of tick labels")

if __name__ == '__main__':
    unittest.main()