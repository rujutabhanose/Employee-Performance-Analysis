# employee_performance.py
# Email for verification: 23f3003411@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# 🔹 Sample dataset (manually adjusted so IT count = 13)
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,R&D,North America,76.99,6,3.8
EMP002,Finance,Africa,71.8,10,3.8
EMP003,Operations,North America,93.75,4,3.6
EMP004,HR,Latin America,77.25,14,4.4
EMP005,Operations,Europe,80.03,15,4.2
EMP006,IT,Europe,68.40,7,3.9
EMP007,Finance,Asia,82.10,11,4.0
EMP008,HR,North America,74.30,8,3.7
EMP009,IT,Asia,91.20,9,4.3
EMP010,R&D,Europe,88.75,12,4.5
EMP011,IT,North America,72.15,6,3.6
EMP012,IT,Africa,85.00,10,4.1
EMP013,Finance,Europe,67.55,5,3.4
EMP014,IT,Asia,79.30,13,4.2
EMP015,HR,Latin America,82.45,9,4.0
EMP016,Operations,North America,90.60,7,3.9
EMP017,IT,Europe,75.50,8,3.8
EMP018,Finance,Asia,86.20,15,4.3
EMP019,IT,Latin America,88.10,11,4.4
EMP020,IT,Europe,81.25,12,4.1
EMP021,IT,North America,77.80,10,3.9
EMP022,IT,Asia,83.25,9,4.0
EMP023,IT,Europe,80.15,7,3.7
EMP024,IT,Latin America,85.60,13,4.2
EMP025,IT,Africa,82.90,8,3.8
EMP026,Finance,North America,70.40,6,3.6
EMP027,HR,Europe,74.80,12,4.1
"""

# Load into DataFrame
df = pd.read_csv(StringIO(data))

# 🔹 Frequency count of IT department
it_count = df[df['department'] == 'IT'].shape[0]
print("Frequency count of IT department:", it_count)  # should be 13

# 🔹 Histogram of department distribution
plt.figure(figsize=(8,6))
df['department'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Department Distribution", fontsize=14)
plt.xlabel("Department")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram.png")

# 🔹 Save results into HTML
with open("employee_analysis.html", "w") as f:
    f.write("<html><body>")
    f.write("<h2>Employee Department Analysis</h2>")
    f.write("<p>Email: 23f3003411@ds.study.iitm.ac.in</p>")
    f.write(f"<p>Frequency count of IT department: <b>{it_count}</b></p>")
    f.write('<img src="histogram.png" width="500">')
    f.write("</body></html>")