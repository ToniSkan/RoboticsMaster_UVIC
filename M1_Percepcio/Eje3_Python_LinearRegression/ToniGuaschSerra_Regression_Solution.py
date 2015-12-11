# PERCEPTION SYSTEMS EXERCISE 1: REGRESSION		|
#-------------------------------------------------------|
# TONI GUASCH SERRA		November 2015		|
#-------------------------------------------------------|
print ('-------------------------------')
print ('|Exercise 1 Perception Systems|')
print ('-------------------------------')
print ('|     TONI GUASCH SERRA       |')
print ('-------------------------------')

import numpy as np
from scipy.linalg import lstsq as calc

alldata=np.loadtxt('housing.data')

#-----------------FUNCION: MSE------------------------
# MSE = (1/N)*sum((y-X*theta)^2)
def MSE(y,X,theta):
	MSE = float(sum((y-np.dot(X, theta))**2)/len(y))
	return MSE
#------------------------------------------------------


print ('------------')
print ('Q1 EXERCISE')
print ('------------')


y = alldata[:,-1]				#Extract Data of Last column (Files=all, Column -1)
print y.T					#print 'Data points', len(y)
print '- Column 1 Have: %d elemnts.' %len(y)

Halfdata = len(y)/2				#Calculate Half Data
Vectunos = np.ones((len(y),1)) 			#Vector of 1's (BIAS)

print ('------------------------------------------------------------------------------------------------')
#------------------------------Exercise Q2)---------------------------------------------------
print ('------------')
print ('Q2 EXERCISE')
print ('------------')

averageQ2= np.dot(np.dot(np.linalg.inv(np.dot(Vectunos.T, Vectunos)), Vectunos.T), y)	#Calculate average
print '- The average of the target value in mode 2 is:', averageQ2
print '\n- MSE as a constant prediction: ' , MSE(y,Vectunos,averageQ2)			#Q2 MSE calculation using MSE functiono
print ('------------------------------------------------------------------------------------------------')

#------------------------------Exercise Q3)---------------------------------------------------
print ('------------')
print ('Q3 EXERCISE')
print ('------------')
#Split data in two parts 50% and 50% for training and testing

#Testing & Training split
train = alldata[:Halfdata,:-1]			#Training	
train_Out = alldata[:Halfdata,-1]		#Training Out
test = alldata[Halfdata:,:-1]			#Test
test_Out = alldata[Halfdata:,-1]		#Test Out


mse_train=[]
theta=[]
mse_test=[]
for i in range(0,len(alldata[0])-1):
	train_Vect = np.hstack((Vectunos[:Halfdata], train[:,i].reshape(Halfdata,1)))	#Train with BIAS
	test_Vect = np.hstack((Vectunos[:Halfdata], test[:,i].reshape(Halfdata,1)))	#Test with BIAS
	theta.append(calc(train_Vect,train_Out)[0])					#theta calculation 	
	mse_train.append(MSE(train_Out,train_Vect,theta[i]))				#MSE calculation for Train
	mse_test.append(MSE(test_Out,test_Vect,theta[i]))				#MSE calculation for Test


print '\n - Most Informative Variable is: %d, With a MSE of:' % mse_train.index(min(mse_train)), min(mse_train)
print '\n - Most generalizable variable is:', mse_test.index(min(mse_test)), 'With a MSE of:', min(mse_test)
print '\n - Worst generalizable variable is:', mse_test.index(max(mse_test)), 'With a MSE of:', max(mse_test)


# Calculating Coefficient of Determination
mean = sum(test_Out) / Halfdata				#(1/N)*sum(y)
VAR = sum((mean-test_Out)**2) / Halfdata		#(1/N)*sum((mean-y)^2)
FUV = mse_test/VAR					#MSE/VAR
Coeff_Q3 = 1 - FUV					#R^2 = 1-FUV

print '\n\n- Most useful variable is %d with a coefficient of determination of: ' % Coeff_Q3.argmax(axis=0), max(Coeff_Q3)
print ('------------------------------------------------------------------------------------------------')


#------------------------------Exercise Q4)---------------------------------------------------
print ('------------')
print ('Q4 EXERCISE')
print ('------------')

train_Vect = np.hstack((Vectunos[:Halfdata], train.reshape(Halfdata,train.shape[1]))) 	#Train with BIAS
test_Vect = np.hstack((Vectunos[:Halfdata], test.reshape(Halfdata,test.shape[1]))) 	#Test with BIAS
average = calc(train_Vect,train_Out)[0]							#theta calculation
MSEtrain = MSE(train_Out,train_Vect,average)						#MSE for Train
MSEtest = MSE(test_Out,test_Vect,average)						#MSE for Test

MEAN = sum(test_Out) / Halfdata				#(1/N)*sum(y)
VAR = sum((MEAN-test_Out)**2) / Halfdata		#(1/N)*sum((MEAN-y)^2)
FUV = MSEtest / VAR					#MSE/VAR
Coeff_Q4 = 1 - FUV					#R^2 = 1-FUV

print '\n- MSE in the training is:', MSEtrain
print '\n- MSE in the testing is:', MSEtest
print '\n- Coefficient of determination is:', Coeff_Q4

print ('--------------------------------------')
print '\nwithout the worst value of Q3:'

# Removing the worst-performing variable in the features array
train_Q4 = np.delete(train,Coeff_Q3.argmin(axis=0),axis=1)
test_Q4 = np.delete(test,Coeff_Q3.argmin(axis=0),axis=1)

# Starting over the experiment
train_Vect = np.hstack((Vectunos[:Halfdata], train_Q4.reshape(Halfdata,train_Q4.shape[1])))	#Stack all features with Bias term (training)
test_Vect = np.hstack((Vectunos[:Halfdata], test_Q4.reshape(Halfdata,test_Q4.shape[1]))) 	#Stack all features with Bias term (testing)
average = calc(train_Vect,train_Out)[0]								#Calculating the model (theta)
MSEtrain = MSE(train_Out,train_Vect,average)							#Calculating the error (training)
MSEtest = MSE(test_Out,test_Vect,average)							#Calculating the error (testing)

MEAN = sum(test_Out) / Halfdata		#(1/N)*sum(y)
VAR = sum((MEAN-test_Out)**2) / Halfdata		#VAR = (1/N)*sum((MEAN-y)^2)
FUV = MSEtest / VAR		#Fraction of Variance Unexplained (FUV) -> FUV = MSE/VAR
Coeff_Q4_2= 1 - FUV		#Coefficient of determination -> R^2 = 1-FUV

print '\n- MSE in the training withouht the worst variable of Q3 is:' , MSEtrain
print '\n- MSE in the testing withouht the worst variable of Q3 is:' , MSEtest
print '\n- Coefficient of determination withouht the worst variable of Q3 is:' , Coeff_Q4_2
print ('------------------------------------------------------------------------------------------------')



