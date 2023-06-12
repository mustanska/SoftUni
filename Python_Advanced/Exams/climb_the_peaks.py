from collections import deque

DAYS = 7

daily_portions = deque([int(x) for x in input().split(", ")])
daily_stamina = deque([int(x) for x in input().split(", ")])

conquered_peaks = []

peaks = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])

for _ in range(DAYS):
    portion = daily_portions.pop()
    stamina = daily_stamina.popleft()

    sum_daily = portion + stamina

    if sum_daily >= peaks[0][1]:
        conquered_peaks.append(peaks[0][0])
        peaks.popleft()

    if not peaks:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print(*conquered_peaks, sep="\n")
