import numpy as np

# HSV color ranges dictionary
# HSV (Hue, Saturation, Value) → color detection ke liye best hai 
# kyunki lighting change hone pe bhi stable rehta hai

COLOR_RANGES = {
    "red": [
        # Red color HSV do parts me aata hai (0-10 aur 170-180)
        (np.array([0, 120, 70]), np.array([10, 255, 255])),
        (np.array([170, 120, 70]), np.array([180, 255, 255]))
    ],
    "green": [
        (np.array([40, 40, 40]), np.array([90, 255, 255]))
    ],
    "blue": [
        (np.array([100, 150, 0]), np.array([140, 255, 255]))
    ],
    "white": [
        # White ke liye saturation kam aur value high hota hai
        (np.array([0, 0, 200]), np.array([180, 30, 255]))
    ],
}
