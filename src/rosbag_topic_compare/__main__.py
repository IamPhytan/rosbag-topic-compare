"""Rosbags topic comparator

Compares topics consistency between rosbags in a dataset directory

Usage:
------

 $ rosbag-topic-compare [OPTIONS] -b BAGFOLDER

Compare topics in different rosbags inside BAGFOLDER
    and summarize the comparison in a JSON or YAML file:

 $ rosbag-topic-compare -b path/to/BAGFOLDER -o rostopics.json
 $ rosbag-topic-compare -b path/to/BAGFOLDER -o rostopics.yaml

Compare topics in rosbags inside BAGFOLDER, summarize in a JSON file
    and plot a figure to show missing topics in each rosbag:

 $ rosbag-topic-compare -b path/to/BAGFOLDER -p

Compare topics in rosbags inside BAGFOLDER,
    show a topic consistency summary
    and save it in `dataset_consistency.png`:

 $ rosbag-topic-compare -b path/to/BAGFOLDER -p --pp

Available options are:

 -h, --help            show this help message and exit
 -o E, --output E       Metadata summary output path
 -p, --plot            Plotting mode : display a summary plot
 -o SP, --summary-plot SP
                       Path for saving the summary plot

 -h, --help                                Show this help
 -b BAGFOLDER, --bagfolder BAGFOLDER       Path to folder with rosbags
 -p, --plot                                Optional. Show missing topics in a matplotlib figure

Version:
--------

- rosbag-topic-compare v0.0.1
"""
from __future__ import annotations

import argparse
from pathlib import Path

from . import utils as u
from .topic_comparator import BagTopicComparator


def parse_arguments():
    """Parse bagfile name"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "bagfolder",
        type=u.path_type(),
        help="""Dataset directory path""",
    )
    parser.add_argument(
        "-m",
        "--metadata",
        type=u.path_type(exists=False),
        help="Metadata summary output path",
    )
    parser.add_argument(
        "-p",
        "--plot",
        help="Plotting mode : display a summary plot",
        action="store_true",
    )
    parser.add_argument(
        "--fig",
        "--summary-figure-path",
        help="Path for saving a topic consistency figure",
    )
    return parser.parse_args()


def main():
    """Main function"""
    args = parse_arguments()
    data_path = Path(args.bagfolder)
    is_plot = args.plot
    rosbag_comp = BagTopicComparator(data_path)
    rosbag_comp.extract_data()
    if args.export:
        rosbag_comp.export_metadata(args.export)
    if is_plot:
        rosbag_comp.plot(args.plot_path)


if __name__ == "__main__":
    main()