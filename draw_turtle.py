import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Shell
shell = patches.Circle((0, 0), radius=1, color='darkgreen')
ax.add_patch(shell)

# Head
head = patches.Circle((0, 1.2), radius=0.2, color='green')
ax.add_patch(head)

# Legs
leg_coords = [(-0.8, 0.6), (0.8, 0.6), (-0.8, -0.6), (0.8, -0.6)]
for x, y in leg_coords:
    leg = patches.Circle((x, y), radius=0.15, color='green')
    ax.add_patch(leg)

# Tail
tail = patches.RegularPolygon((0, -1.2), numVertices=3, radius=0.2, color='green')
ax.add_patch(tail)

# Eyes
eye_white = patches.Circle((-0.07, 1.33), radius=0.05, color='white')
eye_black = patches.Circle((-0.07, 1.33), radius=0.02, color='black')
ax.add_patch(eye_white)
ax.add_patch(eye_black)

eye_white2 = patches.Circle((0.07, 1.33), radius=0.05, color='white')
eye_black2 = patches.Circle((0.07, 1.33), radius=0.02, color='black')
ax.add_patch(eye_white2)
ax.add_patch(eye_black2)

plt.show()
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Shell
shell = patches.Circle((0, 0), radius=1, color='darkgreen')
ax.add_patch(shell)

# Head
head = patches.Circle((0, 1.2), radius=0.2, color='green')
ax.add_patch(head)

# Legs
leg_coords = [(-0.8, 0.6), (0.8, 0.6), (-0.8, -0.6), (0.8, -0.6)]
for x, y in leg_coords:
    leg = patches.Circle((x, y), radius=0.15, color='green')
    ax.add_patch(leg)

# Tail
tail = patches.RegularPolygon((0, -1.2), numVertices=3, radius=0.2, color='green')
ax.add_patch(tail)

# Eyes
eye_white = patches.Circle((-0.07, 1.33), radius=0.05, color='white')
eye_black = patches.Circle((-0.07, 1.33), radius=0.02, color='black')
ax.add_patch(eye_white)
ax.add_patch(eye_black)

eye_white2 = patches.Circle((0.07, 1.33), radius=0.05, color='white')
eye_black2 = patches.Circle((0.07, 1.33), radius=0.02, color='black')
ax.add_patch(eye_white2)
ax.add_patch(eye_black2)

plt.show()

