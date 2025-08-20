# employee_performance.py
# Email for verification: 23f3003411@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset (100 rows ideally, but using a few for demo)
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,R&D,North America,76.99,6,3.8
EMP002,Finance,Africa,71.8,10,3.8
EMP003,Operations,North America,93.75,4,3.6
EMP004,IT,Latin America,77.25,14,4.4
EMP005,Operations,Europe,80.03,15,4.2
EMP006,IT,Europe,68.40,7,3.9
EMP007,Finance,Asia,82.10,11,4.0
EMP008,HR,North America,74.30,8,3.7
EMP009,IT,Asia,91.20,9,4.3
EMP010,R&D,Europe,88.75,12,4.5
"""

# Load into DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data))

# Frequency count of IT department
it_count = df[df['department'] == 'IT'].shape[0]
print("Frequency count of IT department:", it_count)

# Histogram of department distribution
plt.figure(figsize=(8,6))
df['department'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Department Distribution", fontsize=14)
plt.xlabel("Department")
plt.ylabel("Frequency")
plt.tight_layout()

# Save plot
plt.savefig("histogram.png")

# Save to HTML with embedded image
with open("employee_analysis.html", "w") as f:
    f.write("<html><body>")
    f.write("<h2>Employee Department Analysis</h2>")
    f.write(f"<p>Email: 23f3003411@ds.study.iitm.ac.in</p>")
    f.write(f"<p>Frequency count of IT department: {it_count}</p>")
    f.write('<img src="histogram.png" width="600">')
    f.write("</body></html>")