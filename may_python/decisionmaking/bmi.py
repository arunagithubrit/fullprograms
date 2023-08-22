weight_kg=120
height_cm=165
height_meter=height_cm/100
bmi=weight_kg/height_meter**2

if bmi<=18.5:
    print("under weight")

elif bmi<=24.9:
    print("normal weight")

elif bmi<=29.9:
    print("over weight")

elif bmi<=34.4:
    print("obesity level 1")

elif bmi<39.9:
    print("obesity level 2")

else:
    print("obesity class 3")
 
          