#Vinni Paradiso Problem 3

import dbm
db1=dbm.open("houses", "c")
db1["House_1.jpeg"]="a 2 bed, 3 bath Victorian house in South Bend"
db1["House_2.jpeg"]="a 3 bed, 6 bath Modern house in South Bend"
db1["House_3.jpeg"]="an 8 bed, 8 bath Victorian house in Granger"
db1["House_4.jpeg"]="a 6 bed, 4 bath house in South Bend"
db1["House_5.jpeg"]="a 2 bed, 2 bath house in South Bend"
db1["House_6.jpeg"]="a 1 bed, 1 bath Victorian house in South Bend"

for item in db1:
    print(item, db1[item])
