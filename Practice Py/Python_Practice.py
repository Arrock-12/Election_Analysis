counties=["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties")
else:
    print("Arapahoe and El Paso is not in the list of counties")
for county in counties:
    print(county)