def changeTemperature(temperatureC=0, temperatureF=0):
    celsius = int((temperatureF - 32) // 1.8)
    fahrenheit = int(temperatureC * 1.8 + 32)
    print(f"Temperature for {temperatureF}F: {celsius}C\nTemperature for {temperatureC}C: {fahrenheit}F")


changeTemperature()
