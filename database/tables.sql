
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
    nut_id int(11) NOT NULL AUTO_INCREMENT,
    nut_type char(1) NOT NULL,
    PRIMARY KEY (nut_id)
)


CREATE TABLE produits (
    prod_id bigint(13) NOT NULL AUTO_INCREMENT,
    prod_name varchar(250) NOT NULL,
    prod_url varchar(150) NOT NULL,
    prod_store varchar(150) NULL,
    nut_id int(11) NOT NULL,
    PRIMARY KEY (prod_id),
    CONSTRAINT fk_nut_id FOREIGN KEY (nut_id) 
        REFERENCES nutriscore (nut_id)
)



CREATE TABLEsauvegardes (
    save_id int(11) NOT NULL AUTO_INCREMENT,
    prod_id bigint(13) NOT NULL,
    save_time datetime NOT NULL,
    PRIMARY KEY (save_id),
    CONSTRAINT fk_saveprod_id FOREIGN KEY (prod_id) 
        REFERENCES produits (prod_id)
)



CREATE TABLE prodcat (
    prodcat_id int(11) NOT NULL AUTO_INCREMENT,
    cat_id int(11) NOT NULL,
    prod_id bigint(13) NOT NULL,
    PRIMARY KEY (prodcat_id),
    CONSTRAINT fk_cat_id FOREIGN KEY (cat_id) 
        REFERENCES categories (cat_id),
    CONSTRAINT fk_prodcatprod_id FOREIGN KEY (prod_id) 
        REFERENCES produits (prod_id)
)



CREATE TABLE prodshop (
    prodshop_id int(11) NOT NULL AUTO_INCREMENT,
    shop_id int(11) NOT NULL,
    prod_id bigint(13) NOT NULL,
    PRIMARY KEY (prodshop_id),
    CONSTRAINT fk_shop_id FOREIGN KEY (shop_id) 
        REFERENCES shops (shop_id),
    CONSTRAINT fk_prodshopprod_id FOREIGN KEY (prod_id) 
        REFERENCES produits (prod_id)
)



CREATE TABLE prodbrand (
    prodbrand_id int(11) NOT NULL AUTO_INCREMENT,
    brand_id int(11) NOT NULL,
    prod_id bigint(13) NOT NULL,
    PRIMARY KEY (prodbrand_id),
    CONSTRAINT fk_brand_id FOREIGN KEY (brand_id) 
        REFERENCES brandues (brand_id),
    CONSTRAINT fk_prodbrandprod_id FOREIGN KEY (prod_id) 
        REFERENCES produits (prod_id)
)




