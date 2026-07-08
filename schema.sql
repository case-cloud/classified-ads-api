create table if not exists customers (
    id int primary key auto_increment,
    name varchar(100) not null,
    login varchar(36)
);

create table if not exists products (
    id int primary key auto_increment,
    article varchar(20) not null,
    name varchar(100) not null,
    price decimal(10,2) not null
);

create table if not exists employees (
    id int primary key auto_increment,
    name varchar(100) not null,
    login varchar(36)
);

create table if not exists orders (
    id int primary key auto_increment,
    order_num varchar(20) not null,
    customer_id int,
    employee_id int,
    order_date date not null,
    status varchar(20) not null,
    foreign key (customer_id) references customers(id),
    foreign key (employee_id) references employees(id)
);

create table if not exists order_items (
    id int primary key auto_increment,
    order_id int,
    product_id int,
    qty int not null,
    price decimal(10,2) not null,
    foreign key (order_id) references orders(id),
    foreign key (product_id) references products(id)
);