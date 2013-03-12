#!/usr/bin/env python
from util.helper import *
import glob
import sys
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

args = parser.parse_args()

BOTTLENECK_BYTE_RATE = 1000 * 1000 * 1.5 / 8

def plot_throughput(ax, name, label, color, marker):
  xdata = []
  ydata = []
  for s in os.listdir(args.dir):
    interval = re.findall('interval-([0-9.]+)', s)
    if len(interval) == 0: continue

    with open("%s/%s/ss-%s" % (args.dir, s, name)) as hGS:
      data = map(lambda x: x.split(','), hGS.readlines())

    if len(data) < 2:
      print "%s" % (interval[0], )
      continue

    throughput = (float(data[-1][1]) - float(data[0][1])) / (float(data[-1][0]) - float(data[0][0]))
    xdata += [float(interval[0])]
    ydata += [throughput / BOTTLENECK_BYTE_RATE]

  data = sorted(zip(xdata, ydata), lambda x, y: 1 if x[0] - y[0] > 0 else -1)
  ax.plot(*zip(*data), label=label, color=color, marker=marker)

def main():
  fig = plt.figure()
  ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])

  plot_throughput(ax, 'hGR', 'TCP', color='red', marker='s')
  #plot_throughput('hBR', 'Attacker UDP', color='blue', marker='o')

  ax.legend(loc=2, bbox_to_anchor=(1.05, 1))
  ax.set_ylabel("Normalized Throughput")
  ax.set_xlabel("Attack Interval")
  plt.savefig("%s" % (args.out, ))

if __name__ == '__main__':
  main()
