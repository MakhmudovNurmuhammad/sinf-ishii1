
kun = input("kun.oy.yil -> ")
soat = input("saot:minut -> ")
kun_1 = kun.split(".")
soat_1 = soat.split(":")
yil = {
    '01':"Yanvar",
    '02':"Fevral",
    '03':"Mart",
    '04':"Aprel",
    '05':"May",
    '06':"Iyun",
    '07':"Iyul",
    '08':"Avgust",
    '09':"Sentabr",
    '10':"Oktabr",
    '11':"Noyabr",
    '12':"Dekabr",
}
print(f"{kun} == {kun_1[0]} {yil[kun_1[1]]} {kun_1[-1]} yil")
print(f"{soat} == {soat_1[0]} saot {soat_1[1]} minut")
