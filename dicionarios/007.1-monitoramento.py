sensores = ["S-001", "S-002", "S-003", "S-004", "S-005"]
temperaturas = [22.5, 31.0, 19.8, 45.2, 25.0]

status_sensores = dict()

for sen, temp in zip(sensores, temperaturas):
    status_sensores[sen] = temp
    
print(status_sensores)