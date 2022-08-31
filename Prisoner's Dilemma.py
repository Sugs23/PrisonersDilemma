
# 			      B Loyal (0)		B Snitch (1)
#A Loyal (0)		 (R, R)		     (S, T)
#A Snitch (1)		 (T, S) 		 (P, P)

#where T, R, P and S are payoffs and 
#   T>R>P>S

#Code:

import random
import matplotlib.pyplot as plt
import numpy as np

#payoff function to calculate payoff based on strategy
def payoff(Mystrat, Otherstrat, T, R, P, S):

	if Mystrat == 0 and Otherstrat == 0:
		return R

	if Mystrat == 0 and Otherstrat == 1:
		return S

	if Mystrat == 1 and Otherstrat == 0:
		return T

	if Mystrat == 1 and Otherstrat == 1:
		return R


#function to process list to plot on graph
#list has average expected returns from every point  
#if value at t+1 is not updated from value at t, the average stays same
def list_ready(lst, rounds):
    cnt=1
    it=1
    while it<rounds-1:
        lst[it] = lst[it]/cnt
        while lst[it] == lst[it+1]:
            it+=1
        cnt+=1
        it+=1
    lst[rounds-1]= lst[rounds-2]
    return lst
    

	
def main():

	#get input(T, R, P, S)
    T = int(input("Enter T value: "))
    R = int(input("Enter R value: "))
    P = int(input("Enter P value: "))
    S = int(input("Enter S value: "))

    rounds = int(input("Enter Number of iterations: "))

	#initialise 4 variables to store total payoffs for A and B for both strategies (snitch and stay loyal)
    A_snitch = 0
    A_loyal  = 0
    B_snitch = 0
    B_loyal  = 0

	#lists for plots
    A_snitch_plots = []
    A_loyal_plots  = []
    B_snitch_plots = []
    B_loyal_plots  = []


	#start iteration
    for _ in range(0,rounds):
        #list for strategy (0 for Loyal, 1 for Snitch)
        strat = [0,1]

		#randomly choose A and B strategy
        Astrat = random.choice(strat)
        Bstrat = random.choice(strat)

		#add the payoffs 
        if Astrat==0:
            A_payoff = payoff(Astrat, Bstrat, T, R, P, S)
            A_loyal += A_payoff
        
        if Astrat==1:
            A_payoff = payoff(Astrat, Bstrat, T, R, P, S)
            A_snitch += A_payoff

        if Bstrat==0:
            B_payoff = payoff(Bstrat, Astrat, T, R, P, S)
            B_loyal += B_payoff
        
        if Bstrat==1:
            B_payoff = payoff(Bstrat,Astrat, T, R, P, S)
            B_snitch += B_payoff
        
        A_snitch_plots.append(A_snitch)
        A_loyal_plots.append(A_loyal)
        B_snitch_plots.append(B_snitch)
        B_loyal_plots.append(B_loyal)

    #Calculate the expected payoff for both the players for both strategies 
    A_snitch_expected = A_snitch/rounds
    A_loyal_expected  = A_loyal/rounds
    B_snitch_expected = B_snitch/rounds
    B_loyal_expected  = A_loyal/rounds
    

    #Make the list ready for plotting
    A_Snitch_final = list_ready(A_snitch_plots, rounds)
    A_Loyal_final  = list_ready(A_loyal_plots, rounds)
    B_Snitch_final = list_ready(A_snitch_plots, rounds)
    B_Loyal_final  = list_ready(A_loyal_plots, rounds)

    #declare figure where the plots will be made 
    figure, axis = plt.subplots(2, 2)

    #Convert the list into NumPy array and plot it on logarithmic scale

    #plotting A snitches
    A_snitch_np = np.array(A_Snitch_final)
    axis[0][0].plot(A_snitch_np[10:-1], 'b')
    axis[0][0].set_title("A snitches")
    axis[0][0].set_xscale('log')

    #plotting A stays loyal
    A_loyal_np = np.array(A_Loyal_final)
    axis[1][0].plot(A_loyal_np[10:-1], 'b')
    axis[1][0].set_title("A stays loyals")
    axis[1][0].set_xscale('log')

    #plotting B snitches
    B_snitch_np = np.array(B_Snitch_final)
    axis[0][1].plot(B_snitch_np[10:-1], 'b')
    axis[0][1].set_title("B snitches")
    axis[0][1].set_xscale('log')

    #plotting A stays loyal
    B_loyal_np = np.array(B_Loyal_final)
    axis[1][1].plot(B_loyal_np[10:-1], 'b')
    axis[1][1].set_title("B stays loyals")
    axis[1][1].set_xscale('log')

    #Print results 
    print("Expected Payoff if A always snitches: ", A_snitch_expected)
    print("Expected Payoff if A never snitches: ", A_loyal_expected)
    print("Expected Payoff if B always snitches: ", B_snitch_expected)
    print("Expected Payoff if A never snitches: ", B_loyal_expected)

    #Displaying the final Plot
    plt.show()
    
	
if __name__ == "__main__":
    main()