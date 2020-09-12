print("TESTING")


with open("ssm-test-file.txt") as f:
    print(f.readline())

with open("ssm-test-file.txt", "w") as f:
    f.write("Hello there!")

print("TEST SUCCESS!")

