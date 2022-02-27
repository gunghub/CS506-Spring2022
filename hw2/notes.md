用命令行啟動 notebook。  
/opt/anaconda3/envs/gung_python_env/bin/jupyter notebook --no-browser

隨機數
import random
print(random.randint(0,9))

CIFAR 參考
https://github.com/gunghub/CIFAR


有一個 4 維 array A，代表一組 images。
x 是 A 中的一個數值，其坐標為 [100, 23, 67, 1]。
代表第 101 張 image，第 24 row，第 68 column，第 2 個 channel 的值。

B = A.transpose(3,0,2,1)
那麼 x 在重新排列的 array B 中對應的數值為 x' ，其坐標為 [1, 100, 67, 23]。

即
A[100, 23, 67, 1] = B[1, 100, 67, 23]




# 多列圖片
```
import numpy as np
import matplotlib.pyplot as plt
from six.moves import cPickle 

f = open('data/cifar10/cifar-10-batches-py/data_batch_1', 'rb')
datadict = cPickle.load(f,encoding='latin1')
f.close()
X = datadict["data"] 
Y = datadict['labels']
X = X.reshape(10000, 3, 32, 32).transpose(0,2,3,1).astype("uint8")
Y = np.array(Y)

#Visualizing CIFAR 10
fig, axes1 = plt.subplots(5,5,figsize=(3,3))
for j in range(5):
    for k in range(5):
        i = np.random.choice(range(len(X)))
        axes1[j][k].set_axis_off()
        axes1[j][k].imshow(X[i:i+1][0])
```

