temps = [32, 46, 95, 10, 50]
answer = input("Enter the value here: ")
answer = int(answer)
temps.append(answer)
temps.reverse()

print(temps.index(95))
print(temps.count(95))