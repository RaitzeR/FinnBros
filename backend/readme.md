# Endpoints for front-end


## User

### user/create
- id={{firebase uid}}

- @returns None/Failure

### user/get
- id={{firebase uid}}

- @returns {
  "user": user info,
  "comm_foods": all user foods,
  "comm_comms": all user communities
}

### user/edit
- id={{firebase uid}}

- @returns None/Failure

### user/delete
- id={{firebase uid}}

- @returns None/Failure

### user/get_rating
- id={{firebase uid}}

- @returns
{
  "mean_rating": {{rating}}
}

### user/rate
- rator={{firebase uid}}
- rated={{firebase uid}}
- rating={{some number}}

- @returns None/Failure

## Food

### food/get
- id={{food id}}

- @returns
[
  {
    "model": "foodapp.food",
    "pk": {{backend_db_key}},
    "fields": {
      "title": {{title}},
      "image_url": {{image_url}},
      "user": {{user_backend_db_key}},
      "street_address": {{street_address}},
      "price": {{price}},
      "latitude": {{latitude:float}},
      "longitude": {{longitude:float}},
      "city": {{city}},
      "country": {{country}},
      "is_bought": {{is_bought:bool}},
      "buyer": {{user_backend_db_key}},
      "expiry": {{expiry}},
      "categories": {{list_of_category_bd_keys}}
    }
  }
]

### food/get/all
- No parameters

- @returns all foods as list of dicts in the form of see above

### food/create
- title={{food name}}
- image_url={{img url}}
- owner={{firebase uid}}
- community={{community uid}}
- street_address={{address}}
- city={{city}}
- country={{country}}
- price={{price}}
- expiry={{expiry}}, format: "30.12.2018"

- @returns None/Failure

### food/edit
- id={{food id}}
- title={{food name}}
- image_url={{img url}}
- owner={{firebase uid}}
- community={{community uid}}
- street_address={{address}}
- city={{city}}
- country={{country}}
- price={{price}}
- expiry={{expiry}}, format: "30.12.2018"

- @returns None/Failure

### food/buy
- buyer_id={{firebase uid}}
- id={{food id}}

- @returns None/Failure

### food/delete
- id={{food id}}

- @returns None/Failure


## Community

### community/create
- title={{title}}
- description={{description}}
- is_public={{true/false}}

- @returns None/Failure

### community/get
- id={{community id}}
- OPTIONAL: filter={{csv}} for example "categories=porkkana"

- @returns
{
  "comm": community object information,
  "comm_foods": all community foods,
  "comm_all_categories": all community categories,
  "comm_users": all community users
}





### community/delete
- id={{community id}}

- @returns None/Failure

### community/edit
- title={{title}}
- description={{description}}
- is_public={{true/false}}
- id={{community_id}}

- @returns None/Failure

### community/join_user
- id={{community id}}
- user_id={{firebase uid}}

- @returns None/Failure

### community/leave_user
- id={{community id}}
- user_id={{firebase uid}}

- @returns None/Failure


## Category

### category/categories_to_food
- categories={{csv}} for example "categories=porkkana,juusto,kakku"
- food_id={{food id}}

- @returns None/Failure

### category/remove_categories
- categories={{csv}} for example "categories=porkkana,kakku"
- food_id={{food id}}

- @returns None/Failure


## Watson

### watson/img_categories
- image_url={{image url}}

- @returns [{class,score}]
