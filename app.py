import time
import pickle
import os
import warnings
warnings.filterwarnings("ignore")
genie_image = r'''
                               .
              .:::.....:::::::..  :.
           .::::::::::::::::::::::.::.
          :       `::::::::::::::::::::.
                      `::::::::::::::::::.
                              `::::::::::::
                                `::::::::::
                                  `:::::::
                  %%,   .::::.      `:::'      .::::.        ,%%%%
                  `%%%, :::::::.    oOOOo    .:::::::.     ,%%;%%%
                   `%%%,::%%%%::%%%%%%%%%%%%%::%%%%%::%   %%%;%%%
                    `%%,%%%%%%%:%%%%%%%%%%%%%%%%%%%%:'%%,%%%;%%%
                     %%,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,%%;%%%;
                     %%,%;a@@@a;%%%%%%%%%;a@@@@@@a;%%%%%%%%%;%%%
               .oOOOo%,%;@@@@@@@a;%%%%%%;@@@@@@@@@a;%%%%%%,%%;%%
               OOO' .,%;a@@@@@@@@a;%%%%;@@@@@@@@@@@;%%%%%%%%,%;%,
               `OO.%%%%;@@@@@@@@@@;%%%;@@@@@@@@@@@@;%;%%%%%%%,%%%
                 ;%%%%;%;@@@@@@@@@;%%%;@@@@@@@@@@@;;%%%%%%%%%,%%%
                 `%%%%%%;;@@@@@@@@;%%%;@@@@@@@@@;%%%%%%%%%%%,%%%'
                  `%%%%%%%;;@@' .;%%%%%, `@@@@;%%%%%%%;%%%%,%%%'
                   `%;%;%%%%%%%%`%%%%%%%%%%%%%%%%;%;%;%%%%%,""
                   :%%%;,%;%%`%%%%%%%%%%%%%%%%%%%%;;%%%::%%;
                 ::%%%%;O;%%`%%%%%%%%%%%%%%%%%%%%;O;%%%%::%;
               ::%%%%%%;OO;%`%%%%%%%%%%%'%%%%%%%;OO;;%%%%::%
              ::%%%%%%;OOOOOO`%%%%%%%%'%%%%;OOOOOOOO;%%%%%::%
            ::%%%%%%%;OOOOOOOOOO`%%%%'OOOOOOOOOOOOOOO;%%%%%::.
          ::%%%%%%%%;                                ;%%%%%%::.
         ::%%%%%%%%;           ,;;;;;;;;;,;;;;;;;;;, ,;%%%%%%::.
        ::%%%%%%%;           .;;;;;;;;;;,;;;;;;;;;;;oO;%%%%%%%::
       ::%%%%%;OOo,.         ;;;;;;;;;;;;;;;;;;ooOOOOOO;%%%%%%::
       ::%%%%%;OOOOOOoOOOOOOOOoOOOOOOOOoOOOOOOOOOOOOOO;%%%%%%%::
       ::%%%%%%;OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO;%%%%%%%%%::
        ::%%%%%%%%%;OOOOOOOOOOOOOOOOOOOOOOOOOOOO;%%%%%%%%%%%%::'
         `::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:::'
           `:::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%::::'
             `:::::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:::::'
                `:::::%%%%%%%%%%%%%%%%%%%%%%%%%%%::::::'
                   `:::::::::::::::::::::::::::::::'
                      `:::::::::::::::::::::::::'
                         `::::::::::::::::::'
                            `:::::::::::'
                              `:::::::'
                              .::::'
                             .:::'
                            :::'
                           ::'   .::::.
                           ::.   ::  `::
                            ::.   `  .::
                             `::::::::' 
'''

print("Hello Welcome To Diamond Genie")
time.sleep(1)
print(genie_image)
time.sleep(1)
print("I can Help You estimate amount of money you should take with you !")
time.sleep(2)
print("Please Enter the details of the diamond you want to buy.")
#filename = open('C:\Users\Lenovo\Desktop\Code\Project\dt_reg.pkl', 'rb')
#C:\Users\Lenovo\Desktop\Code\Project\dt_reg.pkl

filename = 'dt_reg.pkl'
dt_model_loaded = pickle.load(open(filename, "rb"))

carat = float(input("Enter the carats of diamond  you want to buy : "))
cut = int(input("Enter the type of cut you would prefer \n 1.Fair \n 2.Good \n 3.Ideal \n 4.Premium \n 5.Very Good \nEnter Your Choice : "))
color = int(input("Enter the color of the diamond you want to buy \n 1.D(best) \n 2.E \n 3.F \n 4.G \n 5.H \n 6.I \n 7.J \nEnter Your choice : "))
clarity = int(input("Enter the clarity of the diamond you want to buy \n 1.IF(BEST) \n 2.VS1 \n 3.VS2 \n 4.SI1 \n 5.SI2 \n 6.I1 \nEnter your choice : "))
'''['I1' 'IF' 'SI1' 'SI2' 'VS1' 'VS2' 'VVS1' 'VVS2']'''
#     0   1     2     3     4     5     6       7
if clarity==1:
    clarity=1
elif clarity==2:
    clarity=4
elif clarity==3:
    clarity=5
elif clarity==4:
    clarity=2
elif clarity==5:
    clarity=3
elif clarity==6:
    clarity=0

depth = float(input("Enter the depth percentage of diamond  you want to buy : "))
table = float(input("Enter the table of diamond you want to buy : "))
length_x = float(input("Enter the length of diamond you want to buy : "))
width_y = float(input("Enter the width of diamond you want to buy : "))
depth_z = float(input("Enter the depth of diamond you want to buy : "))


preds_dt = dt_model_loaded.predict([[carat,cut,color,clarity,depth,table,length_x,width_y,depth_z]])
print("The price of diamond you want : $",int(preds_dt))





'''
Color : J (worst) to D (best)
clarity : a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))
['Fair' 'Good' 'Ideal' 'Premium' 'Very Good']
    0     1      2        3         4
['D' 'E' 'F' 'G' 'H' 'I' 'J']
['I1' 'IF' 'SI1' 'SI2' 'VS1' 'VS2' 'VVS1' 'VVS2']'''




