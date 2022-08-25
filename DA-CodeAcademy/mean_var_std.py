import numpy as np
def calculate(a):
    mydict = {}
    myarr = np.array(a).reshape(3,3)
    mydict["mean"] =[list(np.mean(myarr, axis=0)), list(np.mean(myarr, axis=1)), np.mean(myarr)]
    mydict["variance"] = [list(np.var(myarr, axis=0)), list(np.var(myarr, axis=1)), np.var(myarr)]
    mydict["Standard Deviation"] = [list(np.std(myarr, axis=0)), list(np.std(myarr, axis=1)), np.std(myarr)]
    mydict["max"] = [list(np.max(myarr, axis=0)), list(np.max(myarr, axis=1)), np.max(myarr)]
    mydict["min"] = [list(np.min(myarr, axis=0)), list(np.min(myarr, axis=1)), np.min(myarr)]
    mydict["sum"] = [list(np.sum(myarr, axis=0)), list(np.sum(myarr, axis=1)), np.sum(myarr)]
    return mydict

if __name__ == "__main__":
    result = calculate([0,1,2,3,4,5,6,7,8])
    print(result)

