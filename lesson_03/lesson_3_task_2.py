from smartphone import Smartphone
catalog = [
    Smartphone("Samsung", "A15", "+79097877564"),
    Smartphone("Samsung", "A10", "+79089097864"),
    Smartphone("Redmi", "9C", "+79062150151"),
    Smartphone("Samsung", "GalaxyS25 Ultra", "+79087776521"),
    Smartphone("Honor", "200 Lite", "+79052481166")]
for smartphone in catalog:
    print(f"{smartphone.mark_phone} {smartphone.model} {smartphone.number}")
