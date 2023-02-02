from smartphone import Smartphone

Smartphone1=Smartphone('Nokia', 'C20', 89255855551)
Smartphone2=Smartphone('Samsung', 'Galaxy Z Flip3', 89255855552)
Smartphone3=Smartphone('Apple', 'iphone10', 89255855553)
Smartphone4=Smartphone('Huawei', 'Mate 50 Pro', 89255855554)
Smartphone5=Smartphone('Xiaomi', 'Redmi 10C', 89255855555)

catalog=[Smartphone1, Smartphone2, Smartphone3, Smartphone4, Smartphone5]

for i in catalog:
    i.printer()