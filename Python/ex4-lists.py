users = ["Bob", "Alice", "Mike"]

print(users)
print(f"Initial list lenght : {len(users)}")

users.append("Mari")
print(f"Initial list lenght : {len(users)}")

print(f"on index 2 we have : {users[2]}")
users[2]="Patrick"
print(f"on index 2 we have : {users[2]}")

prieteni = ["Ana", "Maria", "Calin"]
users.extend(prieteni)
users.sort()
print(users)