# Recipe Recommender

A [Streamlit](https://streamlit.io/) app that recommends recipes using the [Edamam Recipe API](https://developer.edamam.com/edamam-docs-recipe-api). Pick a meal time, health/diet filters, and a calorie range, and the app returns matching recipes with ingredient lists.

## Features

- Filter recipes by meal type (Breakfast, Lunch, Dinner, Snack)
- Filter by health/diet concerns (dairy-free, gluten-free, vegan, vegetarian, and more)
- Set a minimum and maximum calorie range
- Choose how many results to show
- Optionally randomize which results are shown

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Get free API credentials from [Edamam](https://developer.edamam.com/) for the Recipe Search API.

3. Set the required environment variables:

   ```bash
   export api_id="your-edamam-app-id"
   export api_key="your-edamam-app-key"
   ```

## Running the app

```bash
streamlit run FoodRecs.py
```

Then open the local URL Streamlit prints (usually `http://localhost:8501`) in your browser.

## Requirements

- Python 3.11+
- An Edamam Recipe API `app_id` and `app_key`
