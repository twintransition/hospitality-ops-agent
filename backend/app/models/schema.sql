CREATE TABLE guests (
    guest_id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT,
    phone TEXT
);

CREATE TABLE reservations (
    reservation_id SERIAL PRIMARY KEY,
    guest_id INTEGER REFERENCES guests(guest_id),
    check_in DATE,
    check_out DATE,
    room_type TEXT,
    status TEXT
);

CREATE TABLE policies (
    policy_id SERIAL PRIMARY KEY,
    category TEXT,
    title TEXT,
    content TEXT
);

CREATE TABLE conversations (
    conversation_id SERIAL PRIMARY KEY,
    guest_id INTEGER REFERENCES guests(guest_id),
    message TEXT,
    intent TEXT,
    status TEXT
);

CREATE TABLE agent_actions (
    action_id SERIAL PRIMARY KEY,
    conversation_id INTEGER REFERENCES conversations(conversation_id),
    action TEXT,
    decision TEXT,
    approved BOOLEAN DEFAULT FALSE
);
