"""Rosbags topic comparator

Usage:
------

 $ rosbag-topic-compare [OPTIONS] -b BAGFOLDER

Compare the topics in rosbags inside BAGFOLDER and summarize in a JSON or YAML file:

 $ rosbag-topic compare -b path/to/BAGFOLDER

Compare the topics in rosbags inside BAGFOLDER, summarize in a JSON file
    and plot a figure to show missing topics in each rosbag:

 $ rosbag-topic-compare -b path/to/BAGFOLDER -p

Available options are:

 -h, --help                                Show this help
 -b BAGFOLDER, --bagfolder BAGFOLDER       Path to folder with rosbags
 -p, --plot                                Optional. Show missing topics in a matplotlib window

Version:
--------

- rosbag-topic-compare v0.0.1
"""
from __future__ import annotations

import argparse
from pathlib import Path

import utils as u

from .topic_comparator import BagTopicComparator


def parse_arguments():
    """Parse bagfile name"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "bagfolder",
        type=u.path_type(),
        help="""Path to the rosbag dataset""",
    )
    parser.add_argument(
        "-p",
        "--plot",
        help="Flag for plotting and showing the result",
        action="store_true",
    )
    return parser.parse_args()


def main():
    """Main function"""
    args = parse_arguments()
    data_path = Path(args.bagfolder)
    is_plot = args.plot
    rosbag_comp = BagTopicComparator(data_path)
    rosbag_comp.extract_data()
    rosbag_comp.export_metadata()
    if is_plot:
        rosbag_comp.plot()


if __name__ == "__main__":
    main()
