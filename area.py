
import math
sidex=6
sidey=6
sidez=10
if sidez < sidey and sidez > 0 and sidex > 0 and sidey > 0:
    print("Invalid Input")
else:
    quadriarea= sidex * sidey
    areatriangle= 1/2*(sidez-sidey)*(sidex)
    peri=quadriarea+areatriangle
    print(math.ceil(peri))
