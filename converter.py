def conversion (currency_type, dollar_value):
    currency = input("¿How many " + currency_type + " do you have ?: ")
    currency = float(currency)
    dollars = currency / dollar_value
    dollars = round(dollars, 3) # round nos sirve para redondear la cantidad de decimales
    dollars = str(dollars)
    print("You have $" + dollars + " American dollars")
menu = """
Welcome to the currency converter

1 - Colombian Pesos
2 - Argentine Pesos
3 - Mexican Pesos
4 - Afghan Afghans
5 - Madagascan Ariary
6 - Thai Baht
7 - Balboa
8 - Ethiopian Birr
9 - Boliviano
10 - Cedi
11 - Kenyan shilling
12 - Somali shilling
13 - Tanzanian shilling
14 - Ugandan shilling
15 - colon Costa Rican
16 - Salvadoran colón 
17 - Czech koruna
18 - Danish krone
19 - krona Icelandic
20 - Norwegian Krone
21 - Swedish Krona
22 - Córdoba
23 - Dalasi 
24 - Macedonian Denar
25 - Algerian dinar
26 - Bareini Dinar
27 - Iraqi Dinar
28 - Jordanian dinar 333333
29 - Fijian dollar
30 - Kuwaiti dinar
31 - Libyan dinar
32 - Serbian dinar
33 - Vietnamese Đồng
34 - Tunisian dinar
35 - dram Armenian
36 - United Arab Emirates dirham
37 - Moroccan dirham
38 - Australian dollar
39 - Bahamian Dollar
40 - Belize Dollar
41 - Bermudian Dollar 
42 - Canadian dollar 
43 - Barbadian Dollar 
44 - Brunei dollar
45 - Hong Kong dollar
46 - Singapore dollar
47 - Cayman Islands Dollar
48 - Solomon Islands Dollar
49 - East Caribbean dollar
50 - Guyanese dollar
51 - Jamaican dollar
52 - Liberian dollar
53 - Namibian dollar
54 - New Zealand dollar
55 - Surinamese dollar
56 - Trinidadian Dollar
57 - Cape Verdean Shield
58 - Euro
59 - Netherlands Antillean guilder
60 - Aruban Florin
61 - Hungarian Forint
62 - Central African CFA Franc
63 - CFA franc from West Africa
64 - Franco CFP
65 - Burundian franc
66 - Comorian franc
67 - Congolese franc
68 - Guinea franc
69 - Rwandan franc
70 - Swiss franc
71 - Djiboutian franc
72 - Gourde
73 - Grivna
74 - Paraguayan Guarani
75 - China
76 - Lao Kip
77 - Chinese yuan (extracontinental)
78 - Croatian Kuna
79 - Malawi Kwacha
80 - Zambian Kwacha
81 - kwanza Angolan
82 - Burmese Kyat
83 - Georgian Lari
84 - Lek Albanian
85 - Lempira Honduran
86 - Leone
87 - Moldovan leu
88 - Romanian leu
89 - Lev
90 - Egyptian Pound
91 - Pound sterling
92 - Lebanese pound
93 - Sudanese pound
94 - Lilangeni
95 - Turkish lira
96 - Loti
97 - Manat azerbaiyano
98 - Manat turcomano
99 - Bosnian-Herzegovinian mark
100 - Metical mozambiqueño
101 - Naira
102 - Ngultrum butanés
103 - New Taiwan Dollar
104 - New Belarusian ruble
105 - New shekel
106 - Pa'anga
107 - Macao Pataca
108 - Chilean peso
109 - Dominican Peso
110 - Philippine peso
111 - Uruguayan peso
112 - Pula
113 - Quetzal
114 - South African rand
115 - Brazilian real
116 - Renminbi
117 - Rial
118 - Rial Iranian
119 - Rial Yemeni
120 - Riel Cambodian 
121 - Malaysian Ringgit
122 - Qatari riyal
123 - Saudi Riyal
124 - Russian ruble
125 - Maldivian Rupee
126 - Mauritian Rupee
127 - Seychelles Rupia
128 - Sri Lankan Rupee
129 - Rupee india
130 - Indonesian Rupiah
131 - Nepalese rupee
132 - Pakistani Rupee 
133 - Kyrgyz Som
134 - Uzbek Som
135 - Somoni Tajikistan
136 - Taka bangladesí
137 - tenge Kazakh
138 - Uguiya
139 - South Korean won 
140 - Japanese yen
141 - Golden
142 - Venezuelan bolivar
143 - Cuban peso
144 - Peruvian sol
145 - Chilean development unit



Choose an option: """
option = int(input(menu))
if option == 1:
    conversion("Colombian pesos", 4065)
elif option == 2:
    conversion("Argentine pesos", 102)
elif option == 3:
    conversion("Mexican pesos", 20)
elif option == 4:
    conversion("Afghan Afghans", 103.37)
