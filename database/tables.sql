
CREATE TABLE categorie (
    cat_id      integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    cat_name    varchar(150) NOT NULL
);

CREATE TABLE shops (
  shop_id       integer RIMARY KEY GENERATED ALWAYS AS IDENTITY,
  shop_name     varchar(150) NOT NULL,
)

CREATE TABLE brand (
    brand_id     integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    brand_name   varchar(150) NOT NULL,
)

CREATE TABLE nutriscore (
    nut_id      integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    nut_type    char(1) NOT NULL,
)



CREATE TABLE product (
    prod_id bigint(13) NOT NULL AUTO_INCREMENT,
    prod_name varchar(250) NOT NULL,
    prod_url varchar(150) NOT NULL,
    prod_store varchar(150) NULL,
    nut_id int(11) NOT NULL,
    PRIMARY KEY (prod_id),
    CONSTRAINT fk_nut_id FOREIGN KEY (nut_id) 
        REFERENCES nutriscore (nut_id)
)



CREATE TABLE myproduct (
    save_id int(11) NOT NULL AUTO_INCREMENT,
    user_id 
    prod_id bigint(13) NOT NULL,
    save_time datetime NOT NULL,
    PRIMARY KEY (save_id),
    CONSTRAINT fk_saveprod_id FOREIGN KEY (prod_id) 
        REFERENCES produits (prod_id)
)



CREATE TABLE prodcat (
    cat_id int(11) NOT NULL,
    prod_id bigint(13) NOT NULL,
    CONSTRAINT fk_cat_id FOREIGN KEY (cat_id) 
        REFERENCES categories (cat_id),
    CONSTRAINT fk_prodcatprod_id FOREIGN KEY (prod_id) 
        REFERENCES produits (prod_id)
)



CREATE TABLE prodshop (
    shop_id int(11) NOT NULL,
    prod_id bigint(13) NOT NULL,
    CONSTRAINT fk_shop_id FOREIGN KEY (shop_id) 
        REFERENCES shops (shop_id),
    CONSTRAINT fk_prodshopprod_id FOREIGN KEY (prod_id) 
        REFERENCES produits (prod_id)
)



CREATE TABLE prodbrand (
    brand_id int(11) NOT NULL,
    prod_id bigint(13) NOT NULL,
    CONSTRAINT fk_brand_id FOREIGN KEY (brand_id) 
        REFERENCES brandues (brand_id),
    CONSTRAINT fk_prodbrandprod_id FOREIGN KEY (prod_id) 
        REFERENCES produits (prod_id)
)




