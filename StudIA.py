import tensorflow as tf
# Accéder à la BDD avec un GUI
# Lancer pgAdmin4

# Installer les packages nécessaires
# virtualenv - -no - site - packages - -distribute.env & & source.env / bin / activate & & pip install - r requirements.txt

# https://cloud.google.com/python/docs/?refresh=1

# Pour activer l'environnement virtuel et les commande
# .\env\Scripts\activate
# deactivate

# ==CONFIG==
# W10x64
# pyton 3.6.8
# Microsoft Visual Redistribution 2015 package 3
# Cuda 9.0
# Cudnn 7.5
# pip install tensorflow-gpu==1.12

print("Hello World!")

print("c'est Ayoub")




hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))