#X: N \times D -- matrix 
#Y: {0,1} N \times 1    

#    objective is to learn 
#    w: D \times 1 given X and Y according to a logistic regression model
        
        
import numpy as np
class LogisticRegression:
    
    def __init__(self, X):
        self.w = np.ones(np.shape(X)[1])
        
    def get_w(self, X, Y):
        # d/dw (cost_fn)
        self.w = -np.dot(Y, 1/self.hyp(X)) + np.dot((1-Y), 1/(1-self.hyp(X)))
    
    def hyp(self, X):
        return 1 / (1 - np.exp(-np.transpose(self.w) * X))
    
    def cost(self, X, Y):
        return -np.dot(Y, np.log(self.hyp(X))) - np.dot((1 - Y),  np.log(1 - self.hyp(X)))
np.random.seed(2)
X = np.random.random((3,3))
Y = np.random.random((1,3))

fn = LogisticRegression(X)
fn.get_w(X,Y)
print(fn.w)