elif option == 5:
    conversion("Madagascan Ariary", 3956.67)
elif option == 6:
    conversion("Thai Baht", 33.27)
elif option == 7:
    conversion("Balboa", 1)
elif option == 8:
    conversion("Ethiopian Birr", 49.37)
elif option == 9:
    conversion("Boliviano", 6.87)
elif option == 10:
    conversion("Cedi", 6.16)
elif option == 11:
    conversion("Kenyan shilling", 112.75)
elif option == 12:
    conversion("Somali shilling", 574.37)
elif option == 13:
    conversion("Tanzanian shilling", 2296.12)
elif option == 14:
    conversion("Ugandan shilling", 3532.41)
elif option == 15:
    conversion("colon Costa Rican", 639.48)
elif option == 16:
    conversion("Salvadoran colón ", 8.71)
elif option == 17:
    conversion("Czech koruna", 21.93)
elif option == 18:
    conversion("Danish krone", 6.56)
elif option == 19:
    conversion("krona Icelandic", 130.11)
elif option == 20:
    conversion("Norwegian Krone", 8.83)
elif option == 21:
    conversion("Swedish Krona", 9.06)
elif option == 22:
    conversion("Córdoba", 35.28)
elif option == 23:
    conversion("Dalasi", 52.75)
elif option == 24:
    conversion("Macedonian Denar", 54.23)
elif option == 25:
    conversion("Algerian dinar", 138.93)
elif option == 26:
    conversion("Bareini Dinar", 0.38)
elif option == 27:
    conversion("Iraqi Dinar", 1454.02)
elif option == 28:
    conversion("Jordanian dinar", 0.71)
elif option == 29:
    conversion("Fijian dollar", 2.12)
elif option == 30:
    conversion("Kuwaiti dinar", 0.30)
elif option == 31:
    conversion("Libyan dinar", 4.58)
elif option == 32:
    conversion("Serbian dinar", 103.49)
elif option == 33:
    conversion("Vietnamese Đồng", 2.12)
elif option == 34:
    conversion("Tunisian dinar", 2.88)
elif option == 35:
    conversion("dram Armenian", 477.03)
elif option == 36:
    conversion("United Arab Emirates dirham", 3.67)
elif option == 37:
    conversion("Moroccan dirham", 9.26)
elif option == 38:
    conversion("Australian dollar", 1.38)
elif option == 39:
    conversion("Bahamian Dollar", 1)
elif option == 40:
    conversion("Belize Dollar", 2.01)
elif option == 41:
    conversion("Bermudian Dollar", 1)
elif option == 42:
    conversion("Canadian dollar", 1.27)
elif option == 43:
    conversion("Barbadian Dollar", 2.01)
elif option == 44:
    conversion("Brunei dollar", 1.35)
elif option == 45:
    conversion("Hong Kong dollar", 7.80)
elif option == 46:
    conversion("Singapore dollar", 1.35)
elif option == 47:
    conversion("Cayman Islands Dollar", 0.83)
elif option == 48:
    conversion("Solomon Islands Dollar", 8.09)
elif option == 49:
    conversion("East Caribbean dollar", 2.70)
elif option == 50:
    conversion("Guyanese dollar", 208.40)
elif option == 51:
    conversion("Jamaican dollar", 153.43)
elif option == 52:
    conversion("Liberian dollar", 145.12)
elif option == 53:
    conversion("Namibian dollar", 15.95)
elif option == 54:
    conversion("New Zealand dollar", 1.46)
elif option == 55:
    conversion("Surinamese dollar", 20.81)
elif option == 56:
    conversion("Trinidadian Dollar", 6.77)
elif option == 57:
    conversion("Cape Verdean Shield", 97.07)
elif option == 58:
    conversion("Euro", 0.88)
elif option == 59:
    conversion("Netherlands Antillean guilder" , 1.80)
elif option == 60:
    conversion("Aruban Florin", 1.80)
elif option == 61:
    conversion("Hungarian Forint", 325.73)
elif option == 62:
    conversion("Central African CFA Franc", 577.45)
elif option == 63:
    conversion("CFA franc from West Africa", 577.49)
elif option == 64:
    conversion("Franco CFP", 105.85)
elif option == 65:
    conversion("Burundian franc", 1987.76)
elif option == 66:
    conversion("Comorian franc", 434.88)
elif option == 67:
    conversion("Congolese franc", 2002.50)
elif option == 68:
    conversion("Guinea franc", 9212.53)
elif option == 69:
    conversion("Rwandan franc", 1033.74)
elif option == 70:
    conversion("Swiss franc", 0.91)
elif option == 71:
    conversion("Djiboutian franc", 177.41)
elif option == 72:
    conversion("Gourde", 99.93)
elif option == 73:
    conversion("Grivna", 27.19)
elif option == 74:
    conversion("Paraguayan Guarani", 6856.45)
elif option == 75:
    conversion("China", 3.50)
