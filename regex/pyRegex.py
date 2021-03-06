import re

s = """MC winrate=0.484375, NN eval=0.475102, score=W+0.2

 M16 ->    6764 (W: 49.31%) (U: 47.71%) (V: 50.33%:    158) (N: 65.0%) PV: M16 L17 M17 O14 N15 O15 O18 O13
 G17 ->     219 (W: 46.91%) (U: 47.47%) (V: 46.55%:      6) (N:  3.7%) PV: G17 G18 G16 F16
 L12 ->     152 (W: 45.85%) (U: 45.36%) (V: 46.17%:      4) (N:  6.0%) PV: L12 M10
 K17 ->     137 (W: 46.39%) (U: 45.25%) (V: 47.12%:      3) (N:  3.2%) PV: K17 L17 K18
 M15 ->     133 (W: 43.80%) (U: 35.99%) (V: 48.79%:      3) (N:  9.0%) PV: M15 M16
 O14 ->     101 (W: 48.37%) (U: 48.47%) (V: 48.30%:      3) (N:  1.8%) PV: O14 L12 M16
  P6 ->      85 (W: 47.28%) (U: 38.67%) (V: 52.79%:      1) (N:  2.6%) PV: P6 O5
====================================
6764 visits, score 49.31% (from 48.82%) PV: M16 L17 M17 O14 N15 O15 O18 O13

7735 visits, 1187 nodes, 248 playouts, 123 p/s
"""

pattern = r"PV:(?:\s[A-Z][0-9]{1,2})+"

result = re.findall(pattern, s)
print(result)
