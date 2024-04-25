cedulas = float(input())
cedulasde100=cedulas // 100
cedulasde50=(cedulas % 100)//50
cedulasde20=((cedulas %100)%50)//20
cedulasde10=(((cedulas %100)%50)%20)//10
cedulasde5= ((((cedulas %100)%50)%20)%10)//5
cedulasde2= (((((cedulas %100)%50)%20)%10)%5)//2
cedulasde1= ((((((cedulas %100)%50)%20)%10)%5)%2)//1
moedasde50= (((((((cedulas %100)%50)%20)%10)%5)%2)%1)//0.50
moedasde25= ((((((((cedulas %100)%50)%20)%10)%5)%2)%1)%0.50)//0.25
moedasde10= (((((((((cedulas %100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)//0.10
moedasde5= ((((((((((cedulas %100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)%0.10)//0.05
moedasde1= (((((((((((cedulas %100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)%0.10)%0.05)/0.01
print("NOTAS:\n%1.0f nota(s) de R$ 100.00\n%1.0f nota(s) de R$ 50.00\n%1.0f nota(s) de R$ 20.00\n%1.0f nota(s) de R$ 10.00\n%1.0f nota(s) de R$ 5.00\n%1.0f nota(s) de R$ 2.00\nMOEDAS:\n%1.0f moeda(s) de R$ 1.00\n%1.0f moeda(s) de R$ 0.50\n%1.0f moeda(s) de R$ 0.25\n%1.0f moeda(s) de R$ 0.10\n%1.0f moeda(s) de R$ 0.05\n%1.0f moeda(s) de R$ 0.01" %(cedulasde100,cedulasde50,cedulasde20,cedulasde10, cedulasde5,cedulasde2,cedulasde1,moedasde50,moedasde25,moedasde10,moedasde5,moedasde1))
