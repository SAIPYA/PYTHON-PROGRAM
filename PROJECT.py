Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
A={2,4,6,8,0};
B={3,5,6,8,9};
print("union:",A|B)
union: {0, 2, 3, 4, 5, 6, 8, 9}
print("intersection:",A&B)
intersection: {8, 6}
print("difference:",A-B)
difference: {0, 2, 4}
print("symmetric difference:",A^B)
symmetric difference: {0, 2, 3, 4, 5, 9}
