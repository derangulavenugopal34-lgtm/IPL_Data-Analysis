import pandas as pd

data = {
    "Team": ["CSK", "MI", "RCB", "CSK", "MI"],
    "Runs": [180, 150, 200, 170, 160]
}

df = pd.DataFrame(data)

print("Average Runs:", df["Runs"].mean())
print("Max Runs:", df["Runs"].max())

import matplotlib.pyplot as plt

df.plot(x="Team",y="Runs",kind="bar")
plt.title("Team Runs Analysis")
plt.xlabel("Team")
plt.ylabel("Runs")
plt.show()
