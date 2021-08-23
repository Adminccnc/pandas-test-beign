import pandas as pd

x = pd.DataFrame({

    "Name":[
        "Miss A",
        "Miss B",
        "Miss C"
    ],
    "Age":[
        "19,",
        "20,",
        "21,"
    ],
    "Live":[
        "CMI",
        "CMI",
        "CMI",
    ]
})

print(x)
print("----------------------------------------")
print(x["Age"])
print(x["Age"].max)
print(x["Age"].describe)
 