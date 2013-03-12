#!/usr/bin/env python
from util.helper import *
import glob
import sys
import json
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('--dir',
                    dest="dir",
                    help="Directory from which outputs of the sweep are read.",
                    required=True)
parser.add_argument('--out',
                    dest="out",
                    help="Generated output figure.",
                    required=True)

lines = []
args = parser.parse_args()
with open("%s/options" % (args.dir, )) as f:
  opts = json.loads(f.read())

BOTTLENECK_RATE = float(opts['bw_net']) * 1000 * 1000 / 8.

def plot_rto(f, ax, color, name):
  global lines
  data = map(lambda x: x.split(','), f.readlines())
  xdata = map(lambda x: x[0], data)
  ydata = map(lambda x: x[4] if len(x) >= 5 else 0, data)
  lines += ax.plot(xdata, ydata, label="RTO", color="red")

def plot_rate(f, ax, color, label):
  global lines
  data = map(lambda x: x.split(','), f.readlines())
  xdata = map(lambda x: x[0], data)
  ydata = map(lambda x: x[1], data)
  ydata = map(lambda x: (float(x[0]) - float(x[2])) / (float(x[1]) - float(x[3])) / BOTTLENECK_RATE,
            zip(ydata[1:], xdata[1:], ydata[0:-1], xdata[0:-1]))
  xdata = xdata[1:]
  lines += ax.plot(xdata, ydata, label=label, color=color)

def main():
  fig = plt.figure(figsize=(40, 10))
  axes1 = fig.add_subplot(111)
  axes2 = axes1.twinx()
  axes1.set_xlabel("Elapsed Time")
  axes1.set_ylabel('RTO (seconds)')
  axes2.set_ylabel('Rate')

  with open("%s/ss-hGS" % (args.dir, )) as f:
    plot_rto(f, axes1, 'red', 'RTO')
  with open("%s/ss-hBR" % (args.dir, )) as f:
    plot_rate(f, axes2, 'blue', 'UDP')
  with open("%s/ss-hGR" % (args.dir, )) as f:
    plot_rate(f, axes2, 'green', 'TCP')

  """
  queue = open("%s/qlen_s0-eth1.txt" % (args.dir, ))
  data = map(lambda x: x.split(','), queue.readlines())
  xdata = map(lambda x: x[0], data)
  ydata = map(lambda x: float(x[1]) / 30, data)
  lines += ax.plot(xdata, ydata, label="Queue", color='orange')
  queue.close()
  """

  lns = map(lambda x: x.get_label(), lines)
  plt.legend(lines, lns)
  plt.savefig(args.out)

if __name__ == '__main__':
  main()
