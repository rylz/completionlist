DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS template;
DROP TABLE IF EXISTS template_item;
DROP TABLE IF EXISTS list;
DROP TABLE IF EXISTS list_item;

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL,
    username VARCHAR(32) NOT NULL,
    creation_time INT NOT NULL
);

CREATE TABLE IF NOT EXISTS template (
    template_id SERIAL,
    template_name VARCHAR(32) NOT NULL,
    creator_uid INT NOT NULL,
    creation_time INT NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS template_item (
    template_item_id SERIAL,
    template_id INT NOT NULL,
    item_label VARCHAR(64) NOT NULL,
    creation_time INT NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS list (
    template_id INT NOT NULL,
    uid INT NOT NULL,
    creation_time INT NOT NULL,
    details TEXT,
    PRIMARY KEY(template_id, uid)
);

CREATE TABLE IF NOT EXISTS list_item (
    template_item_id INT NOT NULL,
    uid INT NOT NULL,
    template_id INT NOT NULL,
    checked BOOLEAN NOT NULL,
    modified_time INT NOT NULL,
    details TEXT,
    PRIMARY KEY(template_item_id, uid)
);
