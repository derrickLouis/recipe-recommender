import requests
import streamlit as st
import random
import os

app_id = os.environ["api_id"]
app_key = os.environ["api_key"]

st.set_page_config(#NEW (04)
    page_title="Food Recs App",
    page_icon="🧊",
    layout="wide",)

#Title Page
def title():
    st.header("Welcome to Food Recs!")
    st.subheader("Enter your desired info to the left and watch the magic unfold.")
    st.image("images/food.jpg", width = 200)
    st.write("This app will take your desired filters and give you the ingredients needed to make a recommended dish.")
    st.write("The app uses Edamam's Recipe API to give you only the best reccomendations!")
    st.subheader("Enjoy!")
    st.write("---")
title()
def recipeInfo(time=None, health=None, minimum=None, maximum=None, aCount=10, randomOption=False):
    #url Builder
    baseurl = f"https://api.edamam.com/api/recipes/v2?type=public&app_id={app_id}&app_key={app_key}&dishType=Main%20course"
    if type(health) != None:
        for allergy in health:
            baseurl += f"&health={allergy}"
    baseurl += f"&mealType={time}"
    if minimum <= maximum:
        baseurl += f"&calories={minimum}-{maximum}"
        r = requests.get(baseurl)
        data = r.json()
    else:
        st.write("Sorry! Your minimum can't be more than your max!")
    
    #Print the Recipes
    try:
        recipeCount = data["count"]
        if aCount <= recipeCount:
            iterations = aCount
        else:
            st.write("We don't have that many recipes! But here's what we do have.")
            iterations = 5

        randoList = []
        for num in range(iterations):
            try:
                if randomOption:
                    randomNum = random.randint(0,len(data['hits']))
                    while randomNum in randoList:
                        randomNum = random.randint(0,len(data['hits']))
                    randoList += [randomNum]    
                    st.subheader(f"{data['hits'][randomNum]['recipe']['label']}")
                    foodimg = f"<img src={data['hits'][randomNum]['recipe']['image']} alt='Food' width='100' height='100'>"
                    st.markdown(foodimg, unsafe_allow_html=True)
                    for place,ingredient in enumerate(data['hits'][randomNum]['recipe']['ingredientLines']):
                        st.write(f"{place + 1}. {ingredient}")   
                else:
                    st.subheader(f"{data['hits'][num]['recipe']['label']}")
                    foodimg = f"<img src={data['hits'][num]['recipe']['image']} alt='Food' width='100' height='100'>"
                    st.markdown(foodimg, unsafe_allow_html=True)
                    for place,ingredient in enumerate(data['hits'][num]['recipe']['ingredientLines']):
                        st.write(f"{place + 1}. {ingredient}")
                st.write("---")
            except:
                continue
    except:
        st.write("Aw man there was an issue with your input...check again and everything will be fine.")

#SideBar
st.sidebar.title("Recipe Filters")

time = st.sidebar.radio("Select a Time of Day", ['Breakfast','Dinner','Lunch','Snack'],index=None)
health = st.sidebar.multiselect( #NEW (01)
    'Do you have any of these health concerns?',
    ['dairy-free', 'gluten-free', 'crustacean-free', 'kosher', 'peanut-free',
     'shellfish-free', 'tree-nut-free','vegan','vegetarian','low-sugar'])

minimum = st.sidebar.number_input("Enter a minimum calorie count",step=1,min_value=0,max_value=10000) #NEW (02)
maximum = st.sidebar.number_input("Enter a maximum calorie count",step=1,min_value=0,max_value=10000)

minimum = int(abs(minimum // 1))
maximum = int(abs(maximum // 1))

randomOption = st.sidebar.toggle("Random Options") #NEW (03)

aCount = st.sidebar.number_input("How many results do you want?",step=1,min_value=0,max_value=10000)
recipeInfo(time,health,minimum,maximum,aCount,randomOption)


