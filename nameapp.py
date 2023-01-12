
import streamlit as st
from pyngrok import ngrok
import spacy
from spacy import displacy
from faker import Factory

yourname = st.text_input("あなたの名前を教えてください。（例：田中太一）↓")
str = yourname

Clicked = st.button("Click!!")
if Clicked is True:
  yourname_1 = str[0]
  yourname_3 = str[2]

  fake = Factory.create('ja_JP')
  fake_lastname = fake.last_name()
  fake_firstname = fake.first_name()

  num = 0
  while True:
    suggest = fake.last_name()
    if yourname_1 in suggest:
      result_last = suggest
      break
  while True:
    suggest = fake.first_name()
    if yourname_3 in suggest:
      result_first = suggest
      break

  st.write(f"{yourname}さんの芸名は{result_last+result_first}です")





