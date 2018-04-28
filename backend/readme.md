# Endpoints for front-end


## User

### user/create
- id={{firebase uid}}
- @returns None/Failure

### user/get
- id={{firebase uid}}
- @returns {id,uid,first_name,last_name,email,password,street_address,city,country,cc_verified,company_verified,organisation_verified,communities}

### user/edit
- id={{firebase uid}}
- @returns None/Failure

### user/delete
- id={{firebase uid}}
- @returns None/Failure

### user/get_rating
- id={{firebase uid}}
- @returns {rating}

### user/rate
- rator={{firebase uid}}
- rated={{firebase uid}}
- rating={{some number}}
- @returns None/Failure

## Food

### food/get
- id={{food id}}
- @returns {id, title. image_url, owner, street_address, city, country, longitude, latitude, category, price, original_price}

### food/get/all
- No parameters
- @returns [{id, title. image_url, owner, street_address, city, country, longitude, latitude, category, price, original_price}]

### food/create
- title={{food name}}
- image_url={{img url}}
- owner={{firebase uid}}
- street_address={{address}}
- city={{city}}
- country={{country}}
- @returns None/Failure

### food/edit
- id={{food id}}
- title={{food name}}
- image_url={{img url}}
- owner={{firebase uid}}
- street_address={{address}}
- city={{city}}
- country={{country}}
- @returns Non/Failure

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
- @returns {id,name,description,is_public}
#### Optional
- filter={{csv}} for example "categories=porkkana"



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