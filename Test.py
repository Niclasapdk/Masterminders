
Farvemap = {"Rød": 1, "Lilla": 2, "Blå": 3, "Gul": 4, "Grøn": 5, "Orange": 6, "Hvid": 7, "Pink": 8}
Talmap = {1: "Rød", 2: "Lilla", 3: "Blå", 4: "Gul", 5: "Grøn", 6: "Orange", 7: "Hvid", 8: "Pink"}

def farvekonverter(farve1, farve2, farve3, farve4):
    return [Farvemap[farve1], Farvemap[farve2], Farvemap[farve3], Farvemap[farve4]]

def talkonverter(tal1, tal2, tal3, tal4):
    return [Talmap[tal1], Talmap[tal2], Talmap[tal3], Talmap[tal4]]


print(farvekonverter("Rød", "Lilla", "Blå", "Gul"))
print(talkonverter(1, 2, 3, 4))