#!/usr/bin/env python

from helper import *
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.mlab as mlab

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('--dir',
                      dest="dir",
                      help="Directory from which outputs of the sweep are read.",
                      required=True)
  parser.add_argument('--out',
                      dest="out",
                      help="Generated output figure.",
                      required=True)
  args = parser.parse_args()
  return args

def graph(args):
  # Get data points
  f = open("%s/http-data.txt" % (args.dir, ))
  data = map(lambda x: x.split(','), f.readlines())
  f.close()
  xdata = map(lambda x: float(x[0]), data)
  ydata = map(lambda x: float(x[1]), data)

  # Create a figure with size 6 x 6 inches.
  fig = Figure(figsize=(6, 6))

  # Create a canvas and add the figure to it.
  canvas = FigureCanvas(fig)

  # Added various information
  ax = fig.add_subplot(111)
  ax.set_title("Impact on HTTP Flows", fontsize=14)
  ax.set_xlabel("File Size (packets)", fontsize=12)
  ax.set_ylabel("Response Time (Normalized)", fontsize=12)
  ax.set_xscale('log')
  ax.set_yscale('log')

  # Display Grid.
  ax.grid(True, linestyle='-', color='0.75')

  # Generate and save the Scatter Plot.
  ax.scatter(xdata, ydata, s=20, color='tomato');
  canvas.print_figure(args.out, dpi=500)

def main():
  args = parse_args()
  graph(args)

if __name__ == '__main__':
  main()
