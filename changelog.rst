Changelog
=========

0.0.3
-----------------------------

- Fix usage documentation in README and docstrings
- Resolve the folder name in the plot title
- Fix cmap warning while plotting
- Check for ROS2 bags too, fixes #1

0.0.2
-----------------------------

- Raise a ValueError when plotting missing topics in a consistent dataset (where all rosbags all share a common set of topics)
- Fix a CLI logic mistake where the figure wouldn't show with `-p`
- Update `__main__` docstring with arguments from 0.0.1
