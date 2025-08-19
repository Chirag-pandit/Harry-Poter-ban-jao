import cv2
import numpy as np
from color_ranges import COLOR_RANGES   # Color ranges ko alag file me rakha hai (modular code ke liye)

# ========================== Background Capture Function ==========================
def capture_background(cap, frames=80):
    """
    Ye function background ko capture karta hai.
    Steps:
    1. User ko 80 frames ke liye camera ke samne se hatna hoga
    2. Har frame ko store karte hain
    3. Fir median (middle value) nikal kar ek clean background banate hain
    Median isliye use hota hai taki agar thoda light flicker ho to smooth ho jaye
    """
    print("\n[INFO] Capturing background... Please move out of the frame.")
    collected_frames = []

    for i in range(frames):
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.flip(frame, 1)   # Flip karte hain taaki mirror effect aaye (natural lagta hai)
        collected_frames.append(frame)

    # Median lete hain saare frames ka (axis=0 matlab vertical direction me combine karna)
    background = np.median(collected_frames, axis=0).astype(np.uint8)

    print("[INFO] Background captured successfully!\n")
    return background


# ========================== Mask Creation Function ==========================
def get_mask(hsv, color_name):
    """
    Ye function cloak ke liye mask banata hai.
    Input: hsv frame + cloak ka color name
    Output: binary mask jaha cloak white dikhega aur baaki black
    
    Steps:
    1. HSV range ke andar aane wale pixels ko white banate hain
    2. Baaki sab ko black
    3. Noise remove karne ke liye morphological operations use karte hain
    """
    mask = None
    ranges = COLOR_RANGES[color_name]

    # Kuch colors (jaise Red) HSV wheel me do jagah hote hain
    for lower, upper in ranges:
        part_mask = cv2.inRange(hsv, lower, upper)   # Range ke andar pixels select karo
        if mask is None:
            mask = part_mask
        else:
            mask = mask | part_mask   # Agar multiple ranges hain to unhe combine kar do

    # Smooth edges aur noise hatane ke liye filters
    mask = cv2.medianBlur(mask, 5)                       # Thoda blur kar dete hain
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))  # Choti moti noise remove
    mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=2)          # Cloak ko thoda strong banane ke liye

    return mask


# ========================== Main Program ==========================
def main():
    # Webcam start karo (0 = default laptop camera)
    cap = cv2.VideoCapture(0)

    # Agar camera nahi khula to error dikhado
    if not cap.isOpened():
        print("[ERROR] Cannot open webcam")
        return

    # Starting background aur cloak color
    background = None
    current_color = "red"

    # User controls print kar do console pe
    print("\n--- Harry Potter Invisibility Cloak ---")
    print("Controls:")
    print("  R = Red cloak")
    print("  G = Green cloak")
    print("  B = Blue cloak")
    print("  W = White cloak")
    print("  C = Capture background")
    print("  Q = Quit\n")

    while True:
        # Camera se ek frame read karo
        ret, frame = cap.read()
        if not ret:
            break

        # Frame ko flip karo (mirror effect)
        frame = cv2.flip(frame, 1)

        # Frame ko HSV me convert karo (color detection HSV me easy hota hai)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        if background is not None:
            # Cloak area ke liye mask banao
            mask = get_mask(hsv, current_color)

            # Inverse mask banao (cloak ke alawa sab)
            inv_mask = cv2.bitwise_not(mask)

            # Cloak ke jagah background chipka do
            cloak_area = cv2.bitwise_and(background, background, mask=mask)

            # Cloak ke alawa original frame show karo
            non_cloak_area = cv2.bitwise_and(frame, frame, mask=inv_mask)

            # Dono ko combine karke final magic effect banao ✨
            display = cv2.addWeighted(cloak_area, 1.0, non_cloak_area, 1.0, 0)
        else:
            # Agar background capture nahi hua hai to normal frame hi dikhado
            display = frame

        # Window ke upar controls text likh do
                # Window ke upar controls text likh do
        status = f"Color: {current_color.upper()} |R/G/B/W = Switch Color|C = Capture BG|Q = Quit"

        # --- Black border + White text ---
        cv2.putText(display, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0,0,0), 3, cv2.LINE_AA)   # Black border (thicker)
        cv2.putText(display, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (255,255,255), 1, cv2.LINE_AA)  # White text (thin)

        # Final output show karo
        cv2.imshow("Gayab Karlo Khudko guys", display)


        # Key press check karo
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):          # Quit
            break
        elif key == ord('r'):        # Red cloak select
            current_color = "red"
        elif key == ord('g'):        # Green cloak select
            current_color = "green"
        elif key == ord('b'):        # Blue cloak select
            current_color = "blue"
        elif key == ord('w'):        # White cloak select
            current_color = "white"
        elif key == ord('c'):        # Background capture
            background = capture_background(cap, frames=80)

    # Program close hone ke baad cleanup karo
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