elif option == 76:
    conversion(" Laotian Kip", 11137.09)
elif option == 77:
    conversion("Chinese yuan (extracontinental)", 6.36)
elif option == 78:
    conversion("Croatian Kuna", 6.61)
elif option == 79:
    conversion("Malawi Kwacha", 813.55)
elif option == 80:
    conversion("Zambian Kwacha", 16.60)
elif option == 81:
    conversion("kwanza Angolan", 550.59)
elif option == 82:
    conversion("Burmese Kyat", 1771.80)
elif option == 83:
    conversion("Georgian Lari", 3.09)
elif option == 84:
    conversion("Lek Albanian", 106.31)
elif option == 85:
    conversion("Lempira Honduran", 24.44)
elif option == 86:
    conversion("Leone", 11255.00)
elif option == 87:
    conversion("Moldovan leu", 17.73)
elif option == 88:
    conversion("Romanian leu", 4.35)
elif option == 89:
    conversion("Lev", 1.72)
elif option == 90:
    conversion("Egyptian Pound", 15.74)
elif option == 91:
    conversion("Pound sterling", 0.74)
elif option == 92:
    conversion("Lebanese pound", 1506.85)
elif option == 93:
    conversion("Sudanese pound", 437.50)
elif option == 94:
    conversion("Lilangeni", 15.89)
elif option == 95:
    conversion("Turkish lira", 13.41)
elif option == 96:
    conversion("Loti", 15.95)
elif option == 97:
    conversion("Manat azerbaiyano", 1.70)
elif option == 98:
    conversion("Manat turcomano", 3.51)
elif option == 99:
    conversion("Bosnian-Herzegovinian mark", 1.72)
elif option == 100:
    conversion("Metical mozambiqueño", 63.83)
elif option == 101:
    conversion("Naira", 409.59)
elif option == 102:
    conversion("Ngultrum butanés", 74.10)
elif option == 103:
    conversion("New Taiwan Dollar", 27.65)
elif option == 104:
    conversion("New Belarusian ruble", 2.55)
elif option == 105:
    conversion("New shekel", 3.11)
elif option == 106:
    conversion("Pa'anga", 2.27)
elif option == 107:
    conversion("Macao Pataca", 8.00)
elif option == 108:
    conversion("Chilean peso", 852.00)
elif option == 109:
    conversion("Dominican Peso", 57.01)
elif option == 110:
    conversion("Philippine peso", 51.01)
elif option == 111:
    conversion("Uruguayan peso", 44.46)
elif option == 112:
    conversion("Pula", 11.72)
elif option == 113:
    conversion("Quetzal", 7.69)
elif option == 114:
    conversion("South African rand", 15.97)
elif option == 115:
    conversion("Brazilian real", 5.60)
elif option == 116:
    conversion("Renminbi", 6.36)
elif option == 117:
    conversion("Rial", 0.39)
elif option == 118:
    conversion("Rial Iranian", 42275.00)
elif option == 119:
    conversion("Rial Yemeni", 250.25)
elif option == 120:
    conversion("Riel Cambodian", 4058.18)
elif option == 121:
    conversion("Malaysian Ringgit", 4.17)
elif option == 122:
    conversion("Qatari riyal", 3.64)
elif option == 123:
    conversion("Saudi Riyal", 3.76)
elif option == 124:
    conversion("Russian ruble", 75.16)
elif option == 125:
    conversion("Maldivian Rupee", 15.40)
elif option == 126:
    conversion("Mauritian Rupee", 43.64)
elif option == 127:
    conversion("Seychelles Rupia", 13.61)
elif option == 128:
    conversion("Sri Lankan Rupee", 202.18)
elif option == 129:
    conversion("Rupee india", 74.40)
elif option == 130:
    conversion("Indonesian Rupiah", 14263.05)
elif option == 131:
    conversion("Nepalese rupee", 118.55)
elif option == 132:
    conversion("Pakistani Rupee", 175.88)
elif option == 133:
    conversion("Kyrgyz Som", 84.80)
elif option == 134:
    conversion("Uzbek Som", 10782.62)
elif option == 135:
    conversion("Somoni Tajikistan", 11.26)
elif option == 136:
    conversion("Taka bangladesí", 5.43)
elif option == 137:
    conversion("Tenge Kazakh", 433.51)
elif option == 138:
    conversion("Uguiya", 37.45)
elif option == 139:
    conversion("South Korean won", 1192.55)
elif option == 140:
    conversion("Japanese yen", 115.28)
elif option == 141:
    conversion("Golden", 4.05)
elif option == 142:
    conversion("Venezuelan bolivar", 4.58)
elif option == 143:
    conversion("Cuban peso", 23.92)
elif option == 144:
    conversion("Peruvian sol", 3.98)
elif option == 145:
    conversion("Chilean development unit", 0.027)




else:
    print("Enter a correct option please")
    