-- Activa extensión para UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Borrar tablas si existen (orden correcto por FK)
DROP TABLE IF EXISTS suggestions CASCADE;
DROP TABLE IF EXISTS budgets CASCADE;
DROP TABLE IF EXISTS expenses CASCADE;
DROP TABLE IF EXISTS category_alias CASCADE;
DROP TABLE IF EXISTS categories CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- usuarios
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- catálogo de categorías
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    slug TEXT UNIQUE NOT NULL, -- Identificador interno ("comida", "transporte", etc.)
    display_name TEXT NOT NULL, -- Nombre visible
    budget_pct_hint NUMERIC NULL -- % recomendado del presupuesto
);

-- alias para categorías
CREATE TABLE category_alias (
    id SERIAL PRIMARY KEY,
    category_id INT NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
    alias TEXT NOT NULL -- Alias que van a pasar por un LLM ("tacos", "uber", etc)
);

-- gastos
CREATE TABLE expenses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    --amount_cents INT NOT NULL, -- costo total en centavos
    amount NUMERIC(12,2) NOT NULL,
    --currency CHAR(3) NOT NULL DEFAULT 'MXN',
    expense_date DATE NOT NULL DEFAULT now(), -- Cuando fue el gasto
    note TEXT NULL, -- Anotaciones del usuario
    raw_text TEXT NULL, -- Textto crudo de entrada
    audio_url TEXT NULL, -- Audio original (guardado en S3)
    category_id INT REFERENCES categories(id), --Categoria confirmada
    category_model_score NUMERIC NULL, -- Confianza del modelo al clasificar
    status TEXT NOT NULL CHECK (status IN ('pending','processed')), -- Estatus de la clasificación
    created_at TIMESTAMPTZ NOT NULL DEFAULT now() -- Cuando se insertó el registro
);

-- metas/umbral por categoría
CREATE TABLE budgets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    month DATE NOT NULL, -- Fecha de la meta
    category_id INT REFERENCES categories(id), 
    limit_cents INT NOT NULL -- Límite de gasto
);

-- recomendaciones generadas
CREATE TABLE suggestions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    month DATE NOT NULL, -- A qué mes aplica la recomendación
    kind TEXT NOT NULL, -- e.g., 'reduce_category','set_goal'
    payload JSONB NOT NULL, -- Info completa de la recomendación
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
