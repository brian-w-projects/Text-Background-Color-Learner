# Color Preferences with Machine Learning
## Small Machine Learning App that selects the best color to display text given different colored backgrounds

[![YOUTUBE](https://img.youtube.com/vi/D3QkF0KDC2A/0.jpg)](https://www.youtube.com/watch?v=D3QkF0KDC2A)

This is a small example machine learning project the purpose of which is to determine which color font should be
selected given a variety of different background colors. Two possible font colors are selected at random along with
100 different background colors. A tkinter window asks the user to selected the preferred font color for each of the
100 background colors. Afterwards, a machine learning algorithm is run to select the better font color for ten newly
selected random background colors. The selections are displayed on the tkinter window.

Application:

This project serves as a skeleton for an expandable machine learning project. There are a number of improvements that
can be made to further expand the capabilities of the project.

<pre>
Usage: color_learner.py [-h] [-c [COLORS [COLORS ...]]] [-i ITERATIONS]

Machine Learning Algorithm to Select Appropriate Font Colors

optional arguments:
  -h, --help            show this help message and exit
  -c [COLORS [COLORS ...]]
                        2 len list of font colors to compare. EX: 05ab1b 55abc8
                        Default is random selection.
  -i ITERATIONS         Number of training iterations. Minimum 50. Default is
                        100.
</pre>
