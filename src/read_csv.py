import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    df = pd.read_csv("../data/AAPL.csv")
    print (df.tail(5))
    print (df[10:20])

def get_max_close(sym):
    df = pd.read_csv("../data/{}.csv".format(sym))
    return df['Close'].max()

def get_mean_volume(sym):
    df = pd.read_csv("../data/{}.csv".format(sym))
    return df['Volume'].mean()

def plot_adj_close(sym):
    df = pd.read_csv("../data/{}.csv".format(sym))
    df['Adj Close'].plot() 
    plt.show()

def plot_high(sym):
    df = pd.read_csv("../data/{}.csv".format(sym))
    df['High'].plot()
    plt.xlabel('Time')
    plt.ylabel('High Price')
    plt.title('{} stock'.format(sym))
    plt.show()
    
def plot_col(sym, cols):
    df = pd.read_csv("../data/{}.csv".format(sym))
    df[cols].plot()
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('{} stock'.format(sym))
    plt.show()    

if __name__ == "__main__":
    test_run()
    
    for sym in ['AAPL', 'IBM']:
        print("Max close ", sym, " = ", get_max_close(sym))
        print("Mean Volume ", sym, " = ", get_mean_volume(sym))
        #plot_adj_close(sym)
        #plot_high(sym)
        
        plot_col(sym, ['Close', 'Adj Close'])

    
