# Trial and Error Line Fitting

A Python implementation of trial and error algorithm to find the optimal line through random points.

## Description
- Generates 1000 random points (x,y) normalized between 0-1
- Performs 100 random trials with different line parameters (a,b)
- Uses equation y = ax + b to calculate errors
- Finds the line with minimal average error
- Visualizes results with matplotlib

## Usage
```python
python trial_error_line_fitting.py
