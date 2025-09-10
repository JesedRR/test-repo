-- Table users
INSERT INTO users (name, last_name, email, password_hash) VALUES 
('Miguel', 'Robles', 'mrob@gmail.com', '1234'),
('Jesed', 'Rizo', 'jriz@gmail.com', '1234');


-- Categorías principales
INSERT INTO categories (slug, display_name, budget_pct_hint)
VALUES
('alimentacion', 'Alimentación y restaurantes', 30),
('transporte', 'Transporte', 10),
('entretenimiento', 'Entretenimiento y ocio', 15),
('vivienda', 'Renta / Hipoteca', 35),
('ahorro', 'Ahorro e inversión', 10),
('salud', 'Salud y medicamentos', 5),
('educacion', 'Educación y formación', 5),
('compras', 'Compras personales', 5),
('otros', 'Otros gastos', NULL);


-- Alimentación
INSERT INTO category_alias (category_id, alias) VALUES
(1, 'tacos'),
(1, 'restaurante'),
(1, 'cena'),
(1, 'comida'),
(1, 'super'),
(1, 'oxxo');

-- Transporte
INSERT INTO category_alias (category_id, alias) VALUES
(2, 'uber'),
(2, 'metro'),
(2, 'taxi'),
(2, 'gasolina'),
(2, 'camion'),
(2, 'avion');

-- Entretenimiento
INSERT INTO category_alias (category_id, alias) VALUES
(3, 'cine'),
(3, 'netflix'),
(3, 'spotify'),
(3, 'bar'),
(3, 'concierto'),
(3, 'videojuegos');

-- Vivienda
INSERT INTO category_alias (category_id, alias) VALUES
(4, 'renta'),
(4, 'hipoteca'),
(4, 'luz'),
(4, 'agua'),
(4, 'internet'),
(4, 'mantenimiento');

-- Ahorro
INSERT INTO category_alias (category_id, alias) VALUES
(5, 'cetes'),
(5, 'inversion'),
(5, 'ahorro'),
(5, 'aportacion'),
(5, 'fondo');

-- Salud
INSERT INTO category_alias (category_id, alias) VALUES
(6, 'farmacia'),
(6, 'doctor'),
(6, 'dentista'),
(6, 'seguro'),
(6, 'hospital');

-- Educación
INSERT INTO category_alias (category_id, alias) VALUES
(7, 'udemy'),
(7, 'colegiatura'),
(7, 'libros'),
(7, 'curso'),
(7, 'plataforma');

-- Compras
INSERT INTO category_alias (category_id, alias) VALUES
(8, 'amazon'),
(8, 'liverpool'),
(8, 'zara'),
(8, 'mercado libre'),
(8, 'ropa'),
(8, 'electrónica');

-- Otros
INSERT INTO category_alias (category_id, alias) VALUES
(9, 'varios'),
(9, 'imprevistos'),
(9, 'regalo');
