
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle, Circle

# Traffic environment
roads = ["North", "East", "South", "West"]

traffic = {
    "North": 7,
    "East": 3,
    "South": 9,
    "West": 5
}

green_road = "South"
step = 0

fig, ax = plt.subplots(figsize=(10, 7))
fig.canvas.manager.set_window_title("Smart Traffic Signal Agent")


def choose_road():
    """Agent selects the road with the most traffic."""
    return max(traffic, key=traffic.get)


def draw_car(x, y, width=0.035, height=0.025):
    ax.add_patch(
        Rectangle(
            (x, y), width, height,
            facecolor="gold",
            edgecolor="black",
            linewidth=0.5
        )
    )


def draw_cars(road, count):
    # Display up to 8 cars per road
    for i in range(min(count, 8)):
        if road == "North":
            x = 0.43 + (i % 2) * 0.07
            y = 0.77 - (i // 2) * 0.055
            draw_car(x, y)

        elif road == "South":
            x = 0.43 + (i % 2) * 0.07
            y = 0.20 + (i // 2) * 0.055
            draw_car(x, y)

        elif road == "West":
            x = 0.18 + (i // 2) * 0.055
            y = 0.43 + (i % 2) * 0.07
            draw_car(x, y, 0.025, 0.035)

        else:
            x = 0.72 - (i // 2) * 0.055
            y = 0.43 + (i % 2) * 0.07
            draw_car(x, y, 0.025, 0.035)


def draw_signal(x, y, road):
    color = "lime" if road == green_road else "red"

    ax.add_patch(
        Circle((x, y), 0.035, color="black", zorder=5)
    )
    ax.add_patch(
        Circle((x, y), 0.022, color=color, zorder=6)
    )


def update(frame):
    global green_road, step

    step += 1

    # Agent observes traffic and decides
    green_road = choose_road()

    # Update the traffic after the agent's decision
    for road in roads:
        if road == green_road:
            traffic[road] = max(
                0, traffic[road] - random.randint(2, 4)
            )
        else:
            traffic[road] = min(
                15, traffic[road] + random.randint(0, 2)
            )

    ax.clear()
    ax.set_facecolor("#263238")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Draw intersection
    ax.add_patch(
        Rectangle((0.36, 0), 0.28, 1, color="#555b61")
    )
    ax.add_patch(
        Rectangle((0, 0.36), 1, 0.28, color="#555b61")
    )

    # Lane markings
    ax.plot([0, 1], [0.5, 0.5],
            color="white", linestyle="--", alpha=0.6)
    ax.plot([0.5, 0.5], [0, 1],
            color="white", linestyle="--", alpha=0.6)

    # Road names
    ax.text(0.5, 0.92, "NORTH", color="white",
            ha="center", fontsize=11, weight="bold")
    ax.text(0.5, 0.08, "SOUTH", color="white",
            ha="center", fontsize=11, weight="bold")
    ax.text(0.08, 0.5, "WEST", color="white",
            ha="center", fontsize=10, rotation=90)
    ax.text(0.92, 0.5, "EAST", color="white",
            ha="center", fontsize=10, rotation=90)

    # Signals
    draw_signal(0.40, 0.70, "North")
    draw_signal(0.70, 0.60, "East")
    draw_signal(0.60, 0.30, "South")
    draw_signal(0.30, 0.40, "West")

    # Cars
    for road in roads:
        draw_cars(road, traffic[road])

    # Live traffic counts
    ax.text(0.68, 0.83, f"North: {traffic['North']} cars",
            color="white", fontsize=10)
    ax.text(0.68, 0.17, f"South: {traffic['South']} cars",
            color="white", fontsize=10)
    ax.text(0.02, 0.76, f"West: {traffic['West']} cars",
            color="white", fontsize=10)
    ax.text(0.76, 0.76, f"East: {traffic['East']} cars",
            color="white", fontsize=10)

    ax.text(
        0.5, 0.99, "SMART TRAFFIC SIGNAL AGENT",
        color="#80d8ff", fontsize=15,
        ha="center", va="top", weight="bold"
    )

    ax.text(
        0.5, 0.945,
        "Observe traffic  ->  Decide  ->  Change signal",
        color="white", fontsize=10, ha="center"
    )

    ax.text(
        0.5, 0.015,
        f"Step {step} | GREEN SIGNAL: {green_road}",
        color="#b9f6ca", fontsize=12,
        ha="center", va="bottom", weight="bold"
    )

    fig.tight_layout()


animation = FuncAnimation(
    fig,
    update,
    interval=1200,
    cache_frame_data=False
)

update(0)
plt.show()
