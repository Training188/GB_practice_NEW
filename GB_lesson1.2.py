sec = int(input('Enter seconds: '));
h = sec // 3600;
m = (h // 60) % 60;
s = sec % 60
print(f"Time {h}:{m}:{s}")