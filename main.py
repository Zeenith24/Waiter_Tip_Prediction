import tensorflow as tf 
import pandas as pd 
import numpy as np


data = pd.read_csv("C:\\Users\\harsh\\Desktop\\codeWork\\tips.csv")
print(data.head(5))
x= data['total_bill'].values
y = data['tip'].values

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])
])

model.compile(
    optimizer = tf.keras.optimizers.Adam(learning_rate = 0.01),

    loss = "MSE"
)

model.fit(x, y, epochs = 1000, verbose = 1)
n = int(input("enter the bill amount : \n"))

predict = model.predict(np.array([[n]]))
print("predicted amount : ", predict[0][0])