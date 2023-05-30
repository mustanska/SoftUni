from collections import deque

bullet_price = int(input())
size_of_gun_barrel = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())

gun_bullets = size_of_gun_barrel
fired_bullets = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()

    if bullet <= lock:
        print("Bang!")
    else:
        locks.appendleft(lock)
        print("Ping!")

    gun_bullets -= 1
    fired_bullets += 1

    if gun_bullets == 0 and bullets:
        gun_bullets = min(size_of_gun_barrel, len(bullets))
        print("Reloading!")


if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = intelligence_value - (fired_bullets * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")