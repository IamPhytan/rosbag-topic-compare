"""Rosbags topic comparator

Compares topics consistency between rosbags in a dataset directory

Usage:
------

 $ rosbag-topic-compare [OPTIONS] BAGFOLDER

Compare topics in different rosbags inside BAGFOLDER
    and summarize the comparison in a JSON or YAML file:

 $ rosbag-topic-compare path/to/BAGFOLDER -o rostopics.json
 $ rosbag-topic-compare path/to/BAGFOLDER -o rostopics.yaml

Compare topics in rosbags inside BAGFOLDER, summarize in a JSON file
    and plot a figure to show missing topics in each rosbag:

 $ rosbag-topic-compare path/to/BAGFOLDER -p

Compare topics in rosbags inside BAGFOLDER,
    show a topic consistency summary
    and save it in `dataset_consistency.png`:

 $ rosbag-topic-compare path/to/BAGFOLDER -p --fig dataset_consistency.png

Available options are:

options:
  -h, --help            show this help message and exit
  -m METADATA, --metadata METADATA
                        Metadata summary output path
  -p, --plot            Plotting mode : display a summary plot
  --fig FIG, --summary-figure-path FIG
                        Path for saving a topic consistency figure

Version:
--------

- rosbag-topic-compare v0.0.3
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
    if args.metadata:
        rosbag_comp.export_metadata(args.metadata)
    if is_plot:
        if args.fig:
            rosbag_comp.plot(args.fig)
        else:
            rosbag_comp.plot()
    if not args.metadata and not is_plot:
        # Default behavior, without any arguments
        topics_desc = rosbag_comp.to_yaml_str()
        print(topics_desc)


if __name__ == "__main__":
    main()
