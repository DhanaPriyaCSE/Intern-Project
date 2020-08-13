create table ecommerce.users (user_id serial primary key,
				   username varchar not null,
				   password varchar not null)
INSERT into ecommerce.users(username,password) values('priya','priyaammu')

select * from ecommerce.users

create table ecommerce.categories (id varchar primary key not null,
				   name varchar not null,
				   description varchar not null)
				   
INSERT into ecommerce.categories(id,name,description) 
values('C104','Furnitures','Furnitures in this category')

select * from ecommerce.categories

create table ecommerce.products (id varchar primary key not null,
				   name varchar not null,
				   price int not null,
				   quantity int,
				   description varchar not null,
				   FK_category_id  varchar not null,
				   FOREIGN KEY (FK_category_id) REFERENCES ecommerce.categories(id) )
				   
INSERT into ecommerce.products(id,name,price,quantity,description,FK_category_id) 
values('P103','teddy',200,10,'teddy bears','C102')	

select * from ecommerce.products


create table ecommerce.cart(id serial primary key not null,
							user_id int ,
							FOREIGN KEY (user_id) REFERENCES ecommerce.users(user_id) 
						   )

create table ecommerce.cart_product(id serial primary key not null,
							cart_id int not null ,
							product_id varchar not null,
							product_quantity int not null,
							FOREIGN KEY (cart_id) REFERENCES ecommerce.cart(id) ,
							FOREIGN KEY (product_id) REFERENCES ecommerce.products(id)
						   )
					
					
					